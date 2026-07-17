---
title: "[Solution] Next.js: App Router Error Fix"
description: "Fix Next.js App Router errors including Server Component issues, invalid hooks usage, and route handler failures."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Next.js: App Router Error

This error covers a range of failures specific to the Next.js App Router (app/ directory). It includes invalid hooks usage in Server Components, missing error/loading boundaries, and route handler failures.

## What This Error Means

Common error messages:

- `Error: useCallback is not a function in a Client Component`
- `Error: useState only works in Client Components`
- `Could not find the module "..." in the React Server Component runtime`
- `Uncaught Error:NEXT_REDIRECT`
- `Error rendering layout: ...`

Server Components run only on the server and cannot use React hooks that rely on client state. Client Components need the `'use client'` directive.

## Common Causes

```javascript
// Cause 1: Using hooks in a Server Component
// app/dashboard/page.js (Server Component by default)
import { useState } from 'react';

export default function Dashboard() {
  const [count, setCount] = useState(0); // ERROR
  return <button>{count}</button>;
}

// Cause 2: Missing 'use client' in interactive component
export default function Counter() {
  const [count, setCount] = useState(0); // ERROR without directive
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}

// Cause 3: Accessing request-only APIs in layouts
// app/layout.js
export default function RootLayout({ children }) {
  const cookies = cookies(); // ERROR in layout that may be cached
  return <html><body>{children}</body></html>;
}

// Cause 4: Route handler returning invalid response
// app/api/users/route.js
export async function GET() {
  return { users: [] }; // must use NextResponse
}
```

## How to Fix

### Fix 1: Add 'use client' directive

```jsx
'use client';
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

### Fix 2: Use NextResponse in route handlers

```javascript
// app/api/users/route.js
import { NextResponse } from 'next/server';

export async function GET(request) {
  const users = await fetchUsers();
  return NextResponse.json({ users });
}

export async function POST(request) {
  const body = await request.json();
  const user = await createUser(body);
  return NextResponse.json({ user }, { status: 201 });
}
```

### Fix 3: Access cookies/headers only in Server Components or Route Handlers

```javascript
// app/dashboard/page.js (Server Component)
import { cookies } from 'next/headers';

export default async function Dashboard() {
  const cookieStore = await cookies();
  const token = cookieStore.get('auth-token');
  return <div>Welcome {token?.value}</div>;
}
```

### Fix 4: Use error.js and loading.js boundaries

```javascript
// app/dashboard/error.js
'use client';

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}

// app/dashboard/loading.js
export default function Loading() {
  return <div>Loading dashboard...</div>;
}
```

## Examples

```
Error: useCallback is not a function in a Client Component.
Client components must have a 'use client' directive at the top
of the file.
```

```jsx
// Fix: move the 'use client' directive to the top
'use client';
import { useCallback } from 'react';

export function SearchInput({ onSearch }) {
  const handleSearch = useCallback((e) => {
    onSearch(e.target.value);
  }, [onSearch]);
  return <input onChange={handleSearch} />;
}
```

## Related Errors

- [Next.js Build Error V2]({{< relref "/languages/javascript/nextjs-build-error-v2" >}}) — build failed
- [Next.js Hydration Error V2]({{< relref "/languages/javascript/nextjs-hydration-error-v2" >}}) — hydration mismatch
- [React Error Boundary V2]({{< relref "/languages/javascript/react-error-boundary-v2" >}}) — error boundary caught error
