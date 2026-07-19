---
title: "React lazy loading and code splitting errors"
description: "Errors related to lazy loading components with React.lazy. Common issues include missing Suspense boundaries, incorrect import paths, or not handling loading states properly."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "lazy", "code-splitting", "performance"]
severity: "error"
solution: "Always wrap lazy components with Suspense and provide a fallback. Ensure import paths are correct. Handle errors with Error Boundaries. Consider preloading strategies for better UX."
---

Errors related to lazy loading components with React.lazy. Common issues include missing Suspense boundaries, incorrect import paths, or not handling loading states properly.

## Solution

Always wrap lazy components with Suspense and provide a fallback. Ensure import paths are correct. Handle errors with Error Boundaries. Consider preloading strategies for better UX.

## Code Example

```javascript
  import { lazy, Suspense, useState } from 'react';
  import { ErrorBoundary } from 'react-error-boundary';
  
  // BAD: Missing Suspense
  const BadComponent = lazy(() => import('./BadComponent'));
  
  function BadApp() {
    return <BadComponent />; // Error!
  }
  
  // GOOD: Proper lazy loading with Suspense
  const GoodComponent = lazy(() => import('./GoodComponent'));
  
  function GoodApp() {
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <GoodComponent />
      </Suspense>
    );
  }
  
  // GOOD: With Error Boundary
  function App() {
    return (
      <ErrorBoundary fallback={<div>Error loading component</div>}>
        <Suspense fallback={<div>Loading...</div>}>
          <LazyComponent />
        </Suspense>
      </ErrorBoundary>
    );
  }
  
  // GOOD: Preloading strategy
  const LazyComponent = lazy(() => import('./LazyComponent'));
  
  function preloadComponent() {
    // Preload on hover or intent
    import('./LazyComponent');
  }
  
  function AppWithPreload() {
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <div onMouseEnter={preloadComponent}>
          <LazyComponent />
        </div>
      </Suspense>
    );
  }
  
  // GOOD: Route-based code splitting
  const Dashboard = lazy(() => import('./pages/Dashboard'));
  const Settings = lazy(() => import('./pages/Settings'));
  
  function App() {
    const [currentPage, setCurrentPage] = useState('dashboard');
    
    return (
      <Suspense fallback={<PageSkeleton />}>
        {currentPage === 'dashboard' && <Dashboard />}
        {currentPage === 'settings' && <Settings />}
      </Suspense>
    );
  }
```
