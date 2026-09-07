'use strict';

function languages() {
  return Array.isArray(hexo.config.language) ? hexo.config.language : [hexo.config.language || 'en'];
}

function postLanguage(post, fallback) {
  return post.lang || post.language || fallback;
}

hexo.extend.filter.register('template_locals', function normalizeTemplateLanguage(locals) {
  const configured = languages();
  const page = locals.page || {};
  const pageLanguage = page.lang || page.language || configured[0] || 'en';
  locals.config.language = typeof pageLanguage === 'string' ? pageLanguage : configured[0] || 'en';
  return locals;
});

function translatedPath(post, targetLanguage, defaultLanguage) {
  if (post.translations && post.translations[targetLanguage]) return post.translations[targetLanguage];
  const sibling = hexo.locals.get('posts').find(candidate => candidate.path !== post.path && candidate.slug === post.slug && postLanguage(candidate, defaultLanguage) === targetLanguage);
  return sibling && sibling.path;
}

hexo.extend.filter.register('after_post_render', function addPostLanguageSwitch(post) {
  if (post.layout !== 'post') return post;
  const configured = languages();
  const defaultLanguage = configured[0] || 'en';
  const currentLanguage = postLanguage(post, defaultLanguage);
  const targetLanguage = configured.find(language => language !== currentLanguage);
  const targetPath = targetLanguage && translatedPath(post, targetLanguage, defaultLanguage);
  if (!targetPath) return post;
  const title = targetLanguage === 'zh-TW' ? '查看繁體中文版本' : 'View English version';
  post.content = `<a class="post-lang-switch" href="${targetPath}" title="${title}" aria-label="${title}"><i class="fas fa-language"></i></a>${post.content || ''}`;
  return post;
});

hexo.extend.injector.register('head_end', '<style>.post-lang-switch{float:right;color:var(--link,#3273dc)}</style>', 'default');
hexo.extend.injector.register('body_end', `<script>(() => { const link = document.querySelector('.navbar .navbar-end a.navbar-item[title="Language"]'); if (!link || document.querySelector('.post-lang-switch')) return; const path = location.pathname.replace(/^\\/blog\\/?/, '').replace(/^zh-TW\\/?/, ''); link.href = location.pathname.includes('/zh-TW/') ? '/blog/' + path : '/blog/zh-TW/' + path; })();</script>`, 'default');
