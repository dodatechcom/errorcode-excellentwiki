---
title: "[Solution] Deprecated Function Migration: componentWillUpdate to componentDidUpdate"
description: "Migrate from deprecated componentWillUpdate to componentDidUpdate in React."
deprecated_function: "componentWillUpdate"
replacement_function: "componentDidUpdate"
languages: ["javascript"]
deprecated_since: "React 16.3+"
---

# [Solution] Deprecated Function Migration: componentWillUpdate to componentDidUpdate

The `componentWillUpdate` has been deprecated in favor of `componentDidUpdate`.

## Migration Guide

componentDidUpdate runs after re-rendering and receives previous props/state.

## Before (Deprecated)

```javascript
class MyComponent extends React.Component {
    componentWillUpdate(nextProps, nextState) {
        if (nextState.count !== this.state.count) {
            this.scrollToBottom();
        }
    }
}
```

## After (Modern)

```javascript
class MyComponent extends React.Component {
    componentDidUpdate(prevProps, prevState) {
        if (this.state.count !== prevState.count) {
            this.scrollToBottom();
        }
    }
}

// Or with useEffect
function MyComponent() {
    const [count, setCount] = useState(0);
    useEffect(() => {
        scrollToBottom();
    }, [count]);
}
```

## Key Differences

- componentDidUpdate receives prevProps/prevState
- Side effects go after render
- Check for specific prop/state changes
- useEffect replaces this in functional components
