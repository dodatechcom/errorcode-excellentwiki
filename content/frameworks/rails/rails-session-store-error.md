---
title: "[Solution] Rails Session Store Error"
description: "Fix Rails session store configuration error. Resolve undefined session store or ActiveRecord session store failures."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Rails cannot initialize the configured session store, typically due to a missing database table or misconfigured store adapter.

## Common Causes

- ActiveRecord session store is configured but `sessions` table does not exist
- Cookie store is used but cookies are disabled by middleware
- Cache store session fails when cache server is unavailable
- Session store class is missing or not loaded
- `session_store.rb` initializer references an invalid store type

## How to Fix

1. For ActiveRecord session store, run migrations:

```bash
rails generate active_record:session_migration
rails db:migrate
```

2. Configure the session store correctly in the initializer:

```ruby
# config/initializers/session_store.rb
Rails.application.config.session_store :cookie_store,
  key: '_yourapp_session',
  expire_after: 30.days
```

3. For cache-based sessions, ensure the cache is running:

```ruby
Rails.application.config.session_store :cache_store,
  cache_store: Rails.cache
```

4. Verify the session store type:

```ruby
Rails.application.config.session_store.class
# => ActionDispatch::Session::CookieStore
```

## Examples

```ruby
# ActiveRecord session store without migrations
# ActiveRecord::StatementInvalid: PG::UndefinedTable: ERROR:
# relation "sessions" does not exist

# Fix:
rails active_record:session_migration
rails db:migrate

# Cookie store fails when cookies are blocked
# Set-Cookie header missing, sessions cannot be maintained
```
