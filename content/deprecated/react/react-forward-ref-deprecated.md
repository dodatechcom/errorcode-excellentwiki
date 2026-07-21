---
title: "[Solution] Deprecated Function Migration: forwardRef to ref as prop"
description: "Migrate from deprecated forwardRef to ref as prop."
deprecated_function: "React.forwardRef((props, ref) => <input ref={ref} />)"
replacement_function: "function MyInput({ ref, ...props }) {}"
languages: ["react"]
deprecated_since: "React 19+"
---

# [Solution] Deprecated Function Migration: forwardRef to ref as prop

The `React.forwardRef((props, ref) => <input ref={ref} />)` has been deprecated in favor of `function MyInput({ ref, ...props }) {}`.

## Migration Guide

ref as prop is simpler.

## Before (Deprecated)

```react
const MyInput = React.forwardRef((props, ref) => {
    return <input ref={ref} {...props} />;
});
```

## After (Modern)

```react
function MyInput({ ref, ...props }) {
    return <input ref={ref} {...props} />;
}
```

## Key Differences

- ref as prop is simpler
