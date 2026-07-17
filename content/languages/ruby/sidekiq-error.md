---
title: "[Solution] Ruby Sidekiq Worker Error Fix"
description: "Fix Sidekiq worker errors in Rails. Learn why background jobs fail and how to handle worker exceptions properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sidekiq", "worker", "background-jobs", "rails", "ruby"]
weight: 5
---

## What This Error Means

A Sidekiq worker error occurs when a background job fails during execution. Sidekiq catches exceptions and retries jobs based on configuration, but persistent errors require investigation.

## Common Causes

- Unhandled exception in worker
- External service unavailable
- Redis connection issues
- Serialization errors in arguments

## How to Fix

```ruby
# WRONG: Not handling exceptions in worker
class MyWorker
  include Sidekiq::Worker
  def perform(user_id)
    user = User.find(user_id)  # May raise ActiveRecord::RecordNotFound
    ExternalApi.call(user)      # May raise timeout
  end
end

# CORRECT: Handle exceptions in worker
class MyWorker
  include Sidekiq::Worker
  sidekiq_options retry: 3

  def perform(user_id)
    user = User.find_by(id: user_id)
    return unless user

    ExternalApi.call(user)
  rescue StandardError => e
    Rails.logger.error "Worker failed: #{e.message}"
    raise  # Re-raise for Sidekiq retry
  end
end
```

```ruby
# WRONG: Arguments not serializable
class MyWorker
  include Sidekiq::Worker
  def perform(data)
    # data must be JSON-serializable
  end
end
MyWorker.perform_async(Date.today)  # Serialization error

# CORRECT: Use serializable arguments
MyWorker.perform_async(Date.today.to_s)
```

```ruby
# WRONG: Worker accessing deleted record
class MyWorker
  include Sidekiq::Worker
  def perform(user_id)
    user = User.find(user_id)  # Gone after deletion
    user.update(last_processed: Time.current)
  end
end

# CORRECT: Check existence first
class MyWorker
  include Sidekiq::Worker
  def perform(user_id)
    user = User.find_by(id: user_id)
    return unless user
    user.update(last_processed: Time.current)
  end
end
```

## Examples

```ruby
# Example 1: Check Sidekiq status
Sidekiq::Queue.new.size  # Jobs waiting
Sidekiq::Workers.new.size  # Active workers

# Example 2: Retry configuration
sidekiq_options retry: [1, 5, 10, 30, 60]  # Custom retry schedule

# Example 3: Dead job queue
Sidekiq::DeadSet.new  # Check dead jobs
```

## Related Errors

- [Sidekiq::Worker::TransactionError](rails-sidekiq-error) — transaction conflict
- [Delayed::Worker error](delayed-job-error) — Delayed::Job error
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
