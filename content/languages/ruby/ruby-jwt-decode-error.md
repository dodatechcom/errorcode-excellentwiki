---
title: "[Solution] Ruby JWT — Decode, Signature Verification, Expired Token Errors"
description: "Fix Ruby JWT errors. Handle decode failures, signature verification, expired tokens, and algorithm issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, jwt, json_web_token, authentication, decode"]
severity: "error"
---

# Ruby JWT Decode Errors

## Error Message

```
JWT::DecodeError: Not enough or too many segments
# or
JWT::ExpiredSignature: Signature has expired
# or
JWT::VerificationError: Signature verification failed
```

## Common Causes

- Malformed JWT token (wrong number of segments)
- Expired token without refresh
- Wrong algorithm used for decoding
- Missing or incorrect secret key

## Solutions

### Solution 1: Decode JWT Tokens Safely

Always decode with the correct algorithm and secret.

```ruby
require "jwt"

secret = "your-secret-key"

# Encode a token
token = JWT.encode(
  { user_id: 1, exp: 24.hours.from_now.to_i },
  secret,
  "HS256"
)

# Decode a token
payload, header = JWT.decode(token, secret, true, { algorithm: "HS256" })
payload["user_id"]  # => 1
```

### Solution 2: Handle Expired Tokens

Check expiration and handle expired tokens gracefully.

```ruby
require "jwt"

begin
  payload, _ = JWT.decode(token, secret, true, {
    algorithm: "HS256",
    verify_expiration: true
  })
rescue JWT::ExpiredSignature
  puts "Token expired — refresh needed"
  refresh_token(token)
rescue JWT::DecodeError => e
  puts "Invalid token: #{e.message}"
end
```

### Solution 3: Verify Algorithm and Signature

Always specify the expected algorithm to prevent algorithm confusion attacks.

```ruby
require "jwt"

# BAD: accepts any algorithm
JWT.decode(token, secret, true)

# GOOD: specify expected algorithm
JWT.decode(token, secret, true, { algorithm: "HS256" })

# For RSA keys
private_key = OpenSSL::PKey::RSA.new(File.read("private.pem"))
public_key = private_key.public_key

token = JWT.encode(payload, private_key, "RS256")
payload, _ = JWT.decode(token, public_key, true, { algorithm: "RS256" })
```

### Solution 4: Handle JWT Decode Errors

Rescue all JWT-specific errors in a structured way.

```ruby
require "jwt"

def decode_token(token, secret)
  JWT.decode(token, secret, true, { algorithm: "HS256" })
rescue JWT::ExpiredSignature
  { error: :expired, message: "Token has expired" }
rescue JWT::VerificationError
  { error: :invalid_signature, message: "Invalid signature" }
rescue JWT::DecodeError => e
  { error: :decode_error, message: e.message }
end

result = decode_token(request_token, secret)
if result.is_a?(Hash) && result[:error]
  render json: { error: result[:message] }, status: :unauthorized
else
  payload, _ = result
  current_user = User.find(payload["user_id"])
end
```

## Prevention Tips

- Always specify `algorithm` when decoding JWTs to prevent algorithm confusion
- Set reasonable expiration times on tokens (15min-1hr for access tokens)
- Use RS256 (asymmetric) for better security than HS256 (symmetric)
- Store secrets in environment variables, never in code

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [SecurityError]({{< relref "/languages/ruby/permission-denied" >}})
- [OpenSSL::SSL::SSLError]({{< relref "/languages/ruby/ruby-net-http-error" >}})
