---
title: "[Solution] Rails Record Invalid Error"
description: "save! raises RecordInvalid."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

save! raises RecordInvalid.

## Common Causes

Invalid data.

## How to Fix

Use save or fix data.

## Example

```ruby
if user.save
  redirect_to user
end
```
