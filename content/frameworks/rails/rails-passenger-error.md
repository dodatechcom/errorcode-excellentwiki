---
title: "[Solution] Rails Passenger Error"
description: "Passenger not serving."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Passenger not serving.

## Common Causes

Wrong Nginx config.

## How to Fix

Check config.

## Example

```nginx
server { listen 80; root /app/public; passenger_enabled on; }
```
