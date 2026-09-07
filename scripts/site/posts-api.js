'use strict';

const { sortPosts } = require('../post-sort');

function languageOf(post, fallback) {
  return post.lang || post.language || fallback;
}

function serializePost(post, config, defaultLanguage) {
  return {
    title: post.title,
    date: post.date,
    updated: post.updated,
    description: post.description || post.excerpt || '',
    lang: languageOf(post, defaultLanguage),
    slug: post.slug,
    url: `${config.url.replace(/\/$/, '')}/${post.path.replace(/^\/+/, '')}`
  };
}

hexo.extend.generator.register('posts-api', function postsApi(locals) {
  const languages = Array.isArray(this.config.language) ? this.config.language : [this.config.language];
  const defaultLanguage = languages[0] || 'en';
  const posts = sortPosts(locals.posts, ['-updated', '-date']).map(post => serializePost(post, this.config, defaultLanguage));
  return [{ path: 'api/posts.json', data: JSON.stringify({ posts }) }];
});
