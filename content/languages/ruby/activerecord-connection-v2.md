---
title: "[Solution] ActiveRecord::ConnectionNotEstablished Error Fix"
description: "Fix ActiveRecord connection errors when Rails cannot connect to the database."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["activerecord", "connection", "database", "rails", "ruby"]
weight: 5
---

# ActiveRecord::ConnectionNotEstablished Error Fix

An ActiveRecord::ConnectionNotEstablished error occurs when Rails cannot establish or find a database connection.

## What This Error Means

ActiveRecord manages a connection pool. This error fires when no connection is available, the database server is unreachable, or `establish_connection` hasn't been called.

## Common Causes

- Database server is down or unreachable
- Wrong credentials in database.yml
- Connection pool exhausted
- Missing `establish_connection` call
- Wrong adapter installed

## How to Fix

### 1. Check database configuration

```ruby
# CORRECT: Verify config/database.yml
development:
  adapter: postgresql
  host: localhost
  username: myuser
  password: mypassword
  database: myapp_development
```

### 2. Test connection

```ruby
# CORRECT: Test database connection
rails db:migrate:status
rails runner "puts ActiveRecord::Base.connection.active?"
```

### 3. Handle connection pool

```ruby
# CORRECT: Configure connection pool
development:
  adapter: postgresql
  pool: 5
  timeout: 5000
```

### 4. Rescue connection errors

```ruby
# CORRECT: Handle connection failures
begin
  user = User.find(1)
rescue ActiveRecord::ConnectionNotEstablished => e
  Rails.logger.error "Database connection failed: #{e.message}"
  redirect_to maintenance_path
end
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error-v2) — record missing
- [ActiveRecord::RecordInvalid](activerecord-validation-v2) — validation failed
- [ActiveRecord::MigrationError](activerecord-migration-v2) — migration issues
