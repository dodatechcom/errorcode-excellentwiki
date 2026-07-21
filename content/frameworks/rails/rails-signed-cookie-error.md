---
title: "[Solution] Rails Signed Cookie Error"
description: "Fix Rails InvalidAuthenticityToken or cookie signature invalid. Resolve signed cookie verification failures in Rails."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Rails cannot verify the signature of a signed or encrypted cookie, usually because the `secret_key_base` has changed.

## Common Causes

- `secret_key_base` was regenerated without invalidating existing sessions
- Cookie store secret differs between deployment environments
- Cookie was set by a different app or subdomain
- Cookie exceeds the maximum size (4KB per cookie)
- Tampered or corrupted cookie value

## How to Fix

1. Ensure `secret_key_base` is consistent across deployments:

```text
# .env
SECRET_KEY_BASE=your-long-random-string
```

2. Flush old sessions after changing the key:

```bash
# Clear the sessions store
rm -rf tmp/sessions/*
# Or flush Redis if using cache-based sessions
redis-cli FLUSHDB
```

3. Use encrypted cookies instead of signed cookies:

```ruby
# Safer: encrypted cookies (signed + encrypted)
cookies.encrypted[:user_id] = current_user.id

# Signed only (tamper-proof but readable)
cookies.signed[:user_id] = current_user.id
```

4. Set cookie expiration to handle staleness:

```ruby
cookies[:session_id] = {
  value: session.id,
  expires: 30.days.from_now,
  httponly: true,
  secure: Rails.env.production?
}
```

## Examples

```ruby
# secret_key_base changed, old sessions break
# ActionDispatch::Cookies::InvalidAuthenticityToken
# or
# ActionController::InvalidAuthenticityToken

# Cookies tampered with
cookies.signed[:data] = "original"
# Later, if cookie is modified externally:
# ActionController::InvalidAuthenticityToken: Can't verify CSRF token authenticity
```
