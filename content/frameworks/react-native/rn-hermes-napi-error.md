---
title: "[Solution] React Native Hermes N-API Native Module Link Error"
description: "react-native Hermes engine N-API symbols missing causing native module initialization crash on Android and iOS in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Hermes N-API error occurs when a native module compiled against JavaScriptCore is loaded into the Hermes runtime. Hermes does not implement all N-API (Node.js API for native addons) symbols, causing a crash when the module tries to call an unimplemented function.

## Common Causes

- Native addon uses node_api.h functions that Hermes does not stub
- N-API module compiled with node-gyp expecting full Node.js runtime
- React Native library assumes JSC is the runtime and does not check for Hermes
- mmkv or crypto-native module using Buffer API not available in Hermes
- Misconfigured build settings for N-API in android/CMakeLists.txt

## How to Fix

1. Check if the native module is Hermes-compatible before use:

```javascript
import { Platform } from 'react-native';

if (global.HermesInternal) {
  console.warn('Hermes does not support this native module');
}
```

2. Configure CMakeLists.txt to exclude N-API symbols when using Hermes:

```cmake
if(HERMES_ENABLED)
  target_compile_definitions(MyModule PRIVATE HERMES=1)
endif()
```

3. Use a compatibility shim in native code:

```cpp
#ifdef HERMES
  // Fallback to plain JNI call
#else
  // Use N-API
  napi_call_function(env, ...);
#endif
```

## Examples

```cpp
// Error: undefined symbol: napi_create_buffer
// The module uses napi_create_buffer which is not in Hermes

// Fix: replace with JNI direct methods when Hermes is detected
if (env->IsSameObject(env->GetRuntime(), hermesRuntime)) {
  // Alternative JNI implementation
}
```

## Related Errors

- [Hermes Engine Error]({{< relref "/frameworks/react-native/rn-hermes-engine-error" >}})
