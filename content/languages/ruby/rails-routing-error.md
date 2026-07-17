---
title: "[Solution] Rails ActionController::RoutingError Fix"
description: "Fix Rails routing errors when a request hits a route that doesn't exist."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Rails ActionController::RoutingError Fix

A Rails routing error occurs when a request hits a URL that doesn't match any defined route.

## What This Error Means

Rails routes HTTP requests to controller actions. If no route matches the request URL, Rails raises `ActionController::RoutingError`. In production, this typically shows a 404 page.

## Common Causes

- URL typo in the browser or link
- Route not defined in `config/routes.rb`
- HTTP method mismatch (GET vs POST)
- Missing route constraint
- Route order issues

## How to Fix

### 1. Check routes

```ruby
# CORRECT: List all routes
rails routes

# Search for specific route
rails routes | grep users
```

### 2. Define missing routes

```ruby
# WRONG: Missing route
# No route for GET /api/v2/users

# CORRECT: Add the route
# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v2 do
      resources :users, only: [:index, :show]
    end
  end
end
```

### 3. Handle 404 gracefully

```ruby
# CORRECT: Custom 404 page
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  rescue_from ActionController::RoutingError, with: :render_404

  def render_404
    render file: Rails.root.join("public", "404.html"),
           status: :not_found, layout: false
  end
end
```

### 4. Check HTTP method

```ruby
# WRONG: Route defined for POST, but request is GET
# CORRECT: Match HTTP method
get  '/users', to: 'users#index'
post '/users', to: 'users#create'
```

## Related Errors

- [Rails Controller Error](rails-controller-error) — controller issues
- [Rails Template Error](rails-template-error) — missing templates
- [Rails Routing]({{< relref "/languages/ruby/rails-routing" >}}) — routing guide
