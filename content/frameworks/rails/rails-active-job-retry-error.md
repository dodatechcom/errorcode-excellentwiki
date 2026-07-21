---
title: "[Solution] Rails Active Job Retry Error"
description: "Job retry not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Job retry not working.

## Common Causes

No retry config.

## How to Fix

Add retry_on.

## Example

```ruby
class MyJob < ApplicationJob
  retry_on ActiveRecord::Deadlocked, wait: 5.seconds, attempts: 3
  discard_on ActiveJob::DeserializationError
end
```
