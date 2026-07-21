---
title: "[Solution] Rails Strong Parameters Error"
description: "UnfilteredParameters error."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

UnfilteredParameters error.

## Common Causes

Not calling require.

## How to Fix

Always require then permit.

## Example

```ruby
def article_params
  params.require(:article).permit(:title)
end
```
