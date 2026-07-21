---
title: "[Solution] Rails Active Job Discard Error"
description: "Job not being discarded."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Job not being discarded.

## Common Causes

No discard_on.

## How to Fix

Add discard_on.

## Example

```ruby
class MyJob < ApplicationJob
  discard_on StandardError
end
```
