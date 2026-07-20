---
title: "[Solution] Rails ActiveJob — Serialization, Retry, Adapter Errors"
description: "Fix Rails ActiveJob errors. Handle serialization failures, retry configuration, and adapter issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, active_job, sidekiq, retry"]
severity: "error"
---

# Rails ActiveJob Errors

## Error Message

```
ActiveJob::SerializationError: Error serializing ActiveRecord::Base
# or
ActiveJob::DeserializationError: Error deserializing ActiveRecord::Base
# or
Sidekiq::Worker::JobKey: Job argument must be a Hash
```

## Common Causes

- Passing non-serializable objects (non-GlobalID objects) to jobs
- ActiveRecord record deleted before job runs (deserialization error)
- Wrong adapter configuration for job queue
- Job arguments too large for queue storage

## Solutions

### Solution 1: Use GlobalID for ActiveRecord Serialization

Pass ActiveRecord objects via GlobalID for proper serialization.

```ruby
# BAD: passing the object directly
class MyJob < ApplicationJob
  def perform(user)
    # user must be serializable via GlobalID
  end
end
MyJob.perform_later(User.find(1))

# GOOD: pass GlobalID or find by ID
class MyJob < ApplicationJob
  def perform(user_id)
    user = User.find(user_id)
    process(user)
  end
end
MyJob.perform_later(User.find(1).id)
```

### Solution 2: Handle ActiveJob Serialization Errors

Rescue serialization errors and use scalar arguments.

```ruby
class MyJob < ApplicationJob
  queue_as :default

  # Serialize arguments as scalars
  def perform(user_id, options = {})
    user = User.find_by(id: user_id)
    return unless user  # handle deleted records
    process(user, options)
  end
end

# Use GlobalID for automatic serialization
class MyJob < ApplicationJob
  def perform(user)
    # ActiveRecord objects auto-serialize with GlobalID
    process(user)
  end
end
```

### Solution 3: Configure ActiveJob Retry and Discard

Set up retry policies and discard exceptions properly.

```ruby
class MyJob < ApplicationJob
  queue_as :default
  retry_on ActiveRecord::RecordNotFound, wait: 5.seconds, attempts: 3
  discard_on ActiveJob::DeserializationError

  def perform(user_id)
    user = User.find(user_id)
    process(user)
  end
end

# Or use retry_on for transient errors
class MyJob < ApplicationJob
  retry_on Net::ReadTimeout, wait: :polynomially_longer, attempts: 5

  def perform
    call_external_api
  end
end
```

### Solution 4: Configure ActiveJob Adapter

Set the correct adapter in your environment config.

```ruby
# config/environments/development.rb
config.active_job.queue_adapter = :sidekiq

# config/environments/production.rb
config.active_job.queue_adapter = :sidekiq
config.active_job.queue_name_prefix = "myapp_#{Rails.env}"

# Or use inline adapter for testing
config.active_job.queue_adapter = :inline
```

## Prevention Tips

- Pass ActiveRecord IDs instead of objects when possible
- Use `retry_on` for transient errors, `discard_on` for permanent failures
- Set `queue_as` and `queue_name_prefix` to organize jobs
- Test jobs with `assert_enqueued_with` or Sidekiq testing mode

## Related Errors

- [Sidekiq Error]({{< relref "/languages/ruby/rails-sidekiq-error" >}})
- [ActiveRecord::RecordNotFound]({{< relref "/languages/ruby/activerecord-error" >}})
- [SerializationError]({{< relref "/languages/ruby/ruby-marshal-error" >}})
