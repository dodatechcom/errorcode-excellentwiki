---
title: "React error boundary handling errors"
description: "Error that occurs when Error Boundaries are not properly implemented or when errors occur outside of Error Boundaries. Error Boundaries only catch errors in lifecycle methods and constructors, not in event handlers or async code."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "error-boundary", "handling", "crash"]
severity: "error"
solution: "Wrap component trees with Error Boundaries at appropriate levels. Use try-catch in event handlers and async code. Implement proper fallback UIs. Consider using libraries like react-error-boundary for easier implementation."
---

Error that occurs when Error Boundaries are not properly implemented or when errors occur outside of Error Boundaries. Error Boundaries only catch errors in lifecycle methods and constructors, not in event handlers or async code.

## Solution

Wrap component trees with Error Boundaries at appropriate levels. Use try-catch in event handlers and async code. Implement proper fallback UIs. Consider using libraries like react-error-boundary for easier implementation.

## Code Example

```javascript
  import { Component } from 'react';
  
  // Basic Error Boundary implementation
  class ErrorBoundary extends Component {
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
        return (
          <div className="error-fallback">
            <h2>Something went wrong</h2>
            <button onClick={() => this.setState({ hasError: false })}>
              Try again
            </button>
          </div>
        );
      }
      return this.props.children;
    }
  }
  
  // GOOD: Using Error Boundary
  function App() {
    return (
      <ErrorBoundary>
        <Header />
        <main>
          <ErrorBoundary>
            <Sidebar />
          </ErrorBoundary>
          <ErrorBoundary>
            <Content />
          </ErrorBoundary>
        </main>
      </ErrorBoundary>
    );
  }
  
  // GOOD: Try-catch in event handlers
  function Button() {
    const handleClick = async () => {
      try {
        await riskyOperation();
      } catch (error) {
        console.error('Operation failed:', error);
        // Show user-friendly error
      }
    };
    
    return <button onClick={handleClick}>Click me</button>;
  }
```
