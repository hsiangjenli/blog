hexo.extend.injector.register('head_begin', '<link rel="stylesheet" href="/blog/css/custom.css" />', 'default');
// hexo.extend.injector.register('head_end', '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9209299049234744" crossorigin="anonymous"></script>', 'default');

// Inject a smart script to toggle the language globe link between EN and zh-TW.
// Handles posts with specific translations, as well as archives/tags/categories pages.
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
    
    function setHref(url){
      if (!url) return;
      a.setAttribute('href', url);
      a.removeAttribute('target');
      a.removeAttribute('rel');
    }

    var explicit = a.getAttribute('data-lang-switch-href');
    if (explicit) {
      setHref(explicit);
      return;
    }

    // If page-level translation switch exists (for posts), use its target
    var postSwitch = document.querySelector('.post-lang-switch');
    if (postSwitch && postSwitch.getAttribute('href')) {
      setHref(postSwitch.getAttribute('href'));
      return;
    } else {
      // Smart path switching for archives, tags, categories, and other pages
      var p = window.location.pathname;
      var base = basePath();
      var segs = p.split('/').filter(Boolean);
      
      // Determine if we're at base level (e.g., /blog/) or root (/)
      var baseSegs = base.split('/').filter(Boolean);
      var idx = baseSegs.length; // Index where language or path starts after base
      
      // Check if current path has zh-TW language prefix
      var inZh = (segs[idx] === 'zh-TW');
      
      var targetUrl;
      if (inZh) {
        // Currently in zh-TW, switch to EN (remove zh-TW prefix)
        var pathSegs = segs.slice(idx + 1); // Remove base + zh-TW
        targetUrl = base + pathSegs.join('/');
        if (pathSegs.length > 0) targetUrl += '/';
      } else {
        // Currently in EN (default), switch to zh-TW (add zh-TW prefix)
        var pathSegs = segs.slice(idx); // Get path after base
        targetUrl = base + 'zh-TW/' + pathSegs.join('/');
        if (pathSegs.length > 0) targetUrl += '/';
        else targetUrl = base + 'zh-TW/'; // Just the language root
      }

      setHref(targetUrl);
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', toggleLangHref);
  } else {
    toggleLangHref();
  }
})();
</script>
`, 'default');
