---
title: "[Solution] React Server Component Error Fix"
description: "Fix React Server Component errors in Next.js App Router. Handle server/client component boundaries and async server components."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React Server Component Error

This error occurs when a React Server Component uses client-only features or crosses the server/client boundary incorrectly. It is common in Next.js App Router.

## What This Error Means

Common error messages:

- `Error: ReactClientElementRef: ref is not a React ref`
- `TypeError: useState is not a function`
- `Server Components cannot be directly rendered as Client Components`

Server Components run only on the server and cannot use hooks like `useState`, `useEffect`, or browser APIs.

## Common Causes

```jsx
// Cause 1: Using useState in server component
// app/page.js (Server Component by default)
import { useState } from 'react';

export default function Page() {
  const [count, setCount] = useState(0); // Error
}

// Cause 2: Using useEffect in server component
export default function Page() {
  useEffect(() => {}, []); // Error
}

// Cause 3: Accessing window/document
export default function Page() {
  const width = window.innerWidth; // Error
}

// Cause 4: Importing client-only libraries
import Chart from 'chart.js'; // requires browser APIs
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

### Fix 2: Pass data from server to client component

```jsx
// app/dashboard/page.js (Server)
import { InteractiveChart } from './InteractiveChart'; // Client

async function getChartData() {
  const res = await fetch('http://api.example.com/chart');
  return res.json();
}

export default async function Dashboard() {
  const data = await getChartData(); // OK on server
  return <InteractiveChart data={data} />; // passes to client
}
```

```jsx
// app/dashboard/InteractiveChart.js (Client)
'use client';
import { useState } from 'react';

export function InteractiveChart({ data }) {
  const [selected, setSelected] = useState(null);
  return (
    <div>
      <select onChange={e => setSelected(e.target.value)}>
        {data.map(d => <option key={d.id}>{d.label}</option>)}
      </select>
    </div>
  );
}
```

### Fix 3: Use async server components

```jsx
// app/users/page.js
async function getUsers() {
  const res = await fetch('http://api.example.com/users');
  return res.json();
}

export default async function Users() {
  const users = await getUsers();
  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

### Fix 4: Dynamic import for client-only code

```jsx
import dynamic from 'next/dynamic';

const ClientChart = dynamic(() => import('./ClientChart'), { ssr: false });

export default function Page() {
  return <ClientChart />;
}
```

## Examples

```jsx
// This triggers error
// app/page.js
export default function Page() {
  const [input, setInput] = useState(''); // Error: useState in server component
  return <input value={input} onChange={e => setInput(e.target.value)} />;
}

// Fix: split into server and client
// app/page.js
import { SearchInput } from './SearchInput'; // client component

export default function Page() {
  return <SearchInput />;
}

// app/SearchInput.js
'use client';
import { useState } from 'react';

export function SearchInput() {
  const [input, setInput] = useState('');
  return <input value={input} onChange={e => setInput(e.target.value)} />;
}
```

## Related Errors

- [Next.js App Router]({{< relref "/languages/javascript/nextjs-app-router" >}}) — App Router error
- [Next.js Hydration]({{< relref "/languages/javascript/nextjs-hydration" >}}) — hydration mismatch
- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundary
