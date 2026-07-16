---
title: "[Solution] React State Update on Unmounted Component Warning Fix"
description: "Fix React 'Can't perform a React state update on an unmounted component' warning. Clean up async operations and use cancellation tokens."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["react", "state-update", "unmounted", "useEffect", "cleanup", "memory-leak"]
weight: 5
---

# React: Can't Perform a React State Update on an Unmounted Component

This warning occurs when a component unmounts (is removed from the DOM) but an asynchronous operation (API call, timer, subscription) still tries to call `setState` after the component is gone. While React 18 no longer prints this warning by default, it still represents a real bug — a wasted async operation and potential memory leak.

## Common Causes

- **Un-cancelled API calls** — `fetch` or `axios` returns after component unmounts
- **Missing cleanup in useEffect** — no return function to cancel subscriptions or timers
- **Promise resolved after unmount** — `.then()` handler runs after component is gone
- **Race condition with navigation** — user navigates away during a data fetch

## How to Fix

```jsx
// Cause 1: API call without cancellation
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data));  // Warning if component unmounts first
  }, [userId]);

  return user ? <div>{user.name}</div> : <p>Loading...</p>;
}

// Fix: use AbortController
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setUser(data))
      .catch(err => {
        if (err.name !== "AbortError") throw err;
      });

    return () => controller.abort();
  }, [userId]);

  return user ? <div>{user.name}</div> : <p>Loading...</p>;
}

// Cause 2: Missing cleanup for timer
function Clock() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    setInterval(() => {
      setTime(new Date());  // Warning if component unmounts
    }, 1000);
  }, []);

  return <p>{time.toLocaleTimeString()}</p>;
}

// Fix: clear interval in cleanup
function Clock() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const id = setInterval(() => {
      setTime(new Date());
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <p>{time.toLocaleTimeString()}</p>;
}
```

```jsx
// Cause 3: Subscription without cleanup
function ChatRoom({ roomId }) {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const socket = connect(roomId);
    socket.on("message", msg => setMessages(prev => [...prev, msg]));
  }, [roomId]);

  return <ul>{messages.map((m, i) => <li key={i}>{m}</li>)}</ul>;
}

// Fix: unsubscribe in cleanup
function ChatRoom({ roomId }) {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const socket = connect(roomId);
    socket.on("message", msg => setMessages(prev => [...prev, msg]));
    return () => socket.disconnect();
  }, [roomId]);

  return <ul>{messages.map((m, i) => <li key={i}>{m}</li>)}</ul>;
}
```

## Using a Mounted Flag Pattern

```jsx
function DataLoader({ url }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let isMounted = true;

    fetch(url)
      .then(res => res.json())
      .then(result => {
        if (isMounted) setData(result);
      });

    return () => { isMounted = false; };
  }, [url]);

  return data ? <pre>{JSON.stringify(data)}</pre> : <p>Loading...</p>;
}
```

## Related Errors

- [React Key Warning]({{< relref "/languages/javascript/react-keys" >}}) — missing keys in list rendering
- [React Hooks Violation]({{< relref "/languages/javascript/react-hooks" >}}) — rules of hooks
- [Cannot Read Properties of undefined]({{< relref "/languages/javascript/react-undefined-prop" >}}) — undefined access after unmount
