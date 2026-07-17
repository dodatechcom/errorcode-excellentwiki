---
title: "[Solution] Ruby Redis::CannotConnectError Fix"
description: "Fix Redis::CannotConnectError in Rails. Learn why Redis connections fail and how to configure connection pooling."
languages: ["ruby"]
severities: ["error"]
error-types: ["connection-error"]
tags: ["redis", "cannot-connect", "connection", "rails", "ruby"]
weight: 5
---

## What This Error Means

A `Redis::CannotConnectError` is raised when the Redis client cannot establish a connection to the Redis server. This can happen when Redis is down, unreachable, or misconfigured.

## Common Causes

- Redis server not running
- Wrong host/port configuration
- Redis server overloaded or out of memory
- Connection pool exhausted

## How to Fix

```ruby
# WRONG: Not checking Redis connection
Redis.current.get("key")  # CannotConnectError if Redis is down

# CORRECT: Check connection before use
begin
  redis = Redis.new(url: ENV['REDIS_URL'])
  redis.ping  # "PONG"
rescue Redis::CannotConnectError => e
  puts "Redis unavailable: #{e.message}"
end
```

```ruby
# WRONG: Wrong Redis configuration
# config/initializers/redis.rb
REDIS = Redis.new(host: "wrong-host", port: 6379)

# CORRECT: Use environment variables
REDIS = Redis.new(url: ENV.fetch("REDIS_URL", "redis://localhost:6379/0"))
```

```ruby
# WRONG: Not using connection pool
REDIS = Redis.new  # Single connection, may exhaust

# CORRECT: Use connection pool
REDIS = ConnectionPool.new(size: 5, timeout: 3) do
  Redis.new(url: ENV['REDIS_URL'])
end

REDIS.with { |conn| conn.get("key") }
```

## Examples

```ruby
# Example 1: Test Redis connection
Redis.new.ping  # "PONG"

# Example 2: Redis URL format
ENV['REDIS_URL']  # "redis://localhost:6379/0"

# Example 3: Handle Redis errors
begin
  redis.set("key", "value")
rescue Redis::CannotConnectError => e
  Rails.logger.warn "Redis unavailable: #{e.message}"
end
```

## Related Errors

- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
- [ActionController::RoutingError](rails-routing) — route not found
- [Sidekiq::Worker::TransactionError](rails-sidekiq-error) — Sidekiq worker error
