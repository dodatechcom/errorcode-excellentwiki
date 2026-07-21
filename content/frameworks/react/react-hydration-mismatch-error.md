---
title: "[Solution] React Hydration Mismatch Error"
description: "Server HTML doesn't match client."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Server HTML doesn't match client.

## Common Causes

Different content rendered.

## How to Fix

Ensure consistent rendering.

## Example

```javascript
const [m, setM] = useState(false);
useEffect(() => setM(true), []);
return m ? <BC /> : <SF />;
```
