---
title: "[Solution] Rails Mass Assignment Error"
description: "Strong Parameters error."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Strong Parameters error.

## Common Causes

Not using strong params.

## How to Fix

Permit attributes.

## Example

```ruby
def user_params
  params.require(:user).permit(:name, :email)
end
```
