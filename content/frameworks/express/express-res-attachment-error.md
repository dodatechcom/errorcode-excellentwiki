---
title: "[Solution] Express res.attachment Error"
description: "Attachment not setting."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Attachment not setting.

## Common Causes

Wrong usage.

## How to Fix

Use res.attachment.

## Example

```javascript
res.attachment('/files/doc.pdf');
```
