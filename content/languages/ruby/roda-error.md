---
title: "[Solution] Ruby Roda Routing Error Fix"
description: "Fix Roda routing errors in Ruby. Learn why Roda routes fail and how to handle routing tree errors properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["routing-error"]
weight: 5
---

## What This Error Means

A Roda routing error occurs when the Roda routing tree cannot match a request. Roda uses a tree-based routing approach where each route branch either renders a response or falls through to the next branch.

## Common Causes

- Route branch doesn't match URL
- Missing `r.root` or `r.on` branch
- Wrong HTTP method branch
- Route tree not properly structured

## How to Fix

```ruby
# WRONG: Missing catch-all route
class App < Roda
  route do |r|
    r.on "users" do
      r.is Integer do |id|
        "User #{id}"
      end
    end
    # No fallback — returns 404
  end
end

# CORRECT: Add a root route and catch-all
class App < Roda
  route do |r|
    r.root do
      "Home"
    end

    r.on "users" do
      r.is Integer do |id|
        "User #{id}"
      end
    end

    r.root do
      "Not Found"
    end
  end
end
```

```ruby
# WRONG: Wrong route tree structure
class App < Roda
  route do |r|
    r.on "users" do
      r.get do
        "List users"
      end
      r.post do
        "Create user"
      end
    end
  end
end

# CORRECT: Proper route tree
class App < Roda
  route do |r|
    r.on "users" do
      r.get do
        "List users"
      end

      r.post do
        "Create user"
      end
    end
  end
end
```

## Examples

```ruby
# Example 1: Basic Roda app
class App < Roda
  route do |r|
    r.root do
      "Hello, World!"
    end

    r.on "users" do
      r.is do
        "Users list"
      end

      r.on Integer do |id|
        "User #{id}"
      end
    end
  end
end

# Example 2: Using plugins
class App < Roda
  plugin :render

  route do |r|
    r.root do
      view "index"
    end
  end
end
```

## Related Errors

- [Sinatra application error](sinatra-error) — Sinatra framework error
- [Grape API error](grape-error) — Grape framework error
- [Hanami action error](hanami-error) — Hanami framework error
