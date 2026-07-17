---
title: "App Router Error in Next.js"
description: "Next.js App Router raises errors when layouts, pages, or loading states are misconfigured"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

App Router errors occur when the file-based routing system encounters misconfigured layouts, missing required files, or invalid route structures. These errors typically appear during development or build time.

## Common Causes

- Missing `page.tsx` or `layout.tsx` in app directory
- Invalid use of client/server components
- Nested layouts not properly structured
- Missing `loading.tsx` or `error.tsx` for routes
- Incorrect dynamic route parameter handling

## How to Fix

Set up proper app directory structure:

```
app/
  layout.tsx        # Root layout (required)
  page.tsx          # Home page
  dashboard/
    layout.tsx      # Dashboard layout
    page.tsx        # Dashboard page
    loading.tsx     # Dashboard loading state
    error.tsx       # Dashboard error boundary
```

Create a root layout:

```tsx
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

Handle dynamic routes:

```tsx
// app/posts/[id]/page.tsx
export default function PostPage({ params }: { params: { id: string } }) {
  return <div>Post {params.id}</div>;
}
```

Use error boundaries:

```tsx
// app/dashboard/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

## Examples

```
app/
  layout.tsx
  page.tsx
  about/
    # Missing: page.tsx in about directory
```

```text
Error: The default export is not a React component in "/about/page.tsx"
```

## Related Errors

- [Layout error]({{< relref "/frameworks/nextjs/nextjs-layout-error" >}})
- [Server component error]({{< relref "/frameworks/nextjs/nextjs-server-component-error" >}})
