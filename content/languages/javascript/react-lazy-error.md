---
title: "[Solution] React Lazy Expected a ReactElement Type — Lazy Component Error Fix"
description: "Fix React 'React.lazy: Expected a ReactElement type' error. Understand lazy loading requirements, default exports, and dynamic import patterns."
languages: ["javascript"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# React: React lazy — Expected a ReactElement type

This error occurs when `React.lazy()` receives something that is not a function returning a Promise that resolves to a module with a `default` export containing a React component. It typically happens when the dynamic import doesn't return a component, or the module structure doesn't match what `React.lazy` expects.

## Common Causes

- **Module doesn't have a default export** — `React.lazy` requires the resolved module to have `module.default` as a component
- **Named export used instead of default** — `export function MyComponent` instead of `export default function MyComponent`
- **Import returns non-component** — the lazy import resolves to a non-React value
- **Missing Suspense boundary** — lazy component rendered without a parent `<Suspense>`

## How to Fix

```jsx
// Cause 1: Named export instead of default export
// MyComponent.js — named export
export function MyComponent() {
  return <div>Lazy Loaded</div>;
}

// App.js — WRONG: React.lazy expects default export
const LazyComponent = React.lazy(() => import("./MyComponent"));

// Fix 1a: Add default export to MyComponent.js
// MyComponent.js
export default function MyComponent() {
  return <div>Lazy Loaded</div>;
}

// Fix 1b: Wrap the import in React.lazy with wrapper
const LazyComponent = React.lazy(() =>
  import("./MyComponent").then(module => ({
    default: module.MyComponent,
  }))
);

// Cause 2: Missing Suspense boundary
function App() {
  const LazyComponent = React.lazy(() => import("./HeavyComponent"));
  return <LazyComponent />;  // Error: no Suspense boundary
}

// Fix: wrap in Suspense
function App() {
  const LazyComponent = React.lazy(() => import("./HeavyComponent"));
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <LazyComponent />
    </Suspense>
  );
}
```

```jsx
// Complete working example
// components/HeavyChart.js
export default function HeavyChart({ data }) {
  return <div className="chart">{/* complex chart rendering */}</div>;
}

// App.js
import React, { Suspense } from "react";

const HeavyChart = React.lazy(() => import("./components/HeavyChart"));

function App() {
  const chartData = [1, 2, 3, 4, 5];

  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<div>Loading chart...</div>}>
        <HeavyChart data={chartData} />
      </Suspense>
    </div>
  );
}
```

```jsx
// Lazy loading with error boundary
import React, { Suspense } from "react";

const LazyPage = React.lazy(() => import("./pages/Dashboard"));

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <p>Failed to load component.</p>;
    }
    return this.props.children;
  }
}

function App() {
  return (
    <ErrorBoundary>
      <Suspense fallback={<p>Loading...</p>}>
        <LazyPage />
      </Suspense>
    </ErrorBoundary>
  );
}
```

## Common Patterns

```jsx
// Lazy load a page component with named export
const Dashboard = React.lazy(() =>
  import("./pages/Dashboard").then(module => ({
    default: module.DashboardPage,
  }))
);

// Lazy load with preload hint
const LazyComponent = React.lazy(() => import("./HeavyComponent"));

// Preload on hover
function preloadHeavyComponent() {
  import("./HeavyComponent");
}

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <button onMouseEnter={preloadHeavyComponent}>
        Show Heavy Component
      </button>
      <LazyComponent />
    </Suspense>
  );
}
```

## Related Errors

- [React Key Warning]({{< relref "/languages/javascript/react-keys" >}}) — missing keys in list rendering
- [React Context Error]({{< relref "/languages/javascript/react-context-error" >}}) — useContext without Provider
- [React Hooks Violation]({{< relref "/languages/javascript/react-hooks" >}}) — rules of hooks
