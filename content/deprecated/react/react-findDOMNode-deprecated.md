---
title: "[Solution] Deprecated Function Migration: ReactDOM.findDOMNode to ref"
description: "Migrate from deprecated ReactDOM.findDOMNode to ref."
deprecated_function: "ReactDOM.findDOMNode(this)"
replacement_function: "ref.current"
languages: ["react"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: ReactDOM.findDOMNode to ref

The `ReactDOM.findDOMNode(this)` has been deprecated in favor of `ref.current`.

## Migration Guide

ref is more explicit.

## Before (Deprecated)

```react
const node = ReactDOM.findDOMNode(this);
```

## After (Modern)

```react
const node = ref.current;
```

## Key Differences

- ref is more explicit
