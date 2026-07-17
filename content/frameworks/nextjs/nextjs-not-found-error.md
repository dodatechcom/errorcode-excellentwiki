---
title: "Next.js Not Found Error"
description: "Next.js throws not found errors when routes are undefined or pages explicitly return notFound"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The Next.js not found error occurs when a user navigates to a route that does not exist, or when a page explicitly returns `{ notFound: true }` from `getServerSideProps` or `generateStaticParams`.

## Common Causes

- User navigated to a non-existent route
- Dynamic route parameter does not match any data
- `getServerSideProps` returned `{ notFound: true }`
- Missing `not-found.tsx` for custom 404 page
- Incorrect rewrites or redirects in config

## How to Fix

Create a custom not found page:

```tsx
// app/not-found.tsx
import Link from 'next/link';

export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>The requested page could not be found.</p>
      <Link href="/">Go back home</Link>
    </div>
  );
}
```

Handle not found in `getServerSideProps`:

```tsx
import { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async ({ params }) => {
  const post = await getPost(params?.id as string);

  if (!post) {
    return { notFound: true };
  }

  return { props: { post } };
};
```

Use `notFound()` in App Router:

```tsx
import { notFound } from 'next/navigation';

export default async function PostPage({ params }) {
  const post = await getPost(params.id);

  if (!post) {
    notFound();
  }

  return <article>{post.content}</article>;
}
```

Generate static params with fallback:

```tsx
// app/posts/[id]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({ id: post.id }));
}

export const dynamicParams = true; // Allow dynamic routes not in generateStaticParams
```

## Examples

```tsx
export const getServerSideProps: GetServerSideProps = async ({ params }) => {
  const user = await getUser(params?.id as string);
  return { props: { user } }; // No check for null user
};
```

```text
404: This page could not be found
```

## Related Errors

- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
- [Layout error]({{< relref "/frameworks/nextjs/nextjs-layout-error" >}})
