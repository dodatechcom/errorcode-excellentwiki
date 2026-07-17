---
title: "getServerSideProps Error in Next.js"
description: "Next.js throws an error when getServerSideProps fails during server-side rendering"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `getServerSideProps` error occurs when the server-side data fetching function throws an exception during server-side rendering. This prevents the page from rendering and typically shows an error message in the browser.

## Common Causes

- Database connection failure during SSR
- API call timeout or failure
- Missing environment variables
- Thrown exceptions not caught
- Props returned without required fields

## How to Fix

Handle errors within `getServerSideProps`:

```tsx
import { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async (context) => {
  try {
    const user = await fetchUser(context.params?.id as string);
    if (!user) {
      return { notFound: true };
    }
    return { props: { user } };
  } catch (error) {
    console.error('SSR Error:', error);
    return { props: { error: 'Failed to load user' } };
  }
};
```

Use proper error pages:

```tsx
export const getServerSideProps: GetServerSideProps = async () => {
  try {
    const data = await fetchData();
    return { props: { data } };
  } catch (error) {
    return { redirect: { destination: '/error', permanent: false } };
  }
};
```

Validate environment variables:

```tsx
export const getServerSideProps: GetServerSideProps = async () => {
  if (!process.env.DATABASE_URL) {
    throw new Error('DATABASE_URL is not configured');
  }
  const data = await fetchFromDatabase();
  return { props: { data } };
};
```

## Examples

```tsx
export const getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
};
```

```text
Error: getServerSideProps failed for /dashboard
Failed to fetch data from API
```

## Related Errors

- [Server component error]({{< relref "/frameworks/nextjs/nextjs-server-component-error" >}})
- [API route error]({{< relref "/frameworks/nextjs/nextjs-api-route-error" >}})
