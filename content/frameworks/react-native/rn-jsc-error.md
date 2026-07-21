---
title: "[Solution] React Native JSC JavaScriptCore Engine Error"
description: "react-native JavaScriptCore crash on iOS due to memory pressure, large allocation, or JSContext deallocation while active code is executing"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The JSC engine error on iOS manifests as a crash within JavaScriptCore during heavy computation or memory pressure. iOS's JavaScriptCore is provided by the system and its memory limits vary by device model and OS version, causing hard-to-reproduce crashes.

## Common Causes

- Large data parsing (JSON > 50MB) causing JSC memory limit breach
- Circular JSON structures that cannot be serialized
- JSContext being garbage collected while a callback is pending
- Intensive operations in tight loops blocking the main thread for too long
- Using eval() or Function constructor which JSC can handle but may crash under pressure

## How to Fix

1. Switch to Hermes engine for more predictable memory behavior:

```bash
npm install --save-dev react-native-hermes
npx react-native config
```

2. Chunk large data processing:

```javascript
// Break large JSON parsing into batches
const batchSize = 1000;
for (let i = 0; i < totalItems; i += batchSize) {
  const batch = items.slice(i, i + batchSize);
  processBatch(batch);
  await new Promise(r => setTimeout(r, 0)); // yield to event loop
}
```

3. Set JSC memory limit if using custom JSC:

```objectivec
// iOS: custom JSC configuration
JSContext *context = [[JSContext alloc] init];
context[@"memoryLimit"] = @(256 * 1024 * 1024);
```

## Examples

```javascript
// Error: JavaScriptCore code called, but the previous pending state was already cleared
// Fix: ensure long operations yield
const results = [];
for (const item of data) {
  results.push(transform(item));
  if (results.length % 1000 === 0) {
    await new Promise(setImmediate); // yield
  }
}
```

## Related Errors

- [Hermes Engine Error]({{< relref "/frameworks/react-native/rn-hermes-engine-error" >}})
