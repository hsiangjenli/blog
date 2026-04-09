'use strict';

const RecentPosts = require('hexo-component-inferno/lib/view/widget/recent_posts');
const { cacheComponent } = require('hexo-component-inferno/lib/util/cache');
const { sortPosts } = require('./post-sort');

RecentPosts.Cacheable = cacheComponent(RecentPosts, 'widget.recentposts', props => {
  const { site, helper, limit = 5 } = props;
  const { url_for, __, date_xml, date } = helper;

  if (!site.posts.length) {
    return null;
  }

  const posts = sortPosts(site.posts, ['-updated', '-date']).slice(0, limit).map(post => {
    return {
      url: url_for(post.link || post.path),
      title: post.title,
      date: date(post.date),
      dateXml: date_xml(post.date),
      thumbnail: post.thumbnail ? url_for(post.thumbnail) : null,
      categories: post.categories.map(category => {
        return {
          name: category.name,
          url: url_for(category.path)
        };
      })
    };
  });

  return {
    posts,
    title: __('widget.recents')
  };
});