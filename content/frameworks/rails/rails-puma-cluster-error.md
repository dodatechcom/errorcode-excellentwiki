---
title: "[Solution] Rails Puma Cluster Error"
description: "Cluster workers not starting."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Cluster workers not starting.

## Common Causes

Worker count too high.

## How to Fix

Adjust count.

## Example

```ruby
workers ENV.fetch('WEB_CONCURRENCY') { 2 }
```
