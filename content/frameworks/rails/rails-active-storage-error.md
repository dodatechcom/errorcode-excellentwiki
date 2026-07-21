---
title: "[Solution] Rails Active Storage Error"
description: "File upload failing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

File upload failing.

## Common Causes

Storage not configured.

## How to Fix

Check storage.yml.

## Example

```yaml
local:
  service: Disk
  root: <%= Rails.root.join('storage') %>
```
