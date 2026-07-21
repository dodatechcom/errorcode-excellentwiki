---
title: "[Solution] React Server Side Props Error"
description: "getServerSideProps failing."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

getServerSideProps failing.

## Common Causes

Wrong return.

## How to Fix

Return props.

## Example

```javascript
export async function getServerSideProps() {
  return { props: { data: await getData() } };
}
```
