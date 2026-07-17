---
title: "[Solution] React: Error Boundary Caught Error Fix"
description: "Fix React error boundary catches in component trees. Handle rendering errors, async errors, and proper recovery strategies."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React: Error Boundary Caught Error

This error occurs when a React error boundary catches an unhandled rendering error in its child component tree. The boundary replaces the crashed tree with a fallback UI instead of crashing the entire application.

## What This Error Means

Common error messages:

- `Uncaught Error: ...` (caught by error boundary)
- `The above error occurred in the <ComponentName> component`
- `React will try to recreate this component tree from scratch`
- `Consider adding an error boundary to your tree`

Error boundaries are React class components that implement `componentDidCatch` and/or `getDerivedStateFromError`. They catch errors during rendering, lifecycle methods, and constructors — but **not** event handlers or async code.

## Common Causes

```jsx
// Cause 1: Throwing during render
function UserCard({ user }) {
  return <div>{user.name.toUpperCase()}; // user may be null
}

// Cause 2: Accessing context that doesn't exist
function ThemedButton() {
  const theme = useContext(ThemeContext); // ThemeProvider missing
  return <button className={theme}>Click</button>;
}

// Cause 3: Infinite render loop
function BadComponent() {
  const [state, setState] = useState(0);
  setState(state + 1); // runs on every render
  return <div>{state}</div>;
}

// Cause 4: Error in useEffect not caught by error boundary
useEffect(() => {
  throw new Error('async error'); // NOT caught by error boundary
}, []);
```

## How to Fix

### Fix 1: Create a robust error boundary

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
    console.error('Error caught:', error, errorInfo.componentStack);
    // Send to error tracking service
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

### Fix 2: Use error boundaries at route level

```jsx
// App.js
function App() {
  return (
    <ErrorBoundary fallback={<ErrorPage />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </ErrorBoundary>
  );
}
```

### Fix 3: Handle async errors separately

```jsx
// Async errors need try/catch or error state
function DataFetcher() {
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData()
      .catch(err => setError(err));
  }, []);

  if (error) return <div>Error: {error.message}</div>;
  return <Data />;
}
```

### Fix 4: Add null checks before rendering

```jsx
function UserCard({ user }) {
  if (!user) return <div>Loading...</div>;
  return <div>{user.name.toUpperCase()}</div>;
}
```

## Examples

```
Uncaught TypeError: Cannot read properties of undefined (reading 'toUpperCase')
    at UserCard (UserCard.jsx:5:14)
    at renderWithHooks (react-dom.development.js:...)
```

```jsx
// Fix: add optional chaining
function UserCard({ user }) {
  return <div>{user?.name?.toUpperCase() ?? 'Unknown'}</div>;
}
```

## Related Errors

- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — basic error boundary
- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — state update issues
- [React State Update Error]({{< relref "/languages/javascript/react-state-update-error" >}}) — state update on unmounted component
