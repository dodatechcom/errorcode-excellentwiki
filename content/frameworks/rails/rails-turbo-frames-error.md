---
title: "[Solution] Rails Turbo Frames Error"
description: "Turbo Frames not loading."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Turbo Frames not loading.

## Common Causes

ID mismatch.

## How to Fix

Match IDs.

## Example

```erb
<turbo-frame id="modal"><%= render 'form' %></turbo-frame>
```
