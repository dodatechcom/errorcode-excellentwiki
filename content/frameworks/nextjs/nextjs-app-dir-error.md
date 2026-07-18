---
title: "[Solution] Next.js App Router Directory Error — How to Fix"
description: "Fix Next.js App Router errors. Resolve directory structure, file conventions, and App Router migration issues."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js App Router directory error occurs when the directory structure doesn't follow App Router conventions, when files are placed in wrong locations, or when the migration from Pages Router is incomplete.

## Why It Happens

The App Router uses a file-system based routing convention with specific file names (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`). Errors occur when `page.tsx` files are missing in route segments, when `layout.tsx` is placed incorrectly, when `app/` and `pages/` directories coexist, when `not-found.tsx` is missing, or when route groups are misconfigured.

## Common Error Messages

```
Error: Page / not found. Make sure the page has a default export.
```

```
Error: You cannot use both app and pages directories
```

```
Error: Layout is missing children prop
```

```
Error: Cannot use both 'app/layout.tsx' and 'pages/_app.tsx'
```

## How to Fix It

### 1. Follow App Router File Conventions

Use the correct file structure:

```
app/
├── layout.tsx          # Root layout (required)
├── page.tsx            # Home page
├── loading.tsx         # Loading UI for root
├── error.tsx           # Error boundary for root
├── not-found.tsx       # 404 page
├── about/
│   └── page.tsx        # /about route
├── blog/
│   ├── layout.tsx      # Blog layout
│   ├── page.tsx        # /blog route
│   └── [slug]/
│       └── page.tsx    # /blog/:slug route
└── dashboard/
    ├── layout.tsx      # Dashboard layout
    ├── page.tsx        # /dashboard route
    └── settings/
        └── page.tsx    # /dashboard/settings route
```

### 2. Avoid Mixing App and Pages Router

Choose one routing system:

```bash
# Wrong: both directories exist
app/
pages/

# Correct: only use one
app/    # App Router
# or
pages/  # Pages Router (legacy)
```

### 3. Migrate from Pages Router

Key differences to handle during migration:

```typescript
// Pages Router (pages/)
export default function Home() {
    return <div>Home</div>;
}

// App Router (app/)
export default function Home() {
    return <div>Home</div>;
}

// Pages Router: getServerSideProps
export async function getServerSideProps() {
    const data = await fetchData();
    return { props: { data } };
}

// App Router: async component
export default async function Page() {
    const data = await fetchData();
    return <div>{data.title}</div>;
}
```

### 4. Use Route Groups for Organization

Organize routes without affecting the URL:

```
app/
├── (marketing)/
│   ├── layout.tsx
│   ├── page.tsx        # /
│   └── about/
│       └── page.tsx    # /about
├── (dashboard)/
│   ├── layout.tsx
│   ├── dashboard/
│   │   └── page.tsx    # /dashboard
│   └── settings/
│       └── page.tsx    # /settings
```

## Common Scenarios

**Scenario 1: 404 for existing page.**
Ensure the file is named `page.tsx` (not `Page.tsx`, `index.tsx`, or `page.js`).

**Scenario 2: Layout doesn't update between pages.**
Layouts persist for their segment. If the layout should change, move it to a different directory level.

**Scenario 3: CSS styles don't apply to nested routes.**
Global CSS must be imported in `layout.tsx`, not in `page.tsx`. Component-level CSS works in either.

## Prevent It

1. **Use a consistent naming convention** — always `page.tsx`, `layout.tsx`, `loading.tsx`.

2. **Don't mix `app/` and `pages/` directories.** Choose one routing approach.

3. **Test routes with `next build`** to catch structural issues before deployment.
