---
title: "[Solution] Ruby Rack::Cors Error Fix"
description: "Fix Rack::Cors errors in Rails. Learn why CORS requests fail and how to configure cross-origin resource sharing properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["security-error"]
tags: ["rack", "cors", "cross-origin", "rails", "ruby"]
weight: 5
---

## What This Error Means

A `Rack::Cors` error occurs when a cross-origin request is blocked by the CORS middleware. The browser blocks requests from a different origin unless the server explicitly allows them with CORS headers.

## Common Causes

- Missing CORS configuration
- Origin not in allowed list
- Wrong HTTP method not allowed
- Missing headers in allowed list

## How to Fix

```ruby
# WRONG: No CORS configuration
# Rack::Cors blocks all cross-origin requests by default

# CORRECT: Configure CORS in config/initializers/cors.rb
Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins '*'
    resource '*',
      headers: :any,
      methods: [:get, :post, :put, :patch, :delete, :options, :head]
  end
end
```

```ruby
# WRONG: Origin not in allowed list
origins 'https://example.com'  # Request from different origin blocked

# CORRECT: Allow specific origins or use regex
origins 'https://example.com', 'https://app.example.com'
# Or allow all origins (development only)
origins '*'
```

```ruby
# WRONG: Missing allowed headers
resource '*', headers: :none  # Custom headers blocked

# CORRECT: Allow required headers
resource '*',
  headers: :any,
  expose: ['X-Request-Id']
```

## Examples

```ruby
# Example 1: Development CORS (allow all)
origins '*'

# Example 2: Production CORS (specific origins)
origins 'https://app.example.com', 'https://admin.example.com'

# Example 3: Preflight request handling
resource '*',
  methods: [:get, :post, :options],
  max_age: 3600
```

## Related Errors

- [Rack::Utils::HeaderHash error](rails-rack-error) — header manipulation issues
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
- [ActionController::RoutingError](rails-routing) — route not found
