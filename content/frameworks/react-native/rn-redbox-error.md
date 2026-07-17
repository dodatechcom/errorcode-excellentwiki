---
title: "RedBox error - runtime JS error"
description: "React Native displays a RedBox error when a JavaScript runtime error occurs during development"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a JavaScript runtime error is thrown during React Native development. The RedBox overlay displays the error message, stack trace, and file location.

## Common Causes

- `TypeError` or `ReferenceError` in component code
- Accessing a property on `null` or `undefined`
- State mutation outside of `setState` or state management
- API response structure differs from expected format
- Component throws during render

## How to Fix

1. Use Error Boundaries to catch render errors:

```javascript
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <Text>Something went wrong: {this.state.error.message}</Text>;
    }
    return this.props.children;
  }
}

// Wrap components
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

2. Add null checks for optional data:

```javascript
const UserProfile = ({ user }) => {
  return (
    <View>
      <Text>{user?.profile?.name ?? 'Unknown'}</Text>
    </View>
  );
};
```

3. Enable LogBox to see warnings instead of RedBox:

```javascript
import { LogBox } from 'react-native';
LogBox.ignoreLogs(['Warning: ...']);
```

## Examples

```javascript
// Accessing property on undefined
const UserCard = ({ user }) => (
  <Text>{user.name}</Text> // RedBox if user is undefined
);
```

## Related Errors

- [Native module error]({{< relref "/frameworks/react-native/native-module-error" >}})
- [Build error]({{< relref "/frameworks/react-native/build-error5" >}})
