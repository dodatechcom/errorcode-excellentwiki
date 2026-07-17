---
title: "[Solution] React Warning: Can't perform state update on unmounted component"
description: "Fix React state update warning on unmounted components. Clean up async operations, use AbortController, and manage component lifecycle."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React Warning: Can't perform state update on unmounted component

This warning occurs when you try to update the state of a component that has already been unmounted. It typically happens with async operations that complete after the component is gone.

## What This Error Means

Common error messages:

- `Warning: Can't perform a React state update on an unmounted component.`
- `Warning: setState(...): Can only update a mounted or mounting component.`

React 18+ removed this warning, but the underlying issue still causes memory leaks and wasted computation.

## Common Causes

```jsx
// Cause 1: Fetching data without cleanup
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data)); // component may be unmounted
  }, [userId]);
}

// Cause 2: setTimeout without cleanup
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    setTimeout(() => {
      setCount(1); // if component unmounted before timeout
    }, 5000);
  }, []);
}

// Cause 3: Event listener not removed
function ScrollTracker() {
  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    // missing cleanup
  }, []);
}
```

## How to Fix

### Fix 1: Use cleanup function in useEffect

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    let cancelled = false;

    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        if (!cancelled) setUser(data);
      });

    return () => { cancelled = true; };
  }, [userId]);
}
```

### Fix 2: Use AbortController

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setUser(data))
      .catch(err => {
        if (err.name !== 'AbortError') throw err;
      });

    return () => controller.abort();
  }, [userId]);
}
```

### Fix 3: Clean up timers and listeners

```jsx
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => setCount(1), 5000);
    return () => clearTimeout(timer);
  }, []);
}

function ScrollTracker() {
  useEffect(() => {
    const handler = () => console.log(window.scrollY);
    window.addEventListener('scroll', handler);
    return () => window.removeEventListener('scroll', handler);
  }, []);
}
```

### Fix 4: Use ignore flag pattern

```jsx
function DataFetcher({ url }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let ignore = false;

    async function fetchData() {
      const res = await fetch(url);
      const json = await res.json();
      if (!ignore) setData(json);
    }

    fetchData();
    return () => { ignore = true; };
  }, [url]);

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}
```

## Examples

```jsx
// This triggers the warning
function SearchResults({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch(`/api/search?q=${query}`)
      .then(res => res.json())
      .then(data => setResults(data)); // query changed before fetch completes
  }, [query]);
}

// Fix
function SearchResults({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    let cancelled = false;
    fetch(`/api/search?q=${query}`)
      .then(res => res.json())
      .then(data => {
        if (!cancelled) setResults(data);
      });
    return () => { cancelled = true; };
  }, [query]);
}
```

## Related Errors

- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundary
- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation aborted
- [React Key Prop]({{< relref "/languages/javascript/react-key-prop" >}}) — unique key warning
