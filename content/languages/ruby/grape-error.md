---
title: "[Solution] Ruby Grape API Error Fix"
description: "Fix Grape API errors in Ruby. Learn why Grape endpoints fail and how to handle API errors properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Grape API error occurs when a Grape endpoint fails during request processing. Grape is a REST-like API framework, and errors can arise from parameter validation, authentication, or business logic failures.

## Common Causes

- Missing required parameters
- Authentication failure
- Resource not found
- Invalid parameter type

## How to Fix

```ruby
# WRONG: Not validating params
module API
  class Users < Grape::API
    params do
      requires :name, type: String
    end
    get ':id' do
      User.find(params[:id])  # May raise ActiveRecord::RecordNotFound
    end
  end
end

# CORRECT: Handle not found gracefully
module API
  class Users < Grape::API
    params do
      requires :id, type: Integer
    end
    get ':id' do
      user = User.find_by(id: params[:id])
      error!("User not found", 404) unless user
      user
    end
  end
end
```

```ruby
# WRONG: Not handling validation errors
module API
  class Users < Grape::API
    params do
      requires :email, type: String
    end
    post do
      User.create!(params)  # May raise validation error
    end
  end
end

# CORRECT: Rescue and format errors
module API
  class Users < Grape::API
    rescue_from ActiveRecord::RecordInvalid do |e|
      error!(e.message, 422)
    end

    params do
      requires :email, type: String
    end
    post do
      User.create!(params)
    end
  end
end
```

## Examples

```ruby
# Example 1: Basic Grape endpoint
module API
  class Users < Grape::API
    resource :users do
      desc "Return a user"
      params do
        requires :id, type: Integer
      end
      get ':id' do
        User.find(params[:id])
      end
    end
  end
end

# Example 2: Authentication
before do
  error!("Unauthorized", 401) unless current_user
end

# Example 3: Custom error format
error_formatter :json, lambda { |message, backtrace, options, env|
  { error: message }.to_json
}
```

## Related Errors

- [Sinatra application error](sinatra-error) — Sinatra framework error
- [Roda routing error](roda-error) — Roda routing error
- [Hanami action error](hanami-error) — Hanami framework error
