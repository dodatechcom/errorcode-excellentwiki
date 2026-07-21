---
title: "[Solution] Deprecated Function Migration: defaultProps to default parameters"
description: "Migrate from deprecated defaultProps to default parameters."
deprecated_function: "MyComponent.defaultProps = { color: 'blue' }"
replacement_function: "function MyComponent({ color = 'blue' }) {}"
languages: ["react"]
deprecated_since: "React 18.3+"
---

# [Solution] Deprecated Function Migration: defaultProps to default parameters

The `MyComponent.defaultProps = { color: 'blue' }` has been deprecated in favor of `function MyComponent({ color = 'blue' }) {}`.

## Migration Guide

Default parameters are simpler.

## Before (Deprecated)

```react
MyComponent.defaultProps = {
    color: 'blue'
};
```

## After (Modern)

```react
function MyComponent({ color = 'blue' }) {
    return <div style={{ color }} />;
}
```

## Key Differences

- Default parameters are simpler
