---
title: "[Solution] Deprecated Function Migration: legacy context to React.createContext"
description: "Migrate from deprecated legacy context API to React.createContext."
deprecated_function: "childContextTypes / contextTypes"
replacement_function: "React.createContext"
languages: ["javascript"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: legacy context to React.createContext

The `childContextTypes / contextTypes` has been deprecated in favor of `React.createContext`.

## Migration Guide

Legacy context has re-render issues. Modern Context API is more efficient.

## Before (Deprecated)

```javascript
class Parent extends React.Component {
    getChildContext() { return { color: this.props.color }; }
}
Parent.childContextTypes = { color: PropTypes.string };

class Child extends React.Component {
    render() { return <div>{this.context.color}</div>; }
}
Child.contextTypes = { color: PropTypes.string };
```

## After (Modern)

```javascript
const ThemeContext = React.createContext("light");

function Parent({ children }) {
    return (
        <ThemeContext.Provider value="dark">
            {children}
        </ThemeContext.Provider>
    );
}

function Child() {
    return (
        <ThemeContext.Consumer>
            {color => <div>{color}</div>}
        </ThemeContext.Consumer>
    );
}

// Or with useContext hook
function Child() {
    const color = useContext(ThemeContext);
    return <div>{color}</div>;
}
```

## Key Differences

- React.createContext() creates a Context
- Provider wraps children with a value
- Consumer or useContext reads the value
- More efficient re-rendering
