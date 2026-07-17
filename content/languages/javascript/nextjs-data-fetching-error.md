---
title: "[Solution] Next.js: getServerSideProps Error Fix"
description: "Fix Next.js data fetching errors in getServerSideProps and getStaticProps. Handle fetch failures, serialization issues, and redirect loops."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Next.js: getServerSideProps Error

This error occurs when data fetching fails inside `getServerSideProps` or `getStaticProps` in the Pages Router. If the function throws or returns an invalid shape, the page cannot render.

## What This Error Means

Common error messages:

- `Error occurred prerendering page "/dashboard"`
- `getServerSideProps failed for page "/users". Error: fetch failed`
- `A component suspended while responding to synchronous input`
- `Error: Props must be serializable (no Date, Map, or Set objects)`

`getServerSideProps` runs on every request on the server. `getStaticProps` runs at build time (or revalidation time with ISR). Neither has access to the browser.

## Common Causes

```javascript
// Cause 1: Unhandled fetch error
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data'); // throws on failure
  const data = await res.json();
  return { props: { data } };
}

// Cause 2: Returning non-serializable data
export async function getServerSideProps() {
  return {
    props: {
      date: new Date(), // cannot serialize
      data: await getDatabaseRecord(),
    },
  };
}

// Cause 3: Missing return value
export async function getServerSideProps() {
  // forgot to return
}

// Cause 4: Redirect loop
export async function getServerSideProps(ctx) {
  if (!ctx.req.cookies.auth) {
    return { redirect: { destination: '/login', permanent: false } };
  }
  // login page also calls getServerSideProps and redirects...
}
```

## How to Fix

### Fix 1: Always handle fetch errors

```javascript
export async function getServerSideProps() {
  try {
    const res = await fetch('https://api.example.com/data');
    if (!res.ok) {
      return { notFound: true };
    }
    const data = await res.json();
    return { props: { data } };
  } catch (error) {
    return { props: { data: null, error: error.message } };
  }
}
```

### Fix 2: Serialize non-JSON-safe values

```javascript
export async function getServerSideProps() {
  const record = await db.query('SELECT * FROM posts');
  return {
    props: {
      posts: JSON.parse(JSON.stringify(record.rows)),
      timestamp: new Date().toISOString(), // string, not Date
    },
  };
}
```

### Fix 3: Return an empty object as fallback

```javascript
export async function getServerSideProps() {
  return {
    props: {
      data: [],
      timestamp: new Date().toISOString(),
    },
  };
}
```

### Fix 4: Add auth check to prevent redirect loops

```javascript
export async function getServerSideProps(ctx) {
  const token = ctx.req.cookies.auth;

  if (!token && ctx.resolvedUrl !== '/login') {
    return {
      redirect: {
        destination: '/login',
        permanent: false,
      },
    };
  }

  if (!token && ctx.resolvedUrl === '/login') {
    return { props: {} }; // don't redirect from login page
  }

  return { props: { user: await getUser(token) } };
}
```

## Examples

```bash
Error occurred prerendering page "/users".
Error: getServerSideProps failed for page "/users". Error: connect ECONNREFUSED 127.0.0.1:5432
```

```javascript
// Fix: wrap database call with retry logic
async function getUserWithRetry(token, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await getUser(token);
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 100 * (i + 1)));
    }
  }
}
```

## Related Errors

- [Next.js Build Error]({{< relref "/languages/javascript/nextjs-build-error" >}}) — build failed
- [Fetch Network Error]({{< relref "/languages/javascript/fetch-network-error" >}}) — fetch failed
- [Axios Error]({{< relref "/languages/javascript/axios-error" >}}) — HTTP request failed
