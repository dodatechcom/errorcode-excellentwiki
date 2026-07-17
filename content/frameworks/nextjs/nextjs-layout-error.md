---
title: "Layout Error in Next.js"
description: "Next.js layout errors occur when layout components fail to render or wrap child routes correctly"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Layout errors in Next.js occur when layout components fail to render, do not properly wrap child components, or contain rendering exceptions. Layouts are persistent across navigations and must render `{children}` to display nested routes.

## Common Causes

- Layout does not render `{children}` prop
- Layout throws an exception during rendering
- Missing root `layout.tsx` in app directory
- Layout uses hooks without `'use client'` directive
- Infinite layout nesting or circular dependencies

## How to Fix

Create a proper root layout:

```tsx
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <nav>Navigation</nav>
        {children}
        <footer>Footer</footer>
      </body>
    </html>
  );
}
```

Use nested layouts:

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="dashboard">
      <aside>Dashboard Sidebar</aside>
      <main>{children}</main>
    </div>
  );
}
```

Handle layout errors with error boundaries:

```tsx
// app/dashboard/layout.tsx
'use client';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <ErrorBoundary>
        {children}
      </ErrorBoundary>
    </div>
  );
}
```

Pass data to layouts via props from parent layouts:

```tsx
// app/dashboard/layout.tsx
export default async function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const user = await getUser();
  return (
    <div>
      <header>Welcome, {user.name}</header>
      {children}
    </div>
  );
}
```

## Examples

```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {/* Missing: {children} */}
      </body>
    </html>
  );
}
```

```text
Error: The default export is not a React Component in "app/layout.tsx"
```

## Related Errors

- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
- [Not found error]({{< relref "/frameworks/nextjs/nextjs-not-found-error" >}})
