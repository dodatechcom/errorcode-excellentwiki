---
title: "Client Component Error in Next.js"
description: "Next.js client component errors occur when client-side rendering fails due to missing directives or improper imports"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["client-component", "use-client", "browser", "interactive", "nextjs"]
weight: 5
---

## What This Error Means

Client component errors occur when a component marked with `'use client'` encounters issues with hooks, event handlers, or browser APIs. These errors also happen when a component needs to be interactive but lacks the client directive.

## Common Causes

- Missing `'use client'` directive for interactive components
- Using hooks without proper directive
- Browser APIs used without dynamic import
- State management issues in client components
- Event handlers in server components

## How to Fix

Add the `'use client'` directive:

```tsx
'use client';
import { useState } from 'react';

export default function InteractiveButton() {
  const [clicked, setClicked] = useState(false);

  return (
    <button onClick={() => setClicked(true)}>
      {clicked ? 'Clicked!' : 'Click me'}
    </button>
  );
}
```

Use dynamic imports for browser-only components:

```tsx
import dynamic from 'next/dynamic';

const MapComponent = dynamic(() => import('./MapComponent'), {
  ssr: false,
  loading: () => <p>Loading map...</p>,
});
```

Handle client-side data fetching:

```tsx
'use client';
import { useState, useEffect } from 'react';

export default function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(setUser);
  }, [userId]);

  if (!user) return <p>Loading...</p>;
  return <h1>{user.name}</h1>;
}
```

## Examples

```tsx
// Missing 'use client' - will error if component uses onClick
export default function Button() {
  return <button onClick={() => alert('clicked')}>Click</button>;
}
```

```text
Error: Event handlers cannot be passed to Client Component props.
```

## Related Errors

- [Server component error]({{< relref "/frameworks/nextjs/nextjs-server-component-error" >}})
- [Hydration error]({{< relref "/frameworks/nextjs/nextjs-hydration-error" >}})
