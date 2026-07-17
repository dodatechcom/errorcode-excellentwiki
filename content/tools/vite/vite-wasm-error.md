---
title: "Vite WebAssembly Instantiation Error"
description: "Vite fails to load or instantiate a WebAssembly module."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "wasm", "webassembly", "instantiate", "module"]
weight: 5
---

# Vite WebAssembly — Instantiation Error

This error occurs when Vite fails to load or instantiate a WebAssembly (.wasm) module. The WASM file may be missing, corrupt, or have incompatible imports.

## Common Causes

- WASM file not found at the import path
- WASM module has unmet imports
- WASM file is corrupted or invalid
- Missing Vite WASM plugin

## How to Fix

### Use Vite WASM Plugin

```bash
npm install -D vite-plugin-wasm vite-plugin-top-level-await
```

```javascript
// vite.config.js
import wasm from 'vite-plugin-wasm';
import topLevelAwait from 'vite-plugin-top-level-await';

export default defineConfig({
  plugins: [
    wasm(),
    topLevelAwait(),
  ],
});
```

### Import WASM Module Correctly

```javascript
// Modern approach
import init, { process_data } from './pkg/my_wasm.js';

await init();
const result = process_data(input);
```

### Configure WASM Serving

```javascript
export default defineConfig({
  optimizeDeps: {
    exclude: ['my-wasm-package'],
  },
});
```

### Use WebAssembly.instantiate Directly

```javascript
const response = await fetch('/path/to/module.wasm');
const bytes = await response.arrayBuffer();
const { instance } = await WebAssembly.instantiate(bytes);
```

## Examples

```text
[vite] Internal server error: Failed to load WebAssembly module:
  Module instantiation failed: Import not found: 'env.memory'
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Deps Error]({{< relref "/tools/vite/vite-deps-error" >}}) — pre-bundling errors
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
