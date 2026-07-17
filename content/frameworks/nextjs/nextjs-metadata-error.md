---
title: "Metadata API Error in Next.js"
description: "Next.js Metadata API errors occur when metadata configuration is invalid or conflicts exist"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["metadata", "seo", "head", "title", "nextjs"]
weight: 5
---

## What This Error Means

Metadata API errors occur when the `metadata` export or `generateMetadata` function in pages produces invalid metadata configurations. These errors appear during build or rendering when metadata cannot be properly applied.

## Common Causes

- Duplicate metadata keys in same route
- Invalid `openGraph` or `twitter` configuration
- `generateMetadata` returns invalid values
- Missing required fields in metadata objects
- Conflicting metadata between layout and page

## How to Fix

Define metadata correctly:

```tsx
// app/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My App',
  description: 'A Next.js application',
  openGraph: {
    title: 'My App',
    description: 'A Next.js application',
    url: 'https://myapp.com',
    siteName: 'My App',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'My App',
    description: 'A Next.js application',
  },
};
```

Use `generateMetadata` for dynamic metadata:

```tsx
import { Metadata } from 'next';

type Props = {
  params: { id: string };
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const post = await getPost(params.id);

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
    },
  };
}
```

Override parent layout metadata:

```tsx
// app/dashboard/page.tsx
export const metadata: Metadata = {
  title: 'Dashboard - My App', // Overrides root layout title
  description: 'Dashboard page',
};
```

Handle metadata with `generateStaticParams`:

```tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({ id: post.id }));
}

export async function generateMetadata({ params }): Promise<Metadata> {
  const post = await getPost(params.id);
  return { title: post.title };
}
```

## Examples

```tsx
export const metadata: Metadata = {
  title: 'Page',
  openGraph: {
    title: 'Page',
    // Missing required 'description'
  },
};
```

```text
Error: Invalid metadata configuration. "openGraph" is missing required field "description".
```

## Related Errors

- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
