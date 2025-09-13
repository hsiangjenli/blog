'use strict';

// Add a language switch icon to posts that have a translated counterpart.
// Usage in front-matter (either works):
// 1) translation_key: same key across language variants
// 2) translations:
//      en: /path-to-en/
//      zh-TW: /zh-TW/path-to-zh/

const { store: helpers } = hexo.extend.helper;

function getUrl(path) {
  if (!path) return null;
  const fn = helpers && helpers.url_for;
  try {
    return fn ? fn.call(hexo, path) : path;
  } catch (e) {
    return path;
  }
}

hexo.extend.filter.register('after_post_render', function(data) {
  // Only apply to posts, not pages like archives/tags
  if (data.layout !== 'post') return data;

  const langs = Array.isArray(hexo.config.language) ? hexo.config.language : [hexo.config.language || 'en'];
  const defaultLang = langs[0] || 'en';
  const curLang = data.lang || data.language || defaultLang;
  const targetLang = curLang === 'zh-TW' ? 'en' : 'zh-TW';

  let targetUrl = null;

  // Option A: explicit map in front-matter
  if (data.translations && typeof data.translations === 'object') {
    targetUrl = getUrl(data.translations[targetLang]);
  }

  // Option B: find sibling by translation_key
  if (!targetUrl && data.translation_key) {
    const posts = hexo.locals.get('posts');
    const siblings = posts.filter(p => p.translation_key === data.translation_key);
    const target = siblings.find(p => (p.lang || p.language || defaultLang) === targetLang);
    if (target) targetUrl = getUrl(target.path);
  }

  if (!targetUrl) return data;

  const title = targetLang === 'zh-TW' ? '查看繁體中文版本' : 'View English version';
  const iconHtml = `
    <a class="post-lang-switch" href="${targetUrl}" title="${title}" aria-label="${title}">
      <i class="fas fa-language"></i>
    </a>
  `;

  const style = `
    <style>
    .post-lang-switch{
      position: absolute;
      top: .75rem;
      right: .75rem;
      z-index: 2;
      color: var(--link, #3273dc);
    }
    .post-lang-switch:hover{opacity:.8}
    </style>
  `;

  // Prepend the icon inside content area. Icarus wraps post content in .card > article.card-content
  // Injecting at top of content keeps it visible without editing the theme.
  data.content = `${style}${iconHtml}` + (data.content || '');
  return data;
});

