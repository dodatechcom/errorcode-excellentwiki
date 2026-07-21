---
title: "[Solution] Express Worker Exit Error"
description: "Worker exiting unexpectedly."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Worker exiting unexpectedly.

## Common Causes

Error in worker.

## How to Fix

Handle errors.

## Example

```javascript
cluster.on('exit', (w) => console.log('Worker died'));
```
