---
title: "[Solution] React Native Debugger UI Not Loading"
description: "react-native debugger or Chrome DevTools fails to connect or shows blank screen in Hermes mode for React Native development on all platforms"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The debugger UI error occurs when the Metro bundler cannot establish a WebSocket connection with the debugger, or the Hermes engine debug proxy mismatches the React Native version installed.

## Common Causes

- Hermes debugger port conflict with Metro port when using explicit ports
- React Native DevTools plugin not updated to match rn version
- app.json debuggerHost set incorrectly
- WebSocket from emulator/device fails to connect due to network proxy
- Android emulator proxy settings prevent WebSocket tunneling
- Chrome DevTools hangs on 'Debugging' with warning: full page reload is needed

## How to Fix

1. Reset the debugger session completely:

```bash
npx react-native start --reset-cache
# Press d to show dev menu, then Reload
```

2. Use the new React Native DevTools for RN 0.76+:

```bash
npm install -g @react-native/devtools
npx react-native devtools
```

3. Set the debuggerHost explicitly if behind a proxy:

```javascript
// app.json
{
  "name": "MyApp",
  "debuggerHost": "192.168.1.10:8081"
}
```

## Examples

```javascript
// Error: "Debugger disconnected - check your connection"
// with the red screen flickering

// Fix: disable and re-enable debugging from the dev menu
// or run:
adb reverse tcp:8081 tcp:8081
```

## Related Errors

- [Flipper Error]({{< relref "/frameworks/react-native/rn-flipper-error" >}})
- [Bundler Error]({{< relref "/frameworks/react-native/rn-bundler-error" >}})
