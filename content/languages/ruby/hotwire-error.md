---
title: "[Solution] Ruby Hotwire Error Fix"
description: "Fix Hotwire errors in Rails. Learn why Hotwire integration fails and how to handle Turbo and Stimulus issues."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Hotwire error occurs when the Hotwire integration (Turbo + Stimulus) fails. Hotwire provides fast,SPA-like navigation and page updates, but errors can arise from configuration issues, response format mismatches, or JavaScript errors.

## Common Causes

- Missing Hotwire gems in Gemfile
- Wrong response format for Turbo
- Stimulus controller not loaded
- Turbo not configured properly

## How to Fix

```ruby
# WRONG: Missing Hotwire gems
# Gemfile missing:
# gem "turbo-rails"
# gem "stimulus-rails"

# CORRECT: Include Hotwire gems
# Gemfile
gem "turbo-rails"
gem "stimulus-rails"
```

```ruby
# WRONG: Not importing Turbo
# app/javascript/application.js missing:
# import "@hotwired/turbo-rails"

# CORRECT: Import Turbo
# app/javascript/application.js
import "@hotwired/turbo-rails"
```

```ruby
# WRONG: Wrong response format
render json: @data  # Turbo expects HTML

# CORRECT: Render HTML for Turbo
render :index  # Renders HTML template
```

## Examples

```ruby
# Example 1: Turbo stream response
turbo_stream.replace("list", partial: "list", locals: { items: @items })

# Example 2: Turbo frame
# app/views/posts/show.html.erb
<turbo-frame id="post_<%= @post.id %>">
  <h1><%= @post.title %></h1>
</turbo-frame>

# Example 3: Stimulus controller
# app/javascript/controllers/hello_controller.js
import { Controller } from "@hotwired/stimulus"
export default class extends Controller {
  greet() { alert("Hello!") }
}
```

## Related Errors

- [Turbo navigation error](turbo-error) — Turbo navigation failed
- [Stimulus controller error](stimulus-error) — Stimulus controller failed
- [Importmap error](importmap-error) — import map issue
