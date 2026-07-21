---
title: "[Solution] React Server Component Error"
description: "Server components not configured."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Server components not configured.

## Common Causes

Using browser APIs on server.

## How to Fix

No hooks in server components.

## Example

```jsx
async function SC() {
  const d = await fetchData();
  return <div>{d.title}</div>;
}
```
