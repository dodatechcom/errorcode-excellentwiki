---
title: "[Solution] React Native Excessive Verbose Logs in Console"
description: "react-native Metro bundler outputs too many verbose logs during development, slowing down the Metro terminal and making error detection difficult"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The verbose logs error occurs when Metro or React Native prints an overwhelming amount of diagnostic output. This is common when network logging is enabled, or when working on complex screens that trigger layout recalculations in every frame.

## Common Causes

- __DEV__ logging left in production libraries
- Network logging enabled with Debugger mode active
- Multiple console.log calls inside frequently re-rendering components
- React DevTools verbose logging for component profiling
- Hermes engine debug messages printed to stderr
- Flipper connection negotiation logs

## How to Fix

1. Silence verbose Metro output:

```bash
npx react-native start --no-interactive --max-workers 2
```

2. Filter logs in Metro terminal:

```bash
# Use grep to exclude noisy patterns
npx react-native start 2>&1 | grep -v "VERBOSE\|SocketState"
```

3. Reduce console.log in production:

```javascript
const log = __DEV__ ? console.log : () => {};
// Or use a dedicated logging library with log levels
```

4. Disable Hermes detailed logs:

```bash
# Run with HERMES_ENABLE_VERBOSE_LOGGING=false
export HERMES_ENABLE_VERBOSE_LOGGING=false
npx react-native run-android
```

## Examples

```javascript
// Fix: wrap debug logs in dev only
if (__DEV__) {
  console.log('Layout recalculated', measurements);
}
```

## Related Errors

- [LogBox Error]({{< relref "/frameworks/react-native/rn-logbox-error" >}})
