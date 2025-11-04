// Normalize config.language to a string for templates
// to avoid errors when themes call date helpers expecting strings.

hexo.extend.filter.register('template_locals', function(locals) {
  const cfg = locals.config || {};

  function pickLang(value) {
    if (Array.isArray(value)) return value[0] || 'en';
    if (typeof value === 'string') return value || 'en';
    return 'en';
  }

  const pageLang = locals.page && (locals.page.lang || locals.page.language);
  cfg.language = pickLang(pageLang || cfg.language);

  // Ensure we write back the mutated config
  locals.config = cfg;
  return locals;
});

// Inject a smart language switcher that handles all page types (archives, tags, categories, etc.)
hexo.extend.helper.register('smart_lang_switch', function() {
  const config = this.config || {};
  const page = this.page || {};
  const site = this.site || {};
  const urlFor = this.url_for ? this.url_for.bind(this) : (path => path);

  const langsRaw = Array.isArray(config.language) ? config.language : [config.language || 'en'];
  const langs = langsRaw.filter(Boolean);
  const defaultLang = langs[0] || 'en';

  let currentLang = page.lang || page.language || defaultLang;
  if (!langs.includes(currentLang)) currentLang = defaultLang;

  const targetLang = (langs.find(l => l !== currentLang) || defaultLang) || 'en';

  const root = config.root || '/';

  const ensureLeadingSlash = str => {
    if (!str) return '/';
    return str.startsWith('/') ? str : '/' + str;
  };

  const stripIndex = str => str ? str.replace(/index\.html?$/i, '') : str;

  const stripLangSuffix = segment => {
    if (!segment) return segment;
    let value = segment.replace(/([._-])(zh\-tw|en)$/i, '');
    value = value.replace(/\.(zh\-tw|en)$/i, '');
    return value;
  };

  const currentUrl = page.path ? ensureLeadingSlash(stripIndex(urlFor(page.path)))
    : typeof this.url === 'string' ? ensureLeadingSlash(this.url)
    : root;

  const toArray = collection => {
    if (!collection) return [];
    if (Array.isArray(collection)) return collection;
    if (typeof collection.toArray === 'function') return collection.toArray();
    if (collection.data) return collection.data;
    return [];
  };

  const postsCollection = site.posts || (hexo.locals && typeof hexo.locals.get === 'function' ? hexo.locals.get('posts') : null);
  const posts = toArray(postsCollection);
  const normalizeKey = value => {
    if (!value) return '';
    const base = String(value).toLowerCase();
    const withoutExt = base.replace(/\.[^/.]+$/, '');
    const withoutLocale = withoutExt.replace(/([._-])?(zh\-tw|en)$/, '');
    return withoutLocale.replace(/[^a-z0-9]+/g, '');
  };

  const currentKey = normalizeKey(
    page.translation_key ||
    page.slug ||
    (page.source ? page.source.split('/').pop() : page.path)
  );

  const ensureUrl = path => {
    if (!path) return null;
    if (/^https?:\/\//.test(path)) return path;
    return ensureLeadingSlash(stripIndex(urlFor(path)));
  };

  const getLang = post => post && (post.lang || post.language || defaultLang);

  let preferredUrl = null;

  if (page.layout === 'post') {
    if (page.translations && page.translations[targetLang]) {
      preferredUrl = ensureUrl(page.translations[targetLang]);
    }

    if (!preferredUrl && page.translation_key) {
      const normalizedKey = normalizeKey(page.translation_key);
      if (normalizedKey) {
        const sibling = posts.find(p => {
          if (!p || p.path === page.path) return false;
          if (getLang(p) !== targetLang) return false;
          return normalizeKey(p.translation_key) === normalizedKey;
        });
        if (sibling) preferredUrl = ensureUrl(sibling.path || sibling.permalink);
      }
    }

    if (!preferredUrl && currentKey) {
      const sibling = posts.find(p => {
        if (!p || p.path === page.path) return false;
        if (getLang(p) !== targetLang) return false;
        const key = normalizeKey(
          p.translation_key ||
          p.slug ||
          (p.source ? p.source.split('/').pop() : p.path)
        );
        return key && key === currentKey;
      });
      if (sibling) preferredUrl = ensureUrl(sibling.path || sibling.permalink);
    }
  }

  const stripRoot = url => {
    if (!url) return '';
    let value = url;
    const trimmedRoot = root !== '/' ? root.replace(/\/$/, '') : '';
    if (trimmedRoot && value.startsWith(trimmedRoot + '/')) {
      value = value.slice(trimmedRoot.length + 1);
    } else if (trimmedRoot && value === trimmedRoot) {
      value = '';
    }
    value = value.replace(/^\/+/, '').replace(/\/+$/, '');
    return value;
  };

  const relativePath = stripRoot(stripIndex(currentUrl));
  const segments = relativePath ? relativePath.split('/') : [];
  const hasLangPrefix = segments.length > 0 && langs.includes(segments[0]);
  const restSegments = hasLangPrefix ? segments.slice(1) : segments;

  const computeContentSegments = () => {
    const fromRest = restSegments.slice();
    if (fromRest.length) {
      const lastIdx = fromRest.length - 1;
      fromRest[lastIdx] = stripLangSuffix(fromRest[lastIdx]);
      if (!fromRest[lastIdx]) fromRest.pop();
    }
    if (fromRest.length) return fromRest;

    const slugCandidate = (page.slug || '').trim();
    if (slugCandidate) return [stripLangSuffix(slugCandidate)];

    if (page.source) {
      const baseName = page.source.split('/').pop().replace(/\.[^/.]+$/, '');
      if (baseName) return [stripLangSuffix(baseName)];
    }

    return [];
  };

  const contentSegments = computeContentSegments();

  let fallbackSegments;
  if (targetLang === defaultLang) {
    fallbackSegments = contentSegments.slice();
  } else {
    fallbackSegments = [targetLang, ...contentSegments];
  }

  const fallbackPath = fallbackSegments.join('/');
  let fallbackUrl;
  if (fallbackPath) {
    fallbackUrl = ensureUrl(fallbackPath + '/');
  } else {
    fallbackUrl = targetLang === defaultLang ? ensureUrl('') : ensureUrl(targetLang + '/');
  }

  const finalUrl = preferredUrl || fallbackUrl || ensureUrl('');

  const title = targetLang === 'zh-TW' ? '切換到繁體中文' : 'Switch to English';
  const label = targetLang === 'zh-TW' ? '中文' : 'EN';
  const dataAttr = preferredUrl ? ` data-lang-switch-href="${preferredUrl}"` : '';

  return `<a href="${finalUrl}" title="${title}" aria-label="${title}"${dataAttr}><i class="fas fa-globe"></i> ${label}</a>`;
});

