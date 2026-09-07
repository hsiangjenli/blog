'use strict';

const sharedAssetRoot = 'https://hsiangjenli.github.io/static/shared';
const analyticsId = 'G-RMY40RWC3B';

hexo.extend.injector.register('head_end', `<link rel="stylesheet" href="${sharedAssetRoot}/brand.css">`, 'default');
hexo.extend.injector.register('body_end', `<script>document.body.dataset.analyticsId = '${analyticsId}';</script><script src="${sharedAssetRoot}/brand.js"></script><script src="${sharedAssetRoot}/analytics.js"></script>`, 'default');
