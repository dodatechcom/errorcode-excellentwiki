---
title: "[Solution] Deprecated Function Migration: componentWillMount to componentDidMount"
description: "Migrate from deprecated componentWillMount to componentDidMount in React."
deprecated_function: "componentWillMount"
replacement_function: "componentDidMount"
languages: ["javascript"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: componentWillMount to componentDidMount

The `componentWillMount` has been deprecated in favor of `componentDidMount`.

## Migration Guide

componentWillMount can cause issues with SSR. componentDidMount runs after mount and is safe for data fetching.

## Before (Deprecated)

```javascript
class MyComponent extends React.Component {
    componentWillMount() {
        this.loadData();
        this.timer = setInterval(this.tick, 1000);
    }
}
```

## After (Modern)

```javascript
class MyComponent extends React.Component {
    componentDidMount() {
        this.loadData();
        this.timer = setInterval(this.tick, 1000);
    }

    componentWillUnmount() {
        clearInterval(this.timer);
    }
}

// Functional component with useEffect
function MyComponent() {
    useEffect(() => {
        loadData();
        const timer = setInterval(tick, 1000);
        return () => clearInterval(timer);
    }, []);
}
```

## Key Differences

- componentDidMount runs after mount
- componentWillUnmount for cleanup
- useEffect is the modern equivalent
