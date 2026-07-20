---
title: "[Solution] Ruby bcrypt — Password Hashing, Cost Factor, InvalidSalt Errors"
description: "Fix Ruby bcrypt errors. Handle InvalidSalt, cost factor configuration, and password hashing issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, bcrypt, password, hashing, security"]
severity: "error"
---

# Ruby bcrypt Errors

## Error Message

```
BCrypt::Errors::InvalidSalt: invalid salt
# or
BCrypt::Errors::InvalidHash: invalid hash
# or
ArgumentError: invalid argument (string)
```

## Common Causes

- Passing a non-bcrypt hash string to `BCrypt::Password.new`
- Salt or hash is corrupted or truncated
- Mixing bcrypt versions with incompatible hash formats
- Using the wrong cost factor

## Solutions

### Solution 1: Hash Passwords Correctly

Use `BCrypt::Password.create` to generate proper hashes.

```ruby
require "bcrypt"

# Hash a password
password = BCrypt::Password.create("my_secret_password")
password.to_s  # => "$2a$12$..."

# Verify a password against a hash
stored_hash = BCrypt::Password.new(password.to_s)
stored_hash == "my_secret_password"  # => true
stored_hash == "wrong_password"      # => false
```

### Solution 2: Handle InvalidSalt Gracefully

Rescue salt errors when loading hashes from the database.

```ruby
require "bcrypt"

def verify_password(plain_password, stored_hash)
  return false if stored_hash.nil? || stored_hash.empty?

  BCrypt::Password.new(stored_hash) == plain_password
rescue BCrypt::Errors::InvalidSalt, BCrypt::Errors::InvalidHash
  false
end

# Usage
if verify_password(params[:password], user.password_digest)
  # authenticated
end
```

### Solution 3: Configure the Cost Factor

Set an appropriate cost factor for security vs performance.

```ruby
require "bcrypt"

# Use a cost factor (higher = slower but more secure)
BCrypt::Password.create("password", cost: 12)

# Use default cost (BCrypt::Engine::DEFAULT_COST = 12)
BCrypt::Password.create("password")

# In Rails, configure in an initializer
# config/initializers/bcrypt.rb
BCrypt::Engine.cost = ENV.fetch("BCRYPT_COST", 12).to_i
```

### Solution 4: Upgrade Hash Cost Factor

Migrate old hashes to a higher cost factor when users log in.

```ruby
require "bcrypt"

def maybe_upgrade_cost(password_digest, plain_password)
  current_cost = BCrypt::Password.new(password_digest).cost
  target_cost = BCrypt::Engine.cost

  if current_cost < target_cost && BCrypt::Password.new(password_digest) == plain_password
    BCrypt::Password.create(plain_password, cost: target_cost).to_s
  else
    password_digest
  end
end
```

## Prevention Tips

- Always use `BCrypt::Password.create` to generate hashes
- Never use plain `BCrypt::Password.new` on untrusted input — it doesn't hash
- Check `BCrypt::Password.new(hash) == password` for verification
- Set `BCRYPT_COST` environment variable for production cost factor

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [SecurityError]({{< relref "/languages/ruby/permission-denied" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
