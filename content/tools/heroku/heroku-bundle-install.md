---
title: "[Solution] Heroku Bundle Install Error"
description: "Fix Heroku bundle install errors. Resolve Ruby gem installation issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Bundle Install Error can prevent your application from working correctly.

## Common Causes

- Gem not found
- Version conflict
- Native extension failed

## How to Fix

### Check Gemfile

```ruby
ruby '3.1.0'
gem 'rails', '~> 7.0'
```

