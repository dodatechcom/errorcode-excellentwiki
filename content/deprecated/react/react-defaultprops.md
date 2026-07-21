---
title: "[Solution] Deprecated Function Migration: defaultProps to default parameter values"
description: "Migrate from deprecated defaultProps to default parameter values in React."
deprecated_function: "Component.defaultProps"
replacement_function: "function Component({ prop = default })"
languages: ["javascript"]
deprecated_since: "React 18.3+"
---

# [Solution] Deprecated Function Migration: defaultProps to default parameter values

The `Component.defaultProps` has been deprecated in favor of `function Component({ prop = default })`.

## Migration Guide

defaultProps is deprecated for function components. Use default parameter values instead.

## Before (Deprecated)

```javascript
function Greeting({ name, greeting }) {
    return <div>{greeting}, {name}!</div>;
}

Greeting.defaultProps = {
    name: "World",
    greeting: "Hello"
};
```

## After (Modern)

```javascript
function Greeting({ name = "World", greeting = "Hello" }) {
    return <div>{greeting}, {name}!</div>;
}
```

## Key Differences

- Default params are native JavaScript
- defaultProps still works for class components
- Default params work with destructuring
- TypeScript integration is better
