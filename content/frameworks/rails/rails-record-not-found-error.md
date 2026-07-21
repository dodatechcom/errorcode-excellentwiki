---
title: "[Solution] Rails Record Not Found Error"
description: "RecordNotFound raised."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

RecordNotFound raised.

## Common Causes

Record does not exist.

## How to Fix

Use find_by with check.

## Example

```ruby
u = User.find_by(id: params[:id])
raise ActiveRecord::RecordNotFound unless u
```
