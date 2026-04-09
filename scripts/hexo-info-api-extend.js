'use strict';

const { sortPosts } = require('./post-sort');

// Extend hexo-info-api to include lang and other custom fields in post objects
// This script provides enhanced API endpoints with additional metadata

function getLangList(config) {
  if (Array.isArray(config.language)) return config.language.slice();
  return [config.language || 'en'];
}

function postLangOf(post, fallback) {
  const v = post.lang || post.language;
  return typeof v === 'string' ? v : fallback;
}

function enhancePostData(post, config, defaultLang) {
  const enhanced = {
    title: post.title,
    date: post.date,
    updated: post.updated,
    description: post.description || post.excerpt || '',
    categories: post.categories.map(cat => ({ name: cat.name, _id: cat._id })),
    tags: post.tags.map(tag => ({ name: tag.name, _id: tag._id })),
    lang: postLangOf(post, defaultLang),
    slug: post.slug,
    _path: post.path,
    _link: config.url + '/' + post.path,
    _id: post._id
  };

  // Add optional custom fields if they exist
  if (post.source_sha) enhanced.source_sha = post.source_sha;
  if (post.origin_lang) enhanced.origin_lang = post.origin_lang;
  if (post.author) enhanced.author = post.author;
  if (post.toc !== undefined) enhanced.toc = post.toc;

  return enhanced;
}

// Register enhanced API routes
hexo.extend.generator.register('enhanced-info-api', function(locals) {
  const config = this.config;
  const langs = getLangList(config);
  const defaultLang = langs[0] || 'en';
  
  if (!config.hexo_info_api || !config.hexo_info_api.enable) {
    return [];
  }

  const routes = [];
  const sortedPosts = sortPosts(locals.posts, ['-updated', '-date']);
  
  // Enhanced getPosts endpoint
  routes.push({
    path: 'api/enhanced/getPosts/',
    data: function() {
      const posts = locals.posts.map(post => enhancePostData(post, config, defaultLang));
      
      return JSON.stringify({
        type: 'getPostsEnhanced',
        data: {
          posts: posts,
          count: posts.length
        }
      });
    }
  });

  // Enhanced getLatestPost endpoint
  routes.push({
    path: 'api/enhanced/getLatestPost/',
    data: function() {
      const latestPost = sortedPosts[0];
      if (!latestPost) {
        return JSON.stringify({
          type: 'getLatestPostEnhanced',
          data: null
        });
      }
      
      const enhanced = enhancePostData(latestPost, config, defaultLang);
      enhanced.content = latestPost.content;
      
      return JSON.stringify({
        type: 'getLatestPostEnhanced',
        data: enhanced
      });
    }
  });

  // Enhanced getLatest5Posts endpoint
  routes.push({
    path: 'api/enhanced/getLatest5Posts/',
    data: function() {
      const posts = sortedPosts.slice(0, 5).map(post => enhancePostData(post, config, defaultLang));
      
      return JSON.stringify({
        type: 'getLatest5PostsEnhanced',
        data: posts
      });
    }
  });

  // Get posts by language - create separate routes for each language
  const availableLanguages = new Set();
  locals.posts.forEach(post => {
    const postLang = postLangOf(post, defaultLang);
    availableLanguages.add(postLang);
  });

  // Create routes for each available language
  availableLanguages.forEach(lang => {
    routes.push({
      path: `api/enhanced/getPostsByLang/${lang}/`,
      data: function() {
        const posts = locals.posts.filter(post => {
          const postLang = postLangOf(post, defaultLang);
          return postLang === lang;
        }).map(post => enhancePostData(post, config, defaultLang));
        
        return JSON.stringify({
          type: 'getPostsByLangEnhanced',
          data: {
            lang: lang,
            posts: posts,
            count: posts.length
          }
        });
      }
    });
  });

  // Get available languages
  routes.push({
    path: 'api/enhanced/getLanguages/',
    data: function() {
      const languagesSet = new Set();
      locals.posts.forEach(post => {
        const postLang = postLangOf(post, defaultLang);
        languagesSet.add(postLang);
      });
      
      const languages = Array.from(languagesSet).map(lang => {
        const count = locals.posts.filter(post => postLangOf(post, defaultLang) === lang).length;
        return { lang, count };
      });
      
      return JSON.stringify({
        type: 'getLanguagesEnhanced',
        data: {
          languages: languages,
          default: defaultLang
        }
      });
    }
  });

  return routes;
});