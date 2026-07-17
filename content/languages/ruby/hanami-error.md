---
title: "[Solution] Ruby Hanami Action Error Fix"
description: "Fix Hanami action errors in Ruby. Learn why Hanami controller actions fail and how to handle action errors properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Hanami action error occurs when a Hanami controller action fails during request handling. Hanami actions are plain Ruby objects with a `call` method, and errors can arise from parameter validation, view rendering, or application logic.

## Common Causes

- Missing required parameters
- View template not found
- Unhandled exception in action
- Missing action method

## How to Fix

```ruby
# WRONG: Not handling missing params
class Articles::Show
  include Hanami::Action

  def handle(req, res)
    article = ArticleRepository.new.find(req.params[:id])  # nil if missing
    res.body = article.title  # NoMethodError
  end
end

# CORRECT: Validate params first
class Articles::Show
  include Hanami::Action

  def handle(req, res)
    article = ArticleRepository.new.find(req.params[:id])
    if article
      res.body = article.title
    else
      res.status = 404
      res.body = "Article not found"
    end
  end
end
```

```ruby
# WRONG: Action without proper error handling
class Articles::Create
  include Hanami::Action

  def handle(req, res)
    ArticleRepository.new.create(req.params)
  end
end

# CORRECT: Handle validation errors
class Articles::Create
  include Hanami::Action

  def handle(req, res)
    result = ArticleContract.new.call(req.params)
    if result.success?
      article = ArticleRepository.new.create(result.to_h)
      res.status = 201
      res.body = article.to_json
    else
      res.status = 422
      res.body = result.errors.to_h.to_json
    end
  end
end
```

## Examples

```ruby
# Example 1: Basic action
class Home::Index
  include Hanami::Action

  def handle(req, res)
    res.body = "Hello, World!"
  end
end

# Example 2: Expose to view
class Articles::Show
  include Hanami::Action
  expose :article

  def handle(req, res)
    @article = ArticleRepository.new.find(req.params[:id])
  end
end
```

## Related Errors

- [Grape API error](grape-error) — Grape framework error
- [Sinatra application error](sinatra-error) — Sinatra framework error
- [Roda routing error](roda-error) — Roda routing error
