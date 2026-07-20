---
title: "[Solution] Ruby OAuth2 — Token Refresh, Invalid Grant, Redirect URI Errors"
description: "Fix Ruby OAuth2 errors. Handle token refresh failures, invalid grant, redirect URI mismatch, and OAuth flow issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, oauth, oauth2, token, refresh"]
severity: "error"
---

# Ruby OAuth2 Errors

## Error Message

```
OAuth2::Error: invalid_grant
# or
OAuth2::Error: redirect_uri_mismatch
# or
OAuth2::Error: invalid_client
```

## Common Causes

- Authorization code already used or expired
- Redirect URI doesn't match the registered URI
- Refresh token expired or revoked
- Wrong client_id or client_secret

## Solutions

### Solution 1: Set Up OAuth2 Client Correctly

Configure the OAuth2 client with proper credentials.

```ruby
require "oauth2"

client = OAuth2::Client.new(
  ENV["OAUTH_CLIENT_ID"],
  ENV["OAUTH_CLIENT_SECRET"],
  site: "https://provider.example.com",
  authorize_url: "/oauth/authorize",
  token_url: "/oauth/token"
)

# Get authorization URL
auth_url = client.auth_code.authorize_url(
  redirect_uri: "http://localhost:3000/callback",
  scope: "read write"
)
```

### Solution 2: Handle Token Exchange Correctly

Exchange authorization code for tokens with proper redirect URI.

```ruby
begin
  token = client.auth_code.get_token(
    params[:code],
    redirect_uri: "http://localhost:3000/callback"
  )

  # Use the token
  response = token.get("/api/userinfo")
  user_info = JSON.parse(response.body)
rescue OAuth2::Error => e
  puts "OAuth error: #{e.message}"
  # e.code => "invalid_grant", "redirect_uri_mismatch", etc.
end
```

### Solution 3: Refresh Expired Tokens

Implement token refresh with error handling.

```ruby
begin
  # Try to use existing token
  response = token.get("/api/data")

  if response.status == 401
    # Token expired, try refresh
    token = token.refresh!
    response = token.get("/api/data")
  end
rescue OAuth2::Error => e
  if e.code == "invalid_grant"
    # Refresh token expired — re-authorize
    redirect_to client.auth_code.authorize_url(
      redirect_uri: "http://localhost:3000/callback"
    )
  else
    raise
  end
end
```

### Solution 4: Validate Redirect URI

Ensure redirect URI matches exactly what's registered with the provider.

```ruby
# Register exact URIs with the provider:
# - http://localhost:3000/callback (development)
# - https://myapp.com/callback (production)

# Use the exact same URI when exchanging
redirect_uri = if Rails.env.development?
  "http://localhost:3000/callback"
else
  "https://myapp.com/callback"
end

token = client.auth_code.get_token(
  params[:code],
  redirect_uri: redirect_uri
)
```

## Prevention Tips

- Store `client_id` and `client_secret` in environment variables
- Always specify the exact `redirect_uri` when exchanging codes
- Handle 401 responses by attempting token refresh before re-authenticating
- Store refresh tokens securely and set expiration tracking

## Related Errors

- [OAuth2::Error]({{< relref "/languages/ruby/ruby-oauth-error" >}})
- [Net::HTTP Error]({{< relref "/languages/ruby/ruby-net-http-error" >}})
- [JSON::ParserError]({{< relref "/languages/ruby/ruby-json-error" >}})
