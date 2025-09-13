hexo.extend.injector.register('head_begin', '<link rel="stylesheet" href="/blog/css/custom.css" />', 'default');
hexo.extend.injector.register('head_end', '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9209299049234744" crossorigin="anonymous"></script>', 'default');

// Inject a tiny script to toggle the language globe link between EN and zh-TW.
// If current page is a post with a specific translation target, set the navbar icon to that target.
hexo.extend.injector.register('body_end', `
<script>
(function(){
  function basePath() {
    var p = window.location.pathname; // e.g. /blog/zh-TW/...
    var segs = p.split('/').filter(Boolean);
    // If first segment is 'blog', treat '/blog/' as base; otherwise '/'
    return (segs[0] === 'blog') ? '/blog/' : '/';
  }
  function toggleLangHref(){
    var a = document.querySelector('.navbar .navbar-end a.navbar-item[title="Language"]');
    if(!a) return;
    // If page-level translation switch exists, use its target
    var postSwitch = document.querySelector('.post-lang-switch');
    if (postSwitch && postSwitch.getAttribute('href')) {
      a.setAttribute('href', postSwitch.getAttribute('href'));
    } else {
      var p = window.location.pathname;
      var base = basePath();
      var segs = p.split('/').filter(Boolean);
      var idx = (base === '/blog/') ? 1 : 0;
      var inZh = (segs[idx] === 'zh-TW');
      var href = inZh ? base : base + 'zh-TW/';
      a.setAttribute('href', href);
    }
    // open in same tab
    a.removeAttribute('target');
    a.removeAttribute('rel');
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', toggleLangHref);
  } else {
    toggleLangHref();
  }
})();
</script>
`, 'default');
