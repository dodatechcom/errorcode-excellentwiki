---
title: "[Solution] Rails Redis Connection Error"
description: "Fix Rails Redis connection refused error. Resolve Redis connection failures for caching and Action Cable in Rails."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Rails cannot connect to the Redis server configured for caching, sessions, or Action Cable.

## Common Causes

- Redis server is not running or has crashed
- Redis port or host is misconfigured in `config/`
- Connection pool is exhausted under high traffic
- Redis max memory reached and new connections are rejected
- Firewall blocks the Redis port

## How to Fix

1. Verify Redis is running:

```bash
redis-cli ping
# PONG
```

2. Configure the Redis connection in `config/redis.yml`:

```yaml
default: &default
  host: <%= ENV.fetch("REDIS_HOST", "127.0.0.1") %>
  port: <%= ENV.fetch("REDIS_PORT", 6379) %>
  password: <%= ENV["REDIS_PASSWORD"] %>
  db: 0
  connect_timeout: 2
  read_timeout: 1
  write_timeout: 1

development:
  <<: *default

production:
  <<: *default
  url: <%= ENV["REDIS_URL"] %>
```

3. Use connection pooling:

```ruby
# config/initializers/redis.rb
REDIS_POOL = ConnectionPool.new(size: 25, timeout: 3) do
  Redis.new(url: ENV['REDIS_URL'])
end

REDIS_POOL.with do |conn|
  conn.set('key', 'value')
end
```

4. Handle connection failures gracefully:

```ruby
class ApplicationController < ActionController::Base
  rescue_from Redis::CannotConnectError do
    # Fallback to database cache or no cache
    Rails.cache = ActiveSupport::Cache::MemoryStore.new
    retry
  end
end
```

## Examples

```ruby
# Redis server not running
Rails.cache.write('key', 'value')
# Redis::CannotConnectionError: Error connecting to Redis on 127.0.0.1:6379

# Action Cable fails with Redis down
ActionCable.server.broadcast("chat", { message: "hello" })
# Redis::CannotConnectionError: Connection refused
```
