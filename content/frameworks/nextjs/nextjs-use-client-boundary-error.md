---
title: "[Solution] Next.js use Client Boundary Error"
description: "Client boundary not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Client boundary not working.

## Common Causes

Directive misplaced.

## How to Fix

Put at top of file.

## Example

```jsx
'use client';
import { useState } from 'react';
```
