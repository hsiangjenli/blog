'use strict';

const pagination = require('hexo-pagination');

function getLangs(config) {
  if (Array.isArray(config.language)) return config.language.slice();
  return [config.language || 'en'];
}

function getPostLang(post, fallback) {
  const v = post.lang || post.language;
  return (typeof v === 'string' && v) ? v : fallback;
}

hexo.extend.generator.register('index', function(locals) {
  const config = this.config || {};
  const langs = getLangs(config);
  const defaultLang = langs[0] || 'en';
  const otherLangs = langs.slice(1);

  const paginationDir = config.pagination_dir || 'page';
  const basePath = (config.index_generator && config.index_generator.path) ? config.index_generator.path : '';
  const perPage = (config.index_generator && typeof config.index_generator.per_page !== 'undefined')
    ? config.index_generator.per_page
    : (typeof config.per_page === 'undefined' ? 10 : config.per_page);
  const orderBy = (config.index_generator && config.index_generator.order_by) || '-date';

  const posts = locals.posts.sort(orderBy);
  posts.data.sort((a, b) => (b.sticky || 0) - (a.sticky || 0));

  const routes = [];

  function genFor(lang, prefix) {
    const filtered = posts.filter(p => getPostLang(p, defaultLang) === lang);
    if (!filtered.length) return;
    const path = prefix + basePath;
    routes.push(...pagination(path, filtered, {
      perPage,
      layout: ['index', 'archive'],
      format: (prefix ? `${prefix}${paginationDir}/%d/` : `${paginationDir}/%d/`),
      data: { __index: true, lang }
    }));
  }

  // Default language at root
  genFor(defaultLang, '');
  // Other languages under /<lang>/
  otherLangs.forEach(lang => genFor(lang, `${lang}/`));

  return routes;
});

