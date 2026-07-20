---
title: "[Solution] Rails Bullet — N+1 Query Detection and Eager Loading Errors"
description: "Fix Rails N+1 query errors with Bullet gem. Handle eager loading, includes, and performance issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, bullet, n_plus_one, eager_loading"]
severity: "error"
---

# Rails Bullet N+1 Query Errors

## Error Message

```
N+1 Query detected: User => posts
  Add to your finder: User.includes(:posts)
# or
Unused Eager Load detected: User.includes(:posts)
```

## Common Causes

- Accessing associated records without eager loading
- Over-eager loading associations that aren't used
- Dynamic associations not included in includes/joins
- Nested associations requiring nested includes

## Solutions

### Solution 1: Use includes for Simple Eager Loading

Load associations upfront to avoid N+1 queries.

```ruby
# BAD: N+1 query
@users = User.all
@users.each do |user|
  puts user.posts.map(&:title)  # each user triggers a query
end

# GOOD: eager load
@users = User.includes(:posts).all
@users.each do |user|
  puts user.posts.map(&:title)  # no additional queries
end
```

### Solution 2: Use joins for Filtering and Sorting

Use `joins` when you need to filter by association data.

```ruby
# Filter by association attribute
User.joins(:posts).where(posts: { published: true })

# Use preload for separate queries (default for includes)
User.preload(:posts).where(posts: { published: true })

# Use eager_load for single query with LEFT JOIN
User.eager_load(:posts).where(posts: { published: true })
```

### Solution 3: Handle Nested Associations

Include nested associations with hash syntax.

```ruby
# BAD: N+1 on nested associations
@posts = Post.all
@posts.each do |post|
  post.comments.each { |c| c.user.name }  # more N+1 queries
end

# GOOD: nested includes
@posts = Post.includes(comments: :user)
@posts.each do |post|
  post.comments.each { |c| c.user.name }  # no N+1
end
```

### Solution 4: Use Bullet in Development

Configure Bullet to detect and alert on N+1 queries.

```ruby
# Gemfile
gem "bullet"

# config/environments/development.rb
config.after_initialize do
  Bullet.enable = true
  Bullet.alert = true
  Bullet.bullet_logger = true
  Bullet.console = true
  Bullet.rails_logger = true
  Bullet.add_footer = true
end
```

## Prevention Tips

- Enable Bullet gem in development to catch N+1 queries early
- Use `includes` for simple eager loading, `joins` for filtering
- Use `preload` (default) or `eager_load` depending on query needs
- Profile with `bullet` or `rack-mini-profiler` in development

## Related Errors

- [ActiveRecord::N+1 Error]({{< relref "/languages/ruby/activerecord-error" >}})
- [ActiveRecord::QueryError]({{< relref "/languages/ruby/activerecord-connection" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
