---
title: "[Solution] React Native Performance DevTools Integration Error"
description: "react-native React DevTools performance profiler fails to connect to the app or does not show component render timings on Android and iOS"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The performance profiler error occurs when the React DevTools profiler cannot connect to a running React Native app. The profiler requires a WebSocket connection through Metro, which can be blocked by firewalls, proxy settings, or configuration mismatches.

## Common Causes

- React DevTools version does not match the React version in the app
- Profiling data is not captured because the root component is not wrapped with Profiler
- Multiple React Native debugger tabs are open, creating port conflicts
- Hermes profiler uses a different protocol than JSC profiler
- Firewall blocks WebSocket connections on port 8097

## How to Fix

1. Install and open React DevTools:

```bash
npm install -g react-devtools
npx react-devtools
```

2. Wrap the root component with Profiler API:

```javascript
import { Profiler } from 'react';

const onRender = (id, phase, actualDuration) => {
  console.log(id, phase, actualDuration);
};

<Profiler id="App" onRender={onRender}>
  <App />
</Profiler>
```

3. Use Hermes sampling profiler for RN 0.70+:

```bash
npx react-native profile-hermes
```

## Examples

```javascript
// Error: DevTools shows "No React app found"
// Fix: ensure metro is running and the app is connected
// Then run:
npx react-devtools
// And from the in-app dev menu select "Open React DevTools"
```

## Related Errors

- [Dev Menu Error]({{< relref "/frameworks/react-native/rn-dev-menu-error" >}})
