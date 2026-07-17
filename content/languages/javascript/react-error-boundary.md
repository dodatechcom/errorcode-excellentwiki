---
title: "[Solution] React Error Boundary Caught Error Fix"
description: "Fix React error boundary caught errors. Implement proper error boundaries, handle component errors, and provide graceful fallbacks."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react", "error-boundary", "component-error", "fallback", "catch"]
weight: 5
---

# React Error Boundary — caught error

This error is caught by a React Error Boundary when a rendering error occurs in a child component. Error boundaries catch JavaScript errors during rendering, lifecycle methods, and constructors.

## What This Error Means

Common error messages:

- `Uncaught Error: <Component> threw during render`
- `The above error occurred in the <Component> component`
- `React will try to recreate this component from scratch`

Error boundaries are React class components with `componentDidCatch` and `getDerivedStateFromError` methods. They catch errors in their children, not in themselves.

## Common Causes

```jsx
// Cause 1: Accessing null/undefined props
function UserCard({ user }) {
  return <h1>{user.name}</h1>; // user is null = error
}

// Cause 2: Throwing in render
function BadComponent() {
  throw new Error('Component failed');
  return <div>Never reached</div>;
}

// Cause 3: Invalid hook usage
function BadHook() {
  if (condition) {
    useEffect(() => {}); // conditional hook = error
  }
}

// Cause 4: Async errors not caught
async function fetchData() {
  const res = await fetch('/api'); // network error
  return res.json();
}
```

## How to Fix

### Fix 1: Create an error boundary

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong: {this.state.error.message}</h1>;
    }
    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
}
```

### Fix 2: Add null checks

```jsx
function UserCard({ user }) {
  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

### Fix 3: Use optional chaining

```jsx
function UserCard({ user }) {
  return <h1>{user?.name ?? 'Unknown'}</h1>;
}
```

### Fix 4: Handle async errors separately

```jsx
function DataLoader() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api')
      .then(res => res.json())
      .then(setData)
      .catch(setError);
  }, []);

  if (error) return <div>Error: {error.message}</div>;
  if (!data) return <div>Loading...</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

## Examples

```jsx
// This triggers error boundary
function RiskyComponent() {
  const data = undefined;
  return <div>{data.map(i => <p key={i}>{i}</p>)}</div>;
  // TypeError: Cannot read properties of undefined
}

// Wrap in error boundary
function App() {
  return (
    <ErrorBoundary fallback={<p>Something went wrong</p>}>
      <RiskyComponent />
    </ErrorBoundary>
  );
}
```

## Related Errors

- [React Key Prop]({{< relref "/languages/javascript/react-key-prop" >}}) — unique key warning
- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — unmounted component
- [React JSX Runtime]({{< relref "/languages/javascript/react-jsx-runtime" >}}) — JSX runtime not found
