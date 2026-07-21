---
title: "[Solution] React Client Component Error"
description: "Client component not marked."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Client component not marked.

## Common Causes

Using client features without directive.

## How to Fix

Add 'use client' at top.

## Example

```jsx
'use client';
import { useState } from 'react';
```
