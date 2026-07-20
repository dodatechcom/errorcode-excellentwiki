---
title: "[Solution] JavaScript Electron Build Error — How to Fix"
description: "Fix JavaScript Electron electron-builder packaging errors, code signing failures, native module rebuilds, and distribution configuration issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 807
---

# JavaScript Electron Build Error

An `Error`, `BuildError`, or `NativeModuleError` occurs when `electron-builder` fails to package the application, code signing certificates are invalid, native modules do not rebuild for Electron's Node.js version, or platform-specific configuration is missing.

## Why It Happens

Build errors stem from missing build configuration in `package.json`, native modules compiled for the wrong Node.js ABI, expired or missing code signing certificates, incorrect `electron-builder` YAML/JSON config, and platform-specific packaging requirements.

## Common Error Messages

- `Error: Cannot find module 'electron-builder'`
- `BuildError: Application is not signed`
- `Error: The native module 'xxx' is not compatible with Electron`
- `Error: ENOENT: no such file or directory, stat 'dist/xxx'`
- `Error: electron-builder configuration is invalid`

## How to Fix It

### Fix 1: Configure electron-builder in package.json

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "main": "main.js",
  "build": {
    "appId": "com.example.myapp",
    "productName": "MyApp",
    "directories": {
      "output": "release"
    },
    "files": [
      "dist/**/*",
      "main.js",
      "preload.js"
    ]
  }
}
```

### Fix 2: Rebuild native modules for Electron

```bash
# ❌ Wrong - using system Node.js modules directly
# npm install

# ✅ Correct - rebuild for Electron's ABI
npx electron-rebuild

# Or configure postinstall script
# "postinstall": "electron-builder install-app-deps"
```

### Fix 3: Code signing configuration

```json
{
  "build": {
    "win": {
      "certificateFile": "cert.pfx",
      "certificatePassword": "",
      "signingHashAlgorithms": ["sha256"]
    },
    "mac": {
      "hardenedRuntime": true,
      "gatekeeperAssess": false,
      "identity": "Developer ID Application: Your Name (TEAMID)"
    }
  }
}
```

### Fix 4: Platform-specific build config

```json
{
  "build": {
    "linux": {
      "target": ["AppImage", "deb"],
      "category": "Utility",
      "icon": "build/icon.png"
    },
    "win": {
      "target": ["nsis"],
      "icon": "build/icon.ico"
    },
    "mac": {
      "target": ["dmg"],
      "icon": "build/icon.icns"
    }
  }
}
```

## Examples

Full electron-builder configuration:

```json
{
  "build": {
    "appId": "com.example.myapp",
    "productName": "MyApp",
    "directories": { "output": "release" },
    "files": ["dist/**/*", "main.js", "preload.js", "assets/**/*"],
    "extraResources": ["native/**/*"],
    "asar": true,
    "asarUnpack": ["native/**"],
    "win": { "target": "nsis", "icon": "build/icon.ico" },
    "mac": { "target": "dmg", "icon": "build/icon.icns", "hardenedRuntime": true },
    "linux": { "target": "AppImage", "icon": "build/icon.png" }
  }
}
```

## Related Errors

- [Electron Error](/languages/javascript/electron-error)
- [JavaScript ENOENT](/languages/javascript/enoent-node)
- [JavaScript Module Not Found](/languages/javascript/err-module-not-found)
