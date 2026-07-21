---
title: "[Solution] React Script Strategy Error"
description: "Script not loading correctly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Script not loading correctly.

## Common Causes

Wrong strategy.

## How to Fix

Use correct strategy.

## Example

```javascript
import Script from 'next/script';
<Script src="/analytics.js" strategy="afterInteractive" />
```
