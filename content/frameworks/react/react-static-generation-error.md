---
title: "[Solution] React Static Generation Error"
description: "Static generation failing."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Static generation failing.

## Common Causes

Wrong function usage.

## How to Fix

Use getStaticProps.

## Example

```javascript
export async function getStaticProps() {
  return { props: { data: 'hello' } };
}
```
