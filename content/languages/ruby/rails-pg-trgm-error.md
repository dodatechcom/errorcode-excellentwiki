---
title: "[Solution] Rails PostgreSQL — pg_trgm Trigram Search and GIN Index Errors"
description: "Fix Rails PostgreSQL pg_trgm errors. Handle trigram search, GIN index, and similarity query issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, postgresql, pg_trgm, trigram, search"]
severity: "error"
---

# Rails PostgreSQL pg_trgm Errors

## Error Message

```
PG::UndefinedFunction: function similarity(text, text) does not exist
# or
PG::UndefinedFunction: function trgm_statistic(text) does not exist
# or
ActiveRecord::StatementInvalid: ERROR: operator does not exist: text % text
```

## Common Causes

- pg_trgm extension not installed in PostgreSQL
- Missing GIN or GiST index for trigram queries
- Using similarity functions without enabling the extension
- PostgreSQL version mismatch with trigram features

## Solutions

### Solution 1: Enable pg_trgm Extension

Install the pg_trgm extension in your database.

```ruby
# db/migrate/20260101000000_enable_pg_trgm.rb
class EnablePgTrgm < ActiveRecord::Migration[7.0]
  def up
    execute "CREATE EXTENSION IF NOT EXISTS pg_trgm"
  end

  def down
    execute "DROP EXTENSION IF EXISTS pg_trgm"
  end
end
```

### Solution 2: Add GIN Index for Trigram Search

Create a GIN index for fast trigram similarity queries.

```ruby
# db/migrate/20260101000001_add_trigram_index.rb
class AddTrigramIndex < ActiveRecord::Migration[7.0]
  def change
    add_index :posts, :title, using: :gin, opclass: :gin_trgm_ops
  end
end
```

### Solution 3: Use Trigram Similarity Queries

Query using similarity and percentage operators.

```ruby
# Similarity score
Post.where("title % ?", "search term")
    .order(Arel.sql("similarity(title, 'search term') DESC"))

# Percentage match
Post.where("title %> ?", "search term")

# Trigram distance
Post.where("title <-> ? < 0.5", "search term")
    .order(Arel.sql("title <-> 'search term'"))

# ILIKE with trigram (partial match)
Post.where("title ILIKE ?", "%search%")
```

### Solution 4: Create a Scopable Search Method

Wrap trigram queries in a reusable scope.

```ruby
class Post < ApplicationRecord
  scope :fuzzy_search, ->(query) {
    where("title % :q OR body % :q", q: query)
      .order(Arel.sql("similarity(title, :q) + similarity(body, :q) DESC"), q: query)
  }

  scope :trigram_match, ->(column, query, threshold = 0.3) {
    where("#{column} % :q", q: query)
      .where(Arel.sql("similarity(#{column}, :q) >= :t"), q: query, t: threshold)
  }
end

Post.fuzzy_search("ruby on rails")
Post.trigram_match(:title, "rails", 0.5)
```

## Prevention Tips

- Always `CREATE EXTENSION IF NOT EXISTS pg_trgm` before using trigram features
- Add GIN indexes on columns you search with trigrams
- Use `pg_trgm.similarity_threshold` to control minimum similarity
- Test trigram queries with `EXPLAIN ANALYZE` to verify index usage

## Related Errors

- [ActiveRecord::StatementInvalid]({{< relref "/languages/ruby/activerecord-error" >}})
- [PG::Error]({{< relref "/languages/ruby/activerecord-connection" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
