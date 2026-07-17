---
title: "State update error"
description: "React Native throws a warning or error when updating state on an unmounted component"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when React Native attempts to update the state of a component that has already been unmounted, typically during async operations. This was a common source of memory leaks and warnings.

## Common Causes

- Async operation (fetch, setTimeout) completes after component unmounts
- Event listener not cleaned up in `useEffect` return
- Navigating away from a screen while a request is in progress
- Not using an `isMounted` check or abort controller

## How to Fix

1. Use cleanup functions in `useEffect`:

```jsx
import { useState, useEffect } from 'react';
import { ActivityIndicator, View } from 'react-native';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    fetchUsers().then(data => {
      if (!cancelled) {
        setUsers(data);
        setLoading(false);
      }
    });

    return () => { cancelled = true; };
  }, []);

  if (loading) return <ActivityIndicator />;
  return <UserListItems users={users} />;
}
```

2. Use `AbortController` for fetch requests:

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('https://api.example.com/users', { signal: controller.signal })
    .then(res => res.json())
    .then(data => setUsers(data))
    .catch(err => {
      if (err.name !== 'AbortError') throw err;
    });

  return () => controller.abort();
}, []);
```

3. Clean up subscriptions and listeners:

```jsx
useEffect(() => {
  const subscription = DeviceEventEmitter.addListener('event', handler);
  return () => subscription.remove();
}, []);
```

## Examples

```jsx
// Component unmounts before async completes
function Profile({ userId }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(res => setData(res)); // Warning if unmounted
  }, [userId]);

  return data ? <Text>{data.name}</Text> : <ActivityIndicator />;
}
```

```text
Warning: Can't perform a React state update on an unmounted component.
```

## Related Errors

- [Native module bridge error]({{< relref "/frameworks/react-native/bridge-error" >}})
