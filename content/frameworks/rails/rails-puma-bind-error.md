---
title: "[Solution] Rails Puma Bind Error"
description: "Puma cannot bind."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Puma cannot bind.

## Common Causes

Port in use.

## How to Fix

Change port.

## Example

```ruby
port ENV.fetch('PORT') { 3000 }
```
