---
title: "[Solution] Ruby Sidekiq::Worker::TransactionError Fix"
description: "Fix Sidekiq::Worker::TransactionError in Rails. Learn why Sidekiq worker transactions fail and how to handle database transactions in background jobs."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A `Sidekiq::Worker::TransactionError` is raised when a Sidekiq worker tries to access the database after a transaction has been rolled back. This commonly happens when a transaction wraps a background job that accesses the same database connection.

## Common Causes

- Background job started inside a database transaction
- Worker accesses record after transaction rollback
- Multiple workers sharing same database connection
- Transaction timeout during worker execution

## How to Fix

```ruby
# WRONG: Starting job inside transaction
ActiveRecord::Base.transaction do
  user = User.create!(name: "Alice")
  WelcomeEmailWorker.perform_async(user.id)  # TransactionError if rolled back
end

# CORRECT: Start job after transaction commits
ActiveRecord::Base.transaction do
  user = User.create!(name: "Alice")
end
WelcomeEmailEmailWorker.perform_async(user.id)
```

```ruby
# WRONG: Worker accessing stale record
class MyWorker
  include Sidekiq::Worker
  def perform(user_id)
    user = User.find(user_id)  # May fail if transaction rolled back
    # ...
  end
end

# CORRECT: Handle missing record in worker
class MyWorker
  include Sidekiq::Worker
  def perform(user_id)
    user = User.find_by(id: user_id)
    return unless user
    # ...
  end
end
```

## Examples

```ruby
# Example 1: After commit callback
class User < ApplicationRecord
  after_commit :send_welcome_email, on: :create

  def send_welcome_email
    WelcomeEmailWorker.perform_async(id)
  end
end

# Example 2: Sidekiq middleware
Sidekiq.configure_server do |config|
  config.server_middleware do |chain|
    chain.add Sidekiq::Middleware::Server::RetryJobs
  end
end
```

## Related Errors

- [Sidekiq worker error](sidekiq-error) — general Sidekiq worker issues
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
- [ActiveRecord::RecordInvalid](activerecord-validation) — validation failed
