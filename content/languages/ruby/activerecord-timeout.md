---
title: "[Solution] Ruby ActiveRecord::ConnectionTimeoutError Fix"
description: "Fix ActiveRecord::ConnectionTimeoutError: could not obtain a database connection within 5.000 seconds. Learn how to tune your connection pool and avoid timeouts."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["activerecord, connection-pool, timeout, database"]
severity: "error"
---

# ActiveRecord::ConnectionTimeoutError

## Error Message

```
ActiveRecord::ConnectionTimeoutError: could not obtain a database connection within 5.000 seconds (waited 5.001 seconds)
```

## Common Causes

- Connection pool size is too small for the number of concurrent threads
- Long-running database queries holding connections and blocking the pool
- Connection leak — connections checked out but never returned to the pool
- Sudden spike in traffic exhausting available connections

## Solutions

### Solution 1: Increase the Connection Pool Size

Match the pool size to your server thread count. If you run Puma with 5 threads, your pool should be at least 5.

```ruby
# database.yml — increase pool size
production:
  adapter: postgresql
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 10 } %>
  timeout: 5

# In Puma config — ensure threads <= pool size
# threads_count = ENV.fetch("RAILS_MAX_THREADS") { 5 }
# threads threads_count, threads_count
```

### Solution 2: Use connection_pool for External Connections

Wrap non-ActiveRecord connections with the connection_pool gem to ensure proper checkout/checkin behavior.

```ruby
require 'connection_pool'

REDIS_POOL = ConnectionPool.new(size: 10, timeout: 3) do
  Redis.new(url: ENV['REDIS_URL'])
end

# Usage with automatic checkin
REDIS_POOL.with do |redis|
  redis.set("key", "value")
end
```

### Solution 3: Detect and Fix Connection Leaks

Manually checkout connections only when necessary, and always ensure they are returned. Use with_connection blocks instead of raw checkout.

```ruby
# WRONG: Manual checkout without return
conn = ActiveRecord::Base.connection_pool.checkout
conn.execute("SELECT 1")
# Connection never returned — causes timeout

# CORRECT: Use with_connection block
ActiveRecord::Base.connection_pool.with_connection do
  ActiveRecord::Base.connection.execute("SELECT 1")
end
```

### Solution 4: Monitor Pool Statistics in Production

Log pool stats periodically to identify when the pool is nearing capacity and adjust before timeouts occur.

```ruby
# Check pool status at any time
stats = ActiveRecord::Base.connection_pool.stat
puts "Size: #{stats[:size]}"
puts "Connections in use: #{stats[:connections]}"
puts "Available: #{stats[:available]}"
puts "Waiting: #{stats[:waiting]}"

# Log pool stats in a periodic task
# config/initializers/pool_monitor.rb
if Rails.env.production?
  Thread.new do
    loop do
      stats = ActiveRecord::Base.connection_pool.stat
      Rails.logger.info "DB Pool: #{stats.inspect}"
      sleep 30
    end
  end
end
```

## Prevention Tips

- Always set pool size to at least match your web server thread count
- Use connection_pool gem for Redis, Memcached, and other non-AR connections
- Monitor connection pool stats in production dashboards
- Set a reasonable timeout value (default is 5 seconds)

## Related Errors

- [ActiveRecord::ConnectionNotEstablished]({{< relref "/languages/ruby/activerecord-connection" >}})
- [ActiveRecord::ConnectionTimeoutError v2]({{< relref "/languages/ruby/activerecord-connection-v2" >}})
- [Connection refused]({{< relref "/languages/ruby/connection-refused" >}})
