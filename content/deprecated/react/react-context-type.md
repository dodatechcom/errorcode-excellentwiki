---
title: "[Solution] Deprecated Function Migration: contextType static to useContext hook"
description: "Migrate from deprecated contextType static to useContext hook."
deprecated_function: "static contextType = ThemeContext"
replacement_function: "const theme = useContext(ThemeContext)"
languages: ["react"]
deprecated_since: "React 16.8+"
---

# [Solution] Deprecated Function Migration: contextType static to useContext hook

The `static contextType = ThemeContext` has been deprecated in favor of `const theme = useContext(ThemeContext)`.

## Migration Guide

useContext is more flexible.

## Before (Deprecated)

```react
class MyComponent extends React.Component {
    static contextType = ThemeContext;
    render() {
        return <div>{this.context.theme}</div>;
    }
}
```

## After (Modern)

```react
function MyComponent() {
    const theme = useContext(ThemeContext);
    return <div>{theme}</div>;
}
```

## Key Differences

- useContext is more flexible
