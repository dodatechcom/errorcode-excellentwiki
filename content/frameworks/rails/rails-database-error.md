---
title: "[Solution] Rails Database Error — How to Fix"
description: "Fix Rails database errors. Resolve connection failures, query errors, and ActiveRecord database issues."
frameworks: ["rails"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails database error occurs when ActiveRecord cannot connect, execute queries, or manage transactions.

## Why It Happens

Database errors happen due to connection pool exhaustion, incorrect credentials, timeout issues, deadlocks, or schema mismatches.

## Common Error Messages

```
PG::ConnectionBad: FATAL: database 'myapp' does not exist
```

```
ActiveRecord::ConnectionTimeoutError: could not obtain a database connection
```

```
PG::UnableToSend: canceling statement due to statement timeout
```

```
ActiveRecord::Deadlocked: Deadlock detected
```

## How to Fix It

### 1. Configure Connection Pool

Set the correct pool size.

```yaml
# config/database.yml
production:
  adapter: postgresql
  database: myapp_production
  pool: 5
  timeout: 5000
  url: <%= ENV['DATABASE_URL'] %>
```

### 2. Handle Connection Timeouts

Add retry logic for transient errors.

```ruby
class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true
  retry_on ActiveRecord::ConnectionNotEstablished, wait: 1.second, attempts: 3
  discard_on ActiveRecord::Deadlocked
end
```

### 3. Optimize Slow Queries

Identify and fix slow queries.

```ruby
# Add database indexes
class AddIndexes < ActiveRecord::Migration[7.0]
  def change
    add_index :posts, :user_id
    add_index :posts, [:user_id, :created_at]
  end
end

# Analyze queries
User.includes(:posts).where(posts: { status: 'published' }).explain
```

### 4. Monitor Database Connections

Track connection pool usage.

```ruby
ActiveRecord::Base.connection_pool.stat
```

## Common Scenarios

**Scenario 1: Connection timeout under high traffic.**
Increase pool_size and use pgbouncer.

**Scenario 2: Deadlock during bulk operations.**
Add retry logic and use smaller batches.

**Scenario 3: Connection lost after idle.**
Configure reconnect and pool recovery.

## Prevent It

1. **Use connection pooling.**
Use pgbouncer or pgpool.

2. **Add database monitoring.**
Track connections and query performance.

3. **Write database indexes.**
Index frequently queried columns.

