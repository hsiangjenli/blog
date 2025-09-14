'use strict';

const pagination = require('hexo-pagination');

function getLangList(config) {
  if (Array.isArray(config.language)) return config.language.slice();
  return [config.language || 'en'];
}

function postLangOf(p, fallback) {
  const v = p.lang || p.language;
  return typeof v === 'string' ? v : fallback;
}

// Override archive generator with language-aware routes
hexo.extend.generator.register('archive', function(locals) {
  const { config } = this;

  const langs = getLangList(config);
  const defaultLang = langs[0] || 'en';
  const otherLangs = langs.slice(1);

  let archiveDir = config.archive_dir;
  const paginationDir = config.pagination_dir || 'page';
  const allPostsSorted = locals.posts.sort((config.archive_generator && config.archive_generator.order_by) || '-date');
  const perPage = config.archive_generator && typeof config.archive_generator.per_page !== 'undefined'
    ? config.archive_generator.per_page
    : (typeof config.per_page === 'undefined' ? 10 : config.per_page);

  if (!allPostsSorted.length) return [];
  if (archiveDir[archiveDir.length - 1] !== '/') archiveDir += '/';

  const result = [];

  const self = this;
  function generateFor(lang, basePrefix) {
    const postsLang = allPostsSorted.filter(p => postLangOf(p, defaultLang) === lang);
    if (!postsLang.length) return;

    const base = basePrefix + archiveDir;
    const fmtNum = num => num.toString().padStart(2, '0');

    function generate(path, posts, options = {}) {
      options.archive = true;
      result.push(...pagination(path, posts, {
        perPage,
        layout: ['archive', 'index'],
        format: paginationDir + '/%d/',
        data: options
      }));
    }

    generate(base, postsLang);

    if (!(config.archive_generator && config.archive_generator.yearly)) return;

    const buckets = {};
    postsLang.forEach(post => {
      const date = post.date;
      const year = date.year();
      const month = date.month() + 1;
      if (!Object.prototype.hasOwnProperty.call(buckets, year)) {
        buckets[year] = Array.from({ length: 13 }, () => []);
      }
      buckets[year][0].push(post);
      buckets[year][month].push(post);
      if (config.archive_generator.daily) {
        const day = date.date();
        if (!Object.prototype.hasOwnProperty.call(buckets[year][month], 'day')) {
          buckets[year][month].day = {};
        }
        (buckets[year][month].day[day] || (buckets[year][month].day[day] = [])).push(post);
      }
    });

    const { Query } = self.model('Post');
    const years = Object.keys(buckets);
    for (let i = 0; i < years.length; i++) {
      const y = +years[i];
      const data = buckets[y];
      const url = base + y + '/';
      if (!data[0].length) continue;
      generate(url, new Query(data[0]), { year: y });

      if (!config.archive_generator.monthly && !config.archive_generator.daily) continue;
      for (let m = 1; m <= 12; m++) {
        const monthData = data[m];
        if (!monthData.length) continue;
        if (config.archive_generator.monthly) {
          generate(url + fmtNum(m) + '/', new Query(monthData), { year: y, month: m });
        }
        if (!config.archive_generator.daily) continue;
        for (let d = 1; d <= 31; d++) {
          const dayData = monthData.day && monthData.day[d];
          if (!dayData || !dayData.length) continue;
          generate(url + fmtNum(m) + '/' + fmtNum(d) + '/', new Query(dayData), { year: y, month: m, day: d });
        }
      }
    }
  }

  // Default language at root
  generateFor(defaultLang, '');
  // Other languages under /<lang>/
  otherLangs.forEach(lang => generateFor(lang, lang + '/'));

  return result;
});

// Override tag generator with language-aware routes
hexo.extend.generator.register('tag', function(locals) {
  const config = this.config;
  const langs = getLangList(config);
  const defaultLang = langs[0] || 'en';
  const otherLangs = langs.slice(1);
  const perPage = config.tag_generator && typeof config.tag_generator.per_page !== 'undefined'
    ? config.tag_generator.per_page
    : (typeof config.per_page === 'undefined' ? 10 : config.per_page);
  const paginationDir = config.pagination_dir || 'page';
  const orderBy = (config.tag_generator && config.tag_generator.order_by) || '-date';
  const tags = locals.tags;
  const pages = [];

  function addSet(lang, prefix) {
    tags.forEach(tag => {
      if (!tag.length) return;
      const posts = tag.posts.filter(p => postLangOf(p, defaultLang) === lang).sort(orderBy);
      if (!posts.length) return;
      const path = prefix + tag.path;
      pages.push(...pagination(path, posts, {
        perPage,
        layout: ['tag', 'archive', 'index'],
        format: paginationDir + '/%d/',
        data: { tag: tag.name, lang }
      }));
    });

    if (config.tag_generator && config.tag_generator.enable_index_page) {
      let tagDir = config.tag_dir;
      if (tagDir[tagDir.length - 1] !== '/') tagDir += '/';
      pages.push({
        path: prefix + tagDir,
        layout: ['tag-index', 'tag', 'archive', 'index'],
        posts: locals.posts.filter(p => postLangOf(p, defaultLang) === lang),
        data: {
          base: prefix + tagDir,
          total: 1,
          current: 1,
          current_url: prefix + tagDir,
          posts: locals.posts.filter(p => postLangOf(p, defaultLang) === lang),
          prev: 0,
          prev_link: '',
          next: 0,
          next_link: '',
          tags
        }
      });
    }
  }

  addSet(defaultLang, '');
  otherLangs.forEach(lang => addSet(lang, lang + '/'));
  return pages;
});

// Override category generator with language-aware routes
hexo.extend.generator.register('category', function(locals) {
  const config = this.config;
  const langs = getLangList(config);
  const defaultLang = langs[0] || 'en';
  const otherLangs = langs.slice(1);
  const perPage = config.category_generator && typeof config.category_generator.per_page !== 'undefined'
    ? config.category_generator.per_page
    : (typeof config.per_page === 'undefined' ? 10 : config.per_page);
  const paginationDir = config.pagination_dir || 'page';
  const orderBy = (config.category_generator && config.category_generator.order_by) || '-date';
  const pages = [];

  function addSet(lang, prefix) {
    locals.categories.forEach(category => {
      if (!category.length) return;
      const posts = category.posts.filter(p => postLangOf(p, defaultLang) === lang).sort(orderBy);
      if (!posts.length) return;
      const path = prefix + category.path;
      pages.push(...pagination(path, posts, {
        perPage,
        layout: ['category', 'archive', 'index'],
        format: paginationDir + '/%d/',
        data: { category: category.name, lang }
      }));
    });
  }

  addSet(defaultLang, '');
  otherLangs.forEach(lang => addSet(lang, lang + '/'));
  return pages;
});
