---
title: "[Solution] Rails Puma Thread Error"
description: "Puma thread DB issues."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Puma thread DB issues.

## Common Causes

Pool smaller than threads.

## How to Fix

Match pool to threads.

## Example

```ruby
threads_count = ENV.fetch('RAILS_MAX_THREADS') { 5 }
threads threads_count, threads_count
```
