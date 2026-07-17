---
title: "[Solution] React Cannot Read Properties of undefined — Undefined Prop Access Fix"
description: "Fix React 'Cannot read properties of undefined' errors. Add null checks, use optional chaining, and validate props before rendering."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# React: Cannot Read Properties of undefined (reading 'X')

This error occurs in React when you try to access a property on a value that is `undefined` or `null` — typically inside a component's render method or event handler. It is the React-specific version of the general JavaScript `TypeError: Cannot read properties of undefined`.

## Common Causes

- **Props not yet loaded** — component renders before async data arrives
- **Nested prop access without null checks** — `user.profile.name` when `profile` is undefined
- **Destructuring undefined props** — `const { name } = props` when `props` is undefined
- **State not initialized** — accessing state that hasn't been set yet

## How to Fix

```jsx
// Cause 1: Accessing props before data loads
function UserProfile({ user }) {
  return <h1>{user.name}</h1>;  // TypeError if user is undefined
}

// Fix: check for undefined before rendering
function UserProfile({ user }) {
  if (!user) return <p>Loading...</p>;
  return <h1>{user.name}</h1>;
}

// Cause 2: Nested property access
function UserCard({ user }) {
  return <p>{user.address.city}</p>;  // TypeError if address is undefined
}

// Fix: optional chaining
function UserCard({ user }) {
  return <p>{user?.address?.city ?? "Unknown"}</p>;
}

// Cause 3: Destructuring undefined
function Greeting({ user }) {
  const { name, email } = user;  // TypeError if user is undefined
  return <p>Hello {name}</p>;
}

// Fix: provide defaults
function Greeting({ user }) {
  const { name = "Guest", email = "" } = user ?? {};
  return <p>Hello {name}</p>;
}
```

```jsx
// Cause 4: Array mapping on undefined
function ItemList({ items }) {
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}  // TypeError if items is undefined
    </ul>
  );
}

// Fix: default to empty array
function ItemList({ items = [] }) {
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
}

// Cause 5: API response missing expected structure
function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("/api/posts")
      .then(r => r.json())
      .then(data => setPosts(data.posts));  // TypeError if data.posts is undefined
  }, []);

  return (
    <ul>
      {posts.map(p => <li key={p.id}>{p.title}</li>)}
    </ul>
  );
}

// Fix: validate response structure
useEffect(() => {
  fetch("/api/posts")
    .then(r => r.json())
    .then(data => {
      setPosts(Array.isArray(data?.posts) ? data.posts : []);
    });
}, []);
```

## Related Errors

- [React Key Warning]({{< relref "/languages/javascript/react-keys" >}}) — missing keys in list rendering
- [React State Update on Unmounted]({{< relref "/languages/javascript/react-state-update" >}}) — state updates after unmount
- [TypeError: Cannot read properties of undefined]({{< relref "/languages/javascript/typeerror-cannot-read" >}}) — general JS version
