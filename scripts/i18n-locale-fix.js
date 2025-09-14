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

