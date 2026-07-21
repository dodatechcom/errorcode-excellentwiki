---
title: "[Solution] React Portal Target Not Found"
description: "Error when createPortal cannot find target DOM node."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when createPortal cannot find target DOM node.

## Common Causes

Target container does not exist.

## How to Fix

Ensure target exists before creating portal.

## Example

```javascript
const t = document.getElementById('modal-root');
if (t) ReactDOM.createPortal(<Modal />, t);
```
