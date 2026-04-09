'use strict';

function toArray(collection) {
  if (!collection) return [];
  if (Array.isArray(collection)) return collection.slice();
  if (typeof collection.toArray === 'function') return collection.toArray();
  if (Array.isArray(collection.data)) return collection.data.slice();
  return Array.from(collection);
}

function toTimestamp(value) {
  if (value == null) return null;

  if (typeof value === 'number') {
    return Number.isFinite(value) ? value : null;
  }

  if (value instanceof Date) {
    const timestamp = value.getTime();
    return Number.isNaN(timestamp) ? null : timestamp;
  }

  if (typeof value === 'string') {
    const cleaned = value.replace(/\s*\([^)]*\)\s*$/, '').trim();
    if (!cleaned) return null;
    const timestamp = Date.parse(cleaned);
    return Number.isNaN(timestamp) ? null : timestamp;
  }

  if (typeof value.toDate === 'function') {
    return toTimestamp(value.toDate());
  }

  if (typeof value.valueOf === 'function') {
    const raw = value.valueOf();
    if (raw !== value) return toTimestamp(raw);
  }

  return null;
}

function toComparableValue(post, field) {
  if (field === 'updated') {
    return toTimestamp(post.updated) ?? toTimestamp(post.date) ?? 0;
  }

  if (field === 'date') {
    return toTimestamp(post.date) ?? 0;
  }

  if (field === 'sticky') {
    const sticky = Number(post.sticky || 0);
    return Number.isFinite(sticky) ? sticky : 0;
  }

  return post[field];
}

function compareValues(left, right, descending) {
  if (left === right) return 0;

  if (left == null) return 1;
  if (right == null) return -1;

  if (typeof left === 'number' && typeof right === 'number') {
    return descending ? right - left : left - right;
  }

  const leftText = String(left);
  const rightText = String(right);
  if (leftText === rightText) return 0;

  if (descending) {
    return rightText.localeCompare(leftText);
  }

  return leftText.localeCompare(rightText);
}

function normalizeOrderBy(orderBy) {
  if (Array.isArray(orderBy) && orderBy.length) return orderBy;
  if (typeof orderBy === 'string' && orderBy.trim()) return [orderBy.trim()];
  return ['-updated', '-date'];
}

function comparePosts(left, right, orderBy) {
  const stickyResult = compareValues(
    toComparableValue(left, 'sticky'),
    toComparableValue(right, 'sticky'),
    true
  );
  if (stickyResult !== 0) return stickyResult;

  for (const token of normalizeOrderBy(orderBy)) {
    const descending = !token.startsWith('+');
    const field = token.replace(/^[+-]/, '');
    const result = compareValues(
      toComparableValue(left, field),
      toComparableValue(right, field),
      descending
    );
    if (result !== 0) return result;
  }

  return compareValues(left.path || left.slug || left.title, right.path || right.slug || right.title, false);
}

function sortPosts(posts, orderBy) {
  return toArray(posts).sort((left, right) => comparePosts(left, right, orderBy));
}

module.exports = {
  comparePosts,
  sortPosts
};