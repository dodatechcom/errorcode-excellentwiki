---
title: "[Solution] React Native AppState Change Detection Error"
description: "react-native AppState API fails to detect app foreground and background transitions on iOS and Android, causing stale or missed state change events in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The AppState error occurs when the AppState API returns stale values or misses state transitions between active, inactive, and background states. This commonly disrupts real-time features like WebSocket reconnection, timer suspension, or data sync.

## Common Causes

- AppState listener not cleaned up on component unmount
- Using deprecated AppStateIOS instead of AppState
- State comparison using reference equality instead of string check
- Multiple listeners causing conflicting state updates
- Not handling the 'inactive' state on iOS (e.g., during incoming calls)

## How to Fix

1. Subscribe correctly with cleanup:

```javascript
import { AppState } from 'react-native';

useEffect(() => {
  const subscription = AppState.addEventListener('change', (nextState) => {
    if (nextState === 'background') {
      pauseWebSocket();
    }
    if (nextState === 'active') {
      reconnectWebSocket();
    }
  });
  return () => subscription.remove();
}, []);
```

2. Use currentState as fallback on mount:

```javascript
const appState = useRef(AppState.currentState);
```

## Examples

```javascript
// Error: state never transitions to background
const handleChange = (state) => {
  if (state !== 'active') { /* never fires */ }
};

// Fix: compare exact string
if (state === 'background') { /* works */ }
```

## Related Errors

- [Network Error]({{< relref "/frameworks/react-native/rn-network-error" >}})
