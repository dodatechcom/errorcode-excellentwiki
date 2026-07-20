---
title: "[Solution] Ruby ActionController::ParameterMissing Fix"
description: "Fix ActionController::ParameterMissing: param is missing or the value is empty in Rails. Learn how to properly require and permit strong parameters."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["rails, controllers, parameters, strong-parameters"]
severity: "error"
---

# ActionController::ParameterMissing

## Error Message

```
ActionController::ParameterMissing: param is missing or the value is empty: user
```

## Common Causes

- Calling require(:key) on params when the key does not exist
- Client sending form data in the wrong format (JSON instead of form params)
- Nested parameters missing the parent key entirely
- Content-Type header not set correctly for the request body

## Solutions

### Solution 1: Use require with a Default Fallback

Use permit with safe navigation or provide a default value when the parameter might be absent.

```ruby
# WRONG: require raises if key is missing
def user_params
  params.require(:user).permit(:name, :email)  # ParameterMissing
end

# CORRECT: Use fetch with a default
def user_params
  params.fetch(:user, {}).permit(:name, :email)
end

# CORRECT: Use dig for nested params
def user_params
  params.dig(:user)&.permit(:name, :email) || {}
end
```

### Solution 2: Rescue the Error in Your Controller

Catch ActionController::ParameterMissing and return a user-friendly 422 response instead of a 500 error.

```ruby
class ApplicationController < ActionController::Base
  rescue_from ActionController::ParameterMissing do |exception|
    render json: {
      error: "Missing parameter",
      details: exception.message
    }, status: :unprocessable_entity
  end
end
```

### Solution 3: Ensure Correct Content-Type Header

When sending JSON requests, ensure the Content-Type header is set and params are parsed correctly.

```ruby
# WRONG: Sending JSON without proper Content-Type
# curl -X POST -d '{"user":{"name":"Alice"}}' /users
# Rails sees params as a string, not a hash

# CORRECT: Set Content-Type header
# curl -X POST -H "Content-Type: application/json" \
#   -d '{"user":{"name":"Alice"}}' /users

# In JavaScript fetch:
fetch("/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ user: { name: "Alice" } })
})
```

### Solution 4: Use Strong Parameters with Nested Attributes

Define expected nested structures explicitly to avoid ParameterMissing on complex form submissions.

```ruby
# WRONG: Assuming nested keys exist
def post_params
  params.require(:post).permit(:title, comments: [:body, :author])
end

# CORRECT: Handle optional nested params
def post_params
  permitted = params.require(:post).permit(:title)
  if params[:post][:comments].present?
    permitted.merge(comments: params[:post][:comments].permit(:body, :author))
  else
    permitted
  end
end
```

## Prevention Tips

- Use params.fetch(:key, {}) instead of params.require(:key) when the param is optional
- Always rescue ActionController::ParameterMissing in production
- Set Content-Type: application/json for API requests
- Test both present and absent parameter scenarios

## Related Errors

- [ActionController::InvalidAuthenticityToken]({{< relref "/languages/ruby/rails-csrf-error" >}})
- [ActionController::UnfilteredParameters]({{< relref "/languages/ruby/rails-param-missing" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
