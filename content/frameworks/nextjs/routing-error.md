---
title: "Routing error"
description: "Next.js encounters an error during client-side or file-system based routing"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Next.js encounters an issue with its file-system based routing, such as conflicting routes, invalid dynamic route parameters, or incorrect `useRouter` usage.

## Common Causes

- Conflicting routes (e.g. `pages/user/[id].js` and `pages/user.js` coexisting)
- Missing `[param]` file for a dynamic route
- Using `useRouter` outside of a Next.js page component
- Invalid characters in dynamic route parameters

## How to Fix

1. Ensure no conflicting route files exist:

```
pages/
  user/
    [id].js    # /user/:id (dynamic)
    index.js   # /user (list)
  user.js       # CONFLICT: remove this if using user/ folder
```

2. Validate route params in dynamic routes:

```typescript
// pages/post/[slug].tsx
export async function getStaticProps({ params }) {
  const post = await getPost(params.slug);
  if (!post) return { notFound: true };
  return { props: { post } };
}
```

3. Use `useRouter` correctly:

```tsx
import { useRouter } from 'next/router';

export default function Page() {
  const router = useRouter();
  const { id } = router.query;
  return <p>Post: {id}</p>;
}
```

## Examples

```
pages/
  blog/[slug].js
  blog/index.js
  blog.js         # This conflicts with blog/ directory
```

```text
Error: You cannot have both a pages/blog.js file and a pages/blog/ directory.
```

## Related Errors

- [Middleware error]({{< relref "/frameworks/nextjs/middleware-error2" >}})
