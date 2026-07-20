---
title: "[Solution] Ruby Rack::Attack — Throttle, Whitelist, Blacklist, Safelist Errors"
description: "Fix Ruby Rack::Attack errors. Handle throttling, whitelisting, blacklisting, and safelist configuration issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, rack_attack, throttle, security"]
severity: "error"
---

# Ruby Rack::Attack Errors

## Error Message

```
Rack::Attack::TooManyRequests: throttled
# or
RuntimeError: Rack::Attack cache store not configured
# or
Rack::Attack::Blocked: request blocked by blacklist
```

## Common Causes

- Cache store not configured for Rack::Attack
- Throttle rules too aggressive or too permissive
- Whitelist/safelist not matching expected requests
- Redis not available for distributed throttling

## Solutions

### Solution 1: Configure Rack::Attack with Cache Store

Set up a cache store for Rack::Attack to track request counts.

```ruby
# config/initializers/rack_attack.rb

# Use Rails cache store
Rack::Attack.cache.store = ActiveSupport::Cache::MemoryStore.new

# Or use Redis for production
Rack::Attack.cache.store = ActiveSupport::Cache::RedisCacheStore.new(
  url: ENV["REDIS_URL"]
)
```

### Solution 2: Set Up Throttling Rules

Configure rate limiting for different endpoints.

```ruby
# config/initializers/rack_attack.rb

# Throttle all requests by IP (5 requests per 30 seconds)
Rack::Attack.throttle("requests/ip", limit: 5, period: 30) do |req|
  req.ip unless req.path.start_with?("/assets")
end

# Throttle login attempts by email
Rack::Attack.throttle("logins/email", limit: 5, period: 60) do |req|
  if req.path == "/users/sign_in" && req.post?
    req.params["email"]&.downcase&.strip
  end
end

# Throttle API requests by token
Rack::Attack.throttle("api/token", limit: 100, period: 60) do |req|
  if req.path.start_with?("/api/")
    req.env["HTTP_AUTHORIZATION"]&.split(" ")&.last
  end
end
```

### Solution 3: Use Whitelist and Safelist

Allow specific IPs or patterns through rate limiting.

```ruby
# config/initializers/rack_attack.rb

# Whitelist specific IPs
Rack::Attack.safelist("allow-localhost") do |req|
  "127.0.0.1" == req.ip || "::1" == req.ip
end

# Whitelist by path
Rack::Attack.safelist("allow-health-check") do |req|
  req.path == "/health"
end

# Blacklist malicious IPs
Rack::Attack.blocklist("block-bad-ips") do |req|
  Rack::Attack::Fail2Ban.filter("pentesters-#{req.ip}", maxretry: 3, findtime: 10.minutes, bantime: 1.hour) do
    CGI.unescape(req.query_string) =~ %r{/etc/passwd} ||
    req.path.include?("wp-admin")
  end
end
```

### Solution 4: Customize Throttled Response

Return proper response codes and headers when rate limited.

```ruby
# config/initializers/rack_attack.rb

Rack::Attack.throttled_responder = lambda do |request|
  match_data = request.env["rack.attack.match_data"]
  now = Time.now

  headers = {
    "Content-Type" => "application/json",
    "Retry-After" => (match_data[:period] - (now.to_i % match_data[:period])).to_s,
    "X-RateLimit-Limit" => match_data[:limit].to_s,
    "X-RateLimit-Remaining" => "0",
    "X-RateLimit-Reset" => (now + (match_data[:period] - now.to_i % match_data[:period])).to_s
  }

  body = { error: "Rate limit exceeded. Try again later." }.to_json

  [429, headers, [body]]
end
```

## Prevention Tips

- Always configure `cache.store` before using throttling
- Use Redis for cache store in production (not MemoryStore)
- Use `safelist` for internal IPs and health check endpoints
- Set `Retry-After` header in throttled responses for client guidance

## Related Errors

- [Redis::CannotConnectError]({{< relref "/languages/ruby/rails-redis-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
