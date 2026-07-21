---
title: "[Solution] React ReactDOM.render Deprecated"
description: "Using deprecated ReactDOM.render."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Using deprecated ReactDOM.render.

## Common Causes

Legacy API.

## How to Fix

Migrate to createRoot.

## Example

```javascript
import { createRoot } from 'react-dom/client';
createRoot(document.getElementById('root')).render(<App />);
```
