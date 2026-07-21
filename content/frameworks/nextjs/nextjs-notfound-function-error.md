---
title: "[Solution] Next.js notFound Function Error"
description: "notFound() not triggering."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

notFound() not triggering.

## Common Causes

Not imported.

## How to Fix

Import from next/navigation.

## Example

```javascript
import { notFound } from 'next/navigation';
if (!user) notFound();
```
