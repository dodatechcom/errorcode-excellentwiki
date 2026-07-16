---
title: "[Solution] React Error Boundary Caught an Error — Fix Guide"
description: "Fix React Error Boundary caught errors. Implement error boundaries with componentDidCatch, handle render errors, and recover gracefully."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react", "error-boundary", "componentDidCatch", "catch", "render", "recovery"]
weight: 5
---

# React Error Boundary Caught an Error

An **Error Boundary** is a React class component that catches JavaScript errors during rendering, in lifecycle methods, and in constructors of the tree below it. When an error is caught, the boundary renders a fallback UI instead of crashing the entire application.

## Description

React Error Boundaries are the only way to catch errors in the React component tree. Without them, an error in any component propagates to the root and unmounts the entire UI. Error boundaries use `componentDidCatch` and `static getDerivedStateFromError` to catch and handle errors.

The error message `The above error occurred in the <Component> error boundary` indicates that an error boundary caught and displayed a fallback UI.

## Common Causes

- **Runtime error in render** — accessing properties on undefined/null data
- **Failed network request during render** — synchronous data fetching that throws
- **Invalid JSX** — returning malformed JSX from a component
- **Error in child lifecycle** — error in componentDidMount or componentDidUpdate of a child

## How to Fix

### Fix 1: Create a reusable Error Boundary component

```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error Boundary caught:', error, errorInfo.componentStack);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div role="alert">
          <h2>Something went wrong</h2>
          <details>
            <summary>Error details</summary>
            <pre>{this.state.error?.message}</pre>
          </details>
          <button onClick={() => this.setState({ hasError: false })}>
            Try Again
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}
```

### Fix 2: Wrap components with Error Boundary

```jsx
function App() {
  return (
    <ErrorBoundary>
      <Header />
      <ErrorBoundary>
        <MainContent />
      </ErrorBoundary>
      <Footer />
    </ErrorBoundary>
  );
}
```

### Fix 3: Handle async errors (not caught by boundaries)

```jsx
// Error boundaries don't catch async errors — use try/catch
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchUser(userId)
      .then(setUser)
      .catch(err => setError(err.message));
  }, [userId]);

  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>Loading...</div>;
  return <div>{user.name}</div>;
}
```

### Fix 4: Log errors to an external service

```jsx
componentDidCatch(error, errorInfo) {
  logErrorToService({
    error: error.message,
    stack: error.stack,
    componentStack: errorInfo.componentStack,
  });
}
```

## Examples

```jsx
class BuggyCounter extends Component {
  state = { count: 0 };

  handleClick = () => {
    this.setState(prev => ({ count: prev.count + 1 }));
    if (this.state.count === 4) {
      throw new Error('Counter exploded!');
    }
  };

  render() {
    return <button onClick={this.handleClick}>{this.state.count}</button>;
  }
}

function App() {
  return (
    <ErrorBoundary>
      <BuggyCounter />
    </ErrorBoundary>
  );
}
```

## Related Errors

- [react-invariant]({{< relref "/languages/javascript/react-invariant" >}}) — invariant violations in React internals.
- [react-hooks]({{< relref "/languages/javascript/react-hooks" >}}) — invalid hook calls.
- [react-undefined-prop]({{< relref "/languages/javascript/react-undefined-prop" >}}) — accessing undefined props.
