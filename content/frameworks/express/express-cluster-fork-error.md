---
title: "[Solution] Express Cluster Fork Error"
description: "Cluster fork failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cluster fork failing.

## Common Causes

Wrong call.

## How to Fix

Use cluster.fork().

## Example

```javascript
if (cluster.isPrimary) { cluster.fork(); }
```
