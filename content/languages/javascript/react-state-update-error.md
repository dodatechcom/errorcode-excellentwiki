---
title: "[Solution] React: State Update on Unmounted Component Fix"
description: "Fix React warnings about updating state on an unmounted component. Handle async cleanup with AbortController and useEffect cleanup functions."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React: State Update on Unmounted Component

This warning occurs when a component sets state after it has been removed from the DOM. React 18+ shows this as a console warning; earlier versions showed a full warning. It indicates a memory leak and potentially stale UI updates.

## What This Error Means

Common error messages:

- `Can't perform a React state update on an unmounted component. This is a no-op, but it indicates a memory leak in your application.`
- `Warning: Can't call setState (or forceUpdate) on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in the useEffect cleanup function.`

This happens when an async operation (fetch, setTimeout, WebSocket) resolves after the component unmounts and calls `setState`.

## Common Causes

```javascript
// Cause 1: Fetch resolves after unmount
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data)); // ERROR if component unmounted
  }, [userId]);

  return <div>{user?.name}</div>;
}

// Cause 2: setTimeout without cleanup
useEffect(() => {
  const timer = setTimeout(() => {
    setExpanded(true); // may fire after unmount
  }, 3000);
  // missing cleanup
}, []);

// Cause 3: WebSocket not closed on unmount
useEffect(() => {
  const ws = new WebSocket(url);
  ws.onmessage = (e) => {
    setMessages(prev => [...prev, e.data]); // may fire after unmount
  };
  // missing cleanup
}, []);
```

## How to Fix

### Fix 1: Use AbortController for fetch cleanup

```javascript
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

  return <div>{user?.name}</div>;
}
```

### Fix 2: Add cleanup for setTimeout/setInterval

```javascript
useEffect(() => {
  const timer = setTimeout(() => {
    setExpanded(true);
  }, 3000);

  return () => clearTimeout(timer);
}, []);
```

### Fix 3: Close WebSocket in cleanup

```javascript
useEffect(() => {
  const ws = new WebSocket(url);
  ws.onmessage = (e) => {
    setMessages(prev => [...prev, e.data]);
  };

  return () => ws.close();
}, [url]);
```

### Fix 4: Use a mounted flag for non-cancellable async

```javascript
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    let mounted = true;

    async function load() {
      const data = await fetchUser(userId);
      if (mounted) setUser(data);
    }

    load();
    return () => { mounted = false; };
  }, [userId]);

  return <div>{user?.name}</div>;
}
```

## Examples

```
Warning: Can't perform a React state update on an unmounted component.
This is a no-op, but it indicates a memory leak in your application.
To fix, cancel all subscriptions and asynchronous tasks in a useEffect cleanup function.
```

```javascript
// Fix: combine AbortController with cleanup
useEffect(() => {
  const controller = new AbortController();

  const loadData = async () => {
    try {
      const res = await fetch(url, { signal: controller.signal });
      const data = await res.json();
      setData(data);
    } catch (err) {
      if (err.name !== 'AbortError') {
        setError(err);
      }
    }
  };

  loadData();
  return () => controller.abort();
}, [url]);
```

## Related Errors

- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — state update issues
- [React Error Boundary V2]({{< relref "/languages/javascript/react-error-boundary-v2" >}}) — error boundary caught error
- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation aborted
