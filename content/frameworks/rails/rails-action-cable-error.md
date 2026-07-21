---
title: "[Solution] Rails Action Cable Error"
description: "WebSocket not connecting."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket not connecting.

## Common Causes

Cable misconfigured.

## How to Fix

Check cable.yml.

## Example

```ruby
development:
  adapter: async
```
