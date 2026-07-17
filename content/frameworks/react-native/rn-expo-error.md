---
title: "Expo - module not found error"
description: "Expo project throws module not found error when a required native module is missing or incompatible"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The Expo module not found error occurs when your Expo project references a module that is not installed, requires a config plugin, or is incompatible with Expo's managed workflow. Expo has specific rules about which native modules can be used.

## Common Causes

- Module requires a native code configuration not present in managed workflow
- Expo config plugin not added to `app.json`/`app.config.js`
- Module is not compatible with Expo's current SDK version
- Missing `expo` package updates after SDK upgrade
- Module requires `expo prebuild` to generate native code

## How to Fix

1. Install the module with the Expo-compatible package:

```bash
npx expo install expo-camera
# Use expo install instead of npm install
```

2. Add required config plugins to `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "expo-camera",
        {
          "cameraPermission": "Allow $(PRODUCT_NAME) to access camera"
        }
      ]
    ]
  }
}
```

3. Run prebuild to generate native code:

```bash
npx expo prebuild --clean
```

4. Check SDK compatibility:

```bash
npx expo install --check
```

5. For bare workflow, ensure pods are installed:

```bash
cd ios && pod install
```

## Examples

```bash
$ npx expo start
Error: Module not found: Can't resolve 'expo-camera'
# Fix: use expo install
$ npx expo install expo-camera
```

```bash
# Module found but needs config plugin
Error: 'expo-camera' requires a config plugin. Add 'expo-camera' to plugins in app.json.
```

## Related Errors

- [Expo build error]({{< relref "/frameworks/react-native/rn-expo-build-error" >}})
- [Expo dev client error]({{< relref "/frameworks/react-native/rn-expo-dev-client" >}})
