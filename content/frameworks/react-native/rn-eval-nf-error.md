---
title: "[Solution] React Native eval() not allowed in production"
description: "react-native JavaScript Core or Hermes engine throws ReferenceError for eval() or Function() constructor calls in production builds"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The eval-nf error occurs when a JavaScript runtime built for production disallows eval() or the Function constructor within a React Native context. Hermes does not support eval() for performance and security reasons. JSC on iOS also restricts eval in release mode unless explicitly enabled.

## Common Causes

- Code uses eval() to parse JSON or template strings
- JavaScript minifier transforms a dynamic expression into eval()
- Third-party library tries to use Function() constructor for code generation
- Hermes engine is enabled and code contains eval() support check
- Crashlytics or Sentry source map processing triggers eval() for stack traces

## How to Fix

1. Replace eval usage with safe alternatives:

```javascript
// Bad:
const parsed = eval('(' + jsonString + ')');
// Good:
const parsed = JSON.parse(jsonString);
```

2. Replace Function constructor with literal functions:

```javascript
// Bad:
const fn = new Function('a', 'b', 'return a + b');
// Good:
const fn = (a, b) => a + b;
```

3. For third-party libraries, check configuration:

```javascript
// Sentry example
Sentry.init({
  dsn: '__DSN__',
  debug: false,
  enableNative: true,
  // disable eval() entirely
});
```

## Examples

```javascript
// Error: eval is not defined (Hermes)
// ReferenceError: Can't find variable: eval

// Fix: replace all eval() with JSON.parse or template literals
```

## Related Errors

- [Hermes Engine Error]({{< relref "/frameworks/react-native/rn-hermes-engine-error" >}})
- [RedBox Error]({{< relref "/frameworks/react-native/rn-redbox-error" >}})
