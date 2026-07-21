---
title: "[Solution] Rails Encrypted Cookie Error"
description: "Fix Rails encrypted cookie decryption error. Resolve ActiveSupport::MessageEncryptor errors in Rails sessions."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Rails tries to decrypt an encrypted cookie but the encryption key or cipher has changed since the cookie was created.

## Common Causes

- `secret_key_base` rotated without clearing existing cookies
- Active Record encryption key is different between environments
- Cookie was encrypted with an older Rails version using a different cipher
- Multiple app instances have different encryption keys
- `config.active_record.encryption.primary_key` changed

## How to Fix

1. Verify consistent encryption keys across environments:

```ruby
# config/credentials.yml.enc or config/secrets.yml
# Ensure these values match on all servers
secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>
```

2. Clear encrypted cookies after key rotation:

```ruby
# In a migration or rake task
Rake::Task['tmp:clear'].invoke
```

3. Handle decryption errors gracefully:

```ruby
class ApplicationController < ActionController::Base
  before_action :reset_session_if_corrupted

  private

  def reset_session_if_corrupted
    reset_session
  rescue ActionController::InvalidAuthenticityToken,
         ActiveSupport::MessageEncryptor::InvalidMessage
    redirect_to login_path, alert: "Session expired. Please log in again."
  end
end
```

4. Use `config.active_record.encryption.support_unencrypted_data` during migration:

```ruby
# config/initializers/encryption.rb
ActiveRecord::Encryption.config.support_unencrypted_data = true # temporary
```

## Examples

```ruby
# Decryption fails after key rotation
session[:user_id] = 1
# ActiveSupport::MessageEncryptor::InvalidMessage: decryption failed

# Multiple servers with different keys
# Server A encrypts with key_a, Server B tries to decrypt with key_b
# InvalidMessage: decryption failed
```
