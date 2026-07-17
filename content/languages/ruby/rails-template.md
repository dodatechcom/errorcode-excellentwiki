---
title: "[Solution] Ruby ActionView::MissingTemplate Fix"
description: "Fix ActionView::MissingTemplate in Rails. Learn why view templates aren't found and how to configure template lookup."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["actionview", "template", "missing-template", "rails", "ruby"]
weight: 5
---

## What This Error Means

An `ActionView::MissingTemplate` is raised when Rails cannot find a view template for the requested action. This happens when the template file doesn't exist in the expected location or with the expected format.

## Common Causes

- Template file doesn't exist
- Wrong template format (HTML vs JSON)
- Missing template for a response format
- Template path incorrect

## How to Fix

```ruby
# WRONG: Missing template file
class PostsController < ApplicationController
  def show
    # Expects app/views/posts/show.html.erb
  end
end

# CORRECT: Create the template file
# app/views/posts/show.html.erb
<h1><%= @post.title %></h1>
```

```ruby
# WRONG: Wrong format response
class ApiController < ApplicationController
  def index
    render :index  # Tries to render HTML template
  end
end

# CORRECT: Render correct format
class ApiController < ApplicationController
  def index
    render json: @posts
  end
end
```

```ruby
# WRONG: Template in wrong location
# app/views/admin/posts/show.html.erb
class PostsController < ApplicationController
  def show
    # Looks in app/views/posts/, not admin/posts/
  end
end

# CORRECT: Specify template path
def show
  render "admin/posts/show"
end
```

## Examples

```ruby
# Example 1: List templates
ActionView::Template::Handlers.extensions  # [".erb", ".html.erb", ...]

# Example 2: Multiple formats
respond_to do |format|
  format.html  # render :index.html.erb
  format.json  # render json: @posts
end

# Example 3: Default template
def show
  render :show  # Looks for show.html.erb
end
```

## Related Errors

- [ActionController::RoutingError](rails-routing) — route not found
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
- [ActionMailer::DeliveryError](rails-mailer) — email delivery failed
