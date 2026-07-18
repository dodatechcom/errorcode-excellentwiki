---
title: "[Solution] Rails N+1 Query Error — How to Fix"
description: "Fix Rails N+1 query performance issues. Resolve eager loading problems and optimize ActiveRecord queries."
frameworks: ["rails"]
error-types: ["performance-error"]
severities: ["warning"]
weight: 5
comments: true
---

An N+1 query error occurs when Rails executes one query to fetch a collection and then an additional query for each associated record. This causes severe performance degradation.

## Why It Happens

N+1 queries happen when you iterate over a collection and access associated records without eager loading. ActiveRecord generates individual SQL queries for each association access, resulting in hundreds of queries per request.

## Common Error Messages

```
Bullet gem warning: N+1 Query detected: User.posts
```

```
ActiveRecord::StatementTimeout: canceling statement due to statement timeout
```

```
ActionView::Template::Error: undefined method `posts` for nil:NilClass
```

```
Slow page load times (>5s) for index actions
```

## How to Fix It

### 1. Use includes for Eager Loading

The `includes` method eagerly loads associations to prevent N+1 queries.

```ruby
# Bad - triggers N+1 queries
@users = User.all
@users.each { |u| u.posts.count }

# Good - loads in 2 queries
@users = User.includes(:posts).all
@users.each { |u| u.posts.count }
```

### 2. Use Preload for Explicit Control

`preload` forces a separate query for each association.

```ruby
@users = User.preload(:posts, :comments).order(:name)
```

### 3. Use Eager_load for JOIN Queries

When filtering on associated records, use `eager_load` for a LEFT OUTER JOIN.

```ruby
@users = User.eager_load(:posts).where(posts: { published: true })
```

### 4. Install the Bullet Gem

The Bullet gem detects N+1 queries in development automatically.

```ruby
# Gemfile
gem 'bullet', group: [:development, :test]

# config/environments/development.rb
config.after_initialize do
  Bullet.enable = true
  Bullet.alert = true
end
```

## Common Scenarios

**Scenario 1: Index page loads slowly with 1000+ records.**
Add `includes(:association)` to the query.

**Scenario 2: API endpoint returns thousands of queries.**
Use `includes` for all nested associations in serializers.

**Scenario 3: Background job processes records slowly.**
Eager load associations in the job's query.

## Prevent It

1. **Always use Bullet in development.**
Configure Bullet to show browser alerts for every N+1 query.

2. **Review SQL query count in logs.**
More than 10 queries per request is suspicious.

3. **Use `joins` instead of nested iteration.**
Use `joins` with `select` for filtering instead of loading full objects.

