---
title: "[Solution] Ruby ActionController::RoutingError Fix"
description: "Fix ActionController::RoutingError in Rails. Learn why routes don't match and how to configure Rails routing properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["routing-error"]
weight: 5
---

## What This Error Means

An `ActionController::RoutingError` is raised when a request URL doesn't match any defined route in your Rails application. The router cannot find a controller action to handle the request.

## Common Causes

- URL doesn't match any route in `routes.rb`
- Missing route definition for a controller action
- Wrong HTTP method (GET vs POST)
- Route order conflicts

## How to Fix

```ruby
# WRONG: Missing route for controller action
# routes.rb
# No route for UsersController#profile

# CORRECT: Define the route
# routes.rb
resources :users do
  member do
    get :profile
  end
end
```

```ruby
# WRONG: Wrong HTTP method
# routes.rb
get '/posts', to: 'posts#create'  # POST needed, not GET

# CORRECT: Match HTTP method to action
post '/posts', to: 'posts#create'
```

```ruby
# WRONG: Route ordering issue
# routes.rb
get '/users/:id', to: 'users#show'
get '/users/new', to: 'users#new'  # Matched by above route!

# CORRECT: Put specific routes before parameterized ones
get '/users/new', to: 'users#new'
get '/users/:id', to: 'users#show'
```

## Examples

```ruby
# Example 1: Check routes
rails routes | grep users

# Example 2: Nested routes
resources :users do
  resources :posts
end

# Example 3: Custom route
match '/about', to: 'pages#about', via: [:get, :post]
```

## Related Errors

- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
- [ActionView::MissingTemplate](rails-template) — template not found
- [ActionMailer::DeliveryError](rails-mailer) — email delivery failed
