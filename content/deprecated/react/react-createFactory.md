---
title: "[Solution] Deprecated Function Migration: React.createFactory to JSX"
description: "Migrate from deprecated React.createFactory to JSX."
deprecated_function: "React.createFactory(Component)"
replacement_function: "<Component />"
languages: ["react"]
deprecated_since: "React 16.0+"
---

# [Solution] Deprecated Function Migration: React.createFactory to JSX

The `React.createFactory(Component)` has been deprecated in favor of `<Component />`.

## Migration Guide

JSX is more readable.

## Before (Deprecated)

```react
const factory = React.createFactory(MyComponent);
const element = factory({ name: 'Alice' });
```

## After (Modern)

```react
const element = <MyComponent name="Alice" />;
```

## Key Differences

- JSX is more readable
