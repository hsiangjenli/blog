'use strict';

function escapeHtml(value) {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

hexo.extend.filter.register('before_post_render', post => {
  const markdown = post.raw || post.content || '';
  const rendered = markdown.replace(/```mermaid\s*\n([\s\S]*?)```/g, (_, diagram) => `<pre class="mermaid">${escapeHtml(diagram.trim())}</pre>`);
  post.raw = rendered;
  post.content = rendered;
  return post;
});

hexo.extend.injector.register('body_end', `<script>
if (document.querySelector('.mermaid')) {
  import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs')
    .then(({ default: mermaid }) => mermaid.initialize({ startOnLoad: true }));
}
</script>`, 'default');
