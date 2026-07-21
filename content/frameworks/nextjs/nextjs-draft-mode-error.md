---
title: "[Solution] Next.js Draft Mode Error"
description: "Draft mode not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Draft mode not working.

## Common Causes

Not enabled.

## How to Fix

Enable draft.

## Example

```javascript
import { draftMode } from 'next/headers';
const { isEnabled } = draftMode();
```
