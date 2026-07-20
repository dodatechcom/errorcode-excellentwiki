---
title: "[Solution] Ruby ActionController::InvalidAuthenticityToken Fix"
description: "Fix ActionController::InvalidAuthenticityToken: Can't verify CSRF token authenticity in Rails. Learn why CSRF verification fails and how to fix it."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["rails, csrf, security, authenticity-token"]
severity: "error"
---

# ActionController::InvalidAuthenticityToken

## Error Message

```
ActionController::InvalidAuthenticityToken (Can't verify CSRF token authenticity)
```

## Common Causes

- CSRF token missing from the form submission or AJAX request
- Session expired or cookie reset, invalidating the stored token
- JavaScript not including the CSRF meta tag token in request headers
- Cross-origin requests not including the authenticity token

## Solutions

### Solution 1: Include CSRF Token in JavaScript Requests

Add the CSRF token from the meta tag to the X-CSRF-Token header for AJAX/fetch requests.

```ruby
# app/views/layouts/application.html.erb
# Include the CSRF meta tag
<%= csrf_meta_tags %>

# JavaScript fetch — include the token
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

fetch("/posts", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-CSRF-Token": csrfToken
  },
  body: JSON.stringify({ title: "Hello" })
})
```

### Solution 2: Skip CSRF Verification for API Endpoints

For API controllers or stateless endpoints, skip CSRF verification using null_session strategy.

```ruby
# WRONG: CSRF check on API endpoint causes failures
class ApiController < ApplicationController
  def create
    # CSRF token missing — InvalidAuthenticityToken
  end
end

# CORRECT: Skip CSRF for API controllers
class ApiController < ActionController::Base
  skip_before_action :verify_authenticity_token
  # Or use null_session for APIs
  protect_from_forgery with: :null_session
end
```

### Solution 3: Verify Token Matches Session

If using server-side session storage, ensure the token in the request matches the token stored in the session.

```ruby
# Custom CSRF verification (advanced)
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  private

  def verified_request?
    super || valid_token_submitted?
  end

  def valid_token_submitted?
    request.headers["X-CSRF-Token"] == session[:_csrf_token]
  end
end
```

### Solution 4: Handle CSRF Errors Gracefully

Rescue the error and return a helpful response instead of a generic 500 page.

```ruby
class ApplicationController < ActionController::Base
  rescue_from ActionController::InvalidAuthenticityToken do |exception|
    respond_to do |format|
      format.html { redirect_to root_path, alert: "Session expired. Please try again." }
      format.json { render json: { error: "Invalid CSRF token" }, status: :forbidden }
    end
  end
end
```

## Prevention Tips

- Always include csrf_meta_tags in your application layout
- For SPAs, pass the CSRF token from a meta tag or cookie to your API client
- Use protect_from_forgery with: :null_session for pure API controllers
- Test CSRF protection — never disable it in production without understanding the risk

## Related Errors

- [ActionController::ParameterMissing]({{< relref "/languages/ruby/rails-param-missing" >}})
- [ActionController::InvalidAuthenticityToken]({{< relref "/languages/ruby/rails-csrf-error" >}})
- [RoutingError]({{< relref "/languages/ruby/routing-error" >}})
