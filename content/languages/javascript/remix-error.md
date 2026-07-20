---
title: "[Solution] JavaScript Remix Runtime Error — How to Fix"
description: "Fix JavaScript Remix loader/action errors, data serialization failures, form handling issues, and server/client mismatch bugs."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 808
---

# JavaScript Remix Runtime Error

An `Error`, `TypeError`, or `LoaderError` occurs when Remix loaders or actions throw unhandled exceptions, returned data cannot be serialized, form data is improperly parsed, or server/client code is incorrectly shared.

## Why It Happens

Remix errors arise from loaders that do not return a `Response`, actions that throw instead of returning errors, Date/Map/Set objects in loader data (not serializable), missing `formData` parsing, and importing browser-only APIs in server code.

## Common Error Messages

- `Error: Loader for route 'routes/xxx' must return a Response`
- `TypeError: Do not know how to serialize a BigInt`
- `Error: formData.get is not a function`
- `Error: Cannot find module 'xxx' (server vs client mismatch)`
- `Error: useLoaderData must be used within a route`

## How to Fix It

### Fix 1: Loader must return Response

```typescript
// ❌ Wrong - returning raw object
// export const loader = async () => {
//   return { users: await db.getUsers() }
// }

// ✅ Correct - use json helper
import { json } from '@remix-run/node'

export const loader = async () => {
  const users = await db.getUsers()
  return json({ users })
}
```

### Fix 2: Handle form data in actions

```typescript
import { ActionFunctionArgs, json, redirect } from '@remix-run/node'

export const action = async ({ request }: ActionFunctionArgs) => {
  // ❌ Wrong - missing formData parsing
  // const name = request.body.name

  // ✅ Correct
  const formData = await request.formData()
  const name = formData.get('name')

  if (!name) {
    return json({ error: 'Name is required' }, { status: 400 })
  }

  return redirect('/success')
}
```

### Fix 3: Serialize only plain objects

```typescript
// ❌ Wrong - Date and Map are not serializable
// export const loader = async () => {
//   return json({ date: new Date(), map: new Map() })
// }

// ✅ Correct - convert to serializable formats
export const loader = async () => {
  const events = await db.getEvents()
  return json({
    date: new Date().toISOString(),
    items: events.map(e => ({ id: e.id, name: e.name }))
  })
}
```

### Fix 4: Client-only code in routes

```typescript
// ❌ Wrong - browser API in loader (server)
// export const loader = async () => {
//   const hash = window.location.hash
// }

// ✅ Correct - use useLocation in component, not loader
export default function Route() {
  const location = useLocation()
  const hash = location.hash
  // ...
}
```

## Examples

Action with validation errors:

```typescript
export const action = async ({ request }: ActionFunctionArgs) => {
  const formData = await request.formData()
  const email = formData.get('email')

  const errors: Record<string, string> = {}
  if (!email || !String(email).includes('@')) {
    errors.email = 'Valid email required'
  }

  if (Object.keys(errors).length > 0) {
    return json({ errors }, { status: 400 })
  }

  return redirect('/success')
}
```

## Related Errors

- [Nuxt Error](/languages/javascript/nuxt-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
- [JavaScript SSR Error](/languages/javascript/js-ssr-error)
