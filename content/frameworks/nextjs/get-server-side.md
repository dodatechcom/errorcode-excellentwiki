---
title: "getServerSideProps error"
description: "Next.js raises an error when getServerSideProps throws or returns an invalid result"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when `getServerSideProps` fails during server-side rendering. The function may throw an exception, return an invalid object, or reference an undefined variable.

## Common Causes

- `getServerSideProps` throws an exception (e.g. database query failure)
- Missing or incorrect `props` key in the returned object
- Using browser-only APIs (`window`, `document`) in `getServerSideProps`
- Accessing `req` or `res` properties that are undefined

## How to Fix

1. Wrap server-side logic in try-catch:

```typescript
export async function getServerSideProps(context) {
  try {
    const data = await fetchData();
    return { props: { data } };
  } catch (error) {
    return { props: { error: error.message } };
  }
}
```

2. Return the correct shape with `props` or `redirect`:

```typescript
export async function getServerSideProps(context) {
  const { id } = context.params;

  if (!id) {
    return { redirect: { destination: '/', permanent: false } };
  }

  const post = await getPost(id);
  if (!post) {
    return { notFound: true };
  }

  return { props: { post } };
}
```

3. Never use browser APIs in `getServerSideProps`:

```typescript
// WRONG -- window is not defined on server
export async function getServerSideProps() {
  const width = window.innerWidth; // Error
  return { props: { width } };
}

// CORRECT -- use context or query params instead
export async function getServerSideProps(context) {
  const width = context.req.headers['viewport-width'] || 1024;
  return { props: { width } };
}
```

## Examples

```typescript
export async function getServerSideProps() {
  const data = await fetch('https://api.invalid-url.com/data');
  const json = await data.json(); // fetch throws
  return { props: { data: json } };
}
```

```text
Error: getServerSideProps failed
Page could not render: fetch failed
```

## Related Errors

- [API route error]({{< relref "/frameworks/nextjs/api-error" >}})
