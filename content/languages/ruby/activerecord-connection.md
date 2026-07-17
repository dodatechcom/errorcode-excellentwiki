---
title: "[Solution] Ruby ActiveRecord::ConnectionNotEstablished Fix"
description: "Fix ActiveRecord::ConnectionNotEstablished in Rails. Learn why database connections fail and how to configure connection pooling."
languages: ["ruby"]
severities: ["error"]
error-types: ["connection-error"]
weight: 5
---

## What This Error Means

An `ActiveRecord::ConnectionNotEstablished` is raised when ActiveRecord cannot establish a connection to the database. This happens when the database server is unreachable, credentials are wrong, or the connection pool is exhausted.

## Common Causes

- Database server is down or unreachable
- Wrong database configuration in `database.yml`
- Connection pool exhausted (too many connections)
- Missing database adapter gem

## How to Fix

```ruby
# WRONG: Not checking database connection
User.all  # ConnectionNotEstablished if DB is down

# CORRECT: Check connection before queries
begin
  ActiveRecord::Base.connection.active?  # true/false
  User.all
rescue ActiveRecord::ConnectionNotEstablished => e
  puts "Database unavailable: #{e.message}"
end
```

```ruby
# WRONG: Wrong database.yml config
production:
  adapter: postgresql
  host: wrong-host  # Connection refused
  database: myapp

# CORRECT: Verify configuration
production:
  adapter: postgresql
  host: <%= ENV['DATABASE_HOST'] %>
  database: <%= ENV['DATABASE_NAME'] %>
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
```

```ruby
# WRONG: Connection pool too small
pool: 2  # Not enough for concurrent requests

# CORRECT: Match pool to thread count
pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
```

```ruby
# WRONG: Not checking for missing adapter
# Gemfile missing: gem 'pg'

# CORRECT: Ensure adapter gem is in Gemfile
# gem 'pg'  # PostgreSQL
# gem 'mysql2'  # MySQL
# gem 'sqlite3'  # SQLite
```

## Examples

```ruby
# Example 1: Test connection
ActiveRecord::Base.connection_pool.with_connection do
  ActiveRecord::Base.connection.execute("SELECT 1")
end

# Example 2: Reconnect after failure
ActiveRecord::Base.clear_active_connections!

# Example 3: Check pool status
ActiveRecord::Base.connection_pool.stat  # {:size=>5, :connections=>2, ...}
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error) — record not found
- [ActiveRecord::RecordInvalid](activerecord-validation) — validation failed
- [ActiveRecord::MigrationError](activerecord-migration) — migration issues
