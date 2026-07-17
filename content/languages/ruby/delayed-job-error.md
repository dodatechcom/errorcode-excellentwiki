---
title: "[Solution] Ruby Delayed::Worker Error Fix"
description: "Fix Delayed::Worker errors in Rails. Learn why Delayed::Job workers fail and how to handle background job errors."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Delayed::Worker error occurs when a background job in Delayed::Job fails during execution. The error is recorded in the `delayed_jobs` table and the job may be retried based on configuration.

## Common Causes

- Unhandled exception in job method
- Object serialized but later destroyed
- External service timeout
- Database connection lost during execution

## How to Fix

```ruby
# WRONG: Not handling exceptions
class NewsletterJob
  def perform(user_id)
    user = User.find(user_id)  # May raise if user deleted
    UserMailer.newsletter(user).deliver_now
  end
end

# CORRECT: Handle exceptions gracefully
class NewsletterJob
  def perform(user_id)
    user = User.find_by(id: user_id)
    return unless user
    UserMailer.newsletter(user).deliver_now
  rescue StandardError => e
    Rails.logger.error "Newsletter failed for user #{user_id}: #{e.message}"
  end
end
```

```ruby
# WRONG: Using object references in arguments
Delayed::Job.enqueue NewsletterJob.new(user)  # Serializes entire user

# CORRECT: Use IDs as arguments
Delayed::Job.enqueue NewsletterJob.new(user.id)
```

```ruby
# WRONG: Long-running job without timeout
class SlowJob
  def perform
    sleep 3600  # Blocks worker
  end
end

# CORRECT: Use timeout or break into smaller jobs
class SlowJob
  def perform
    Timeout.timeout(300) do
      # Process in smaller chunks
    end
  end
end
```

## Examples

```ruby
# Example 1: Check failed jobs
Delayed::Job.where("last_error IS NOT NULL").count

# Example 2: Clear failed jobs
Delayed::Job.delete_all("last_error IS NOT NULL")

# Example 3: Retry configuration
Delayed::Worker.max_attempts = 5
Delayed::Worker.max_run_time = 30.minutes
```

## Related Errors

- [Sidekiq worker error](sidekiq-error) — Sidekiq job failure
- [ActiveRecord::RecordNotFound](activerecord-error) — record not found
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
