---
title: "[Solution] Ruby Devise Authentication Error Fix"
description: "Fix Devise authentication errors in Rails. Learn why Devise authentication fails and how to configure authentication properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["authentication-error"]
tags: ["devise", "authentication", "login", "rails", "ruby"]
weight: 5
---

## What This Error Means

Devise authentication errors occur when the authentication process fails. Common errors include `InvalidAuthenticityToken`, `InvalidAttempt`, and configuration issues with Devise modules.

## Common Causes

- Wrong email or password
- Account locked due to too many failed attempts
- Missing Devise configuration
- CSRF token mismatch
- Confirmable module not confirmed

## How to Fix

```ruby
# WRONG: Not configuring Devise
# config/initializers/devise.rb missing required settings

# CORRECT: Configure Devise
Devise.setup do |config|
  config.mailer_sender = 'noreply@example.com'
  config.secret_key_base = ENV['DEVISE_SECRET_KEY']
end
```

```ruby
# WRONG: Not handling failed authentication
class SessionsController < ApplicationController
  def create
    # May raise InvalidAuthenticityToken
  end
end

# CORRECT: Handle authentication failure
class SessionsController < ApplicationController
  def create
    user = User.find_by(email: params[:email])
    if user&.valid_password?(params[:password])
      sign_in user
      redirect_to root_path
    else
      flash.now[:alert] = "Invalid email or password"
      render :new
    end
  end
end
```

```ruby
# WRONG: Locked account not handled
class User < ApplicationRecord
  devise :database_authenticatable, :lockable
end

# CORRECT: Handle locked accounts
class User < ApplicationRecord
  devise :database_authenticatable, :lockable,
         maximum_attempts: 5,
         lock_strategy: :failed_attempts
end
```

## Examples

```ruby
# Example 1: Devise modules
class User < ApplicationRecord
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
end

# Example 2: Custom authentication
class CustomSessionsController < Devise::SessionsController
  def create
    super do |resource|
      resource.update(last_login_at: Time.current)
    end
  end
end

# Example 3: Check Devise config
Rails.application.config.to_prepare { Devise.setup do |c| end }
```

## Related Errors

- [CanCan::AccessDenied](rails-can-can-can) — authorization denied
- [Pundit::NotAuthorizedError](rails-pundit-error) — authorization failed
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
