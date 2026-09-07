# Posts API

The generated site exposes one intentionally small public endpoint:

```
GET /blog/api/posts.json
```

It returns posts ordered by update date. Each entry contains `title`, `date`,
`updated`, `description`, `lang`, `slug`, and its canonical `url`. Consumers
filter by `lang`; no post content or internal Hexo metadata is exposed.
