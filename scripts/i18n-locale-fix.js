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
  const config = this.config;
  const page = this.page;
  const currentUrl = this.url;
  
  // Get language list
  const langs = Array.isArray(config.language) ? config.language : [config.language || 'en'];
  const defaultLang = langs[0] || 'en';
  
  // Determine current language from page or URL
  let currentLang = page.lang || page.language || defaultLang;
  
  // If current path starts with a language code, extract it
  const pathLangMatch = currentUrl.match(/^\/([^\/]+)\//);
  if (pathLangMatch && langs.includes(pathLangMatch[1])) {
    currentLang = pathLangMatch[1];
  } else if (!currentUrl.startsWith('/' + currentLang + '/') && currentLang !== defaultLang) {
    // Path doesn't start with current lang, assume default
    currentLang = defaultLang;
  }
  
  // Determine target language (toggle between en and zh-TW)
  const targetLang = currentLang === 'zh-TW' ? 'en' : 'zh-TW';
  
  // Build target URL
  let targetUrl;
  
  if (currentLang === defaultLang) {
    // Currently on default language (no prefix), add target language prefix
    targetUrl = '/' + targetLang + currentUrl;
  } else {
    // Currently on non-default language, need to remove or replace prefix
    const langPrefix = '/' + currentLang + '/';
    if (currentUrl.startsWith(langPrefix)) {
      const pathWithoutLang = currentUrl.substring(langPrefix.length - 1); // keep leading /
      
      if (targetLang === defaultLang) {
        // Going to default language, remove prefix
        targetUrl = pathWithoutLang;
      } else {
        // Going to another non-default language, replace prefix
        targetUrl = '/' + targetLang + pathWithoutLang;
      }
    } else {
      // Fallback: just add target language prefix
      targetUrl = '/' + targetLang + currentUrl;
    }
  }
  
  // Normalize URL (remove double slashes, ensure proper format)
  targetUrl = targetUrl.replace(/\/+/g, '/');
  
  // Add base URL if configured
  const root = config.root || '/';
  if (root !== '/' && !targetUrl.startsWith(root)) {
    targetUrl = root.replace(/\/$/, '') + targetUrl;
  }
  
  const title = targetLang === 'zh-TW' ? '切換到繁體中文' : 'Switch to English';
  
  return `<a href="${targetUrl}" title="${title}" aria-label="${title}"><i class="fas fa-globe"></i> ${targetLang === 'zh-TW' ? '中文' : 'EN'}</a>`;
});

