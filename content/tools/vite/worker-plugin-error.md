---
title: "[Solution] Vite Worker Plugin Error"
description: "Fix Vite worker plugin errors when web worker bundling fails due to incompatible configuration or plugin conflicts."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite Worker Plugin Error

Vite supports web workers via a dedicated plugin that bundles worker scripts. This error occurs when the worker plugin cannot process worker entry points, often due to configuration conflicts or incompatible module formats.

## Common Causes

- The worker entry file uses top-level await which is unsupported in some worker contexts
- A plugin registered for the worker build conflicts with the main build plugins
- The `worker.rollupOptions` configuration contains invalid Rollup options
- The worker imports CSS or assets that the bundler cannot resolve

## How to Fix

1. Ensure the worker entry file uses standard module syntax:

```javascript
// Worker entry -- avoid top-level await
self.onmessage = async (e) => {
  const result = await processData(e.data);
  self.postMessage(result);
};
```

2. Configure worker build options separately from the main build:

```javascript
// vite.config.js
export default defineConfig({
  worker: {
    format: 'es',
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].[hash].js'
      }
    }
  }
});
```

3. Use `new Worker` with the correct constructor options:

```javascript
const worker = new Worker(new URL('./worker.js', import.meta.url), {
  type: 'module'
});
```

4. Check that imported assets in the worker are supported:

```javascript
// Worker importing assets -- use explicit URLs
const wasmUrl = new URL('./worker.wasm', import.meta.url).href;
```

## Examples

```bash
# Error output
[vite] Worker build failed: Cannot use import statement outside a module
```

```javascript
// vite.config.js with worker configuration
export default defineConfig({
  worker: {
    format: 'es',
    plugins: () => [vue()],
    rollupOptions: {
      external: ['some-external']
    }
  }
});
```

```javascript
// Correct worker instantiation in main thread
const worker = new Worker(
  new URL('./processors/data-processor.js', import.meta.url),
  { type: 'module' }
);
```

## Related Errors

- [Worker Import]({{< relref "/tools/vite/worker-import" >}}) -- worker import resolution issues
- [Build Error]({{< relref "/tools/vite/build-error7" >}}) -- general build failures
- [Plugin Error]({{< relref "/tools/vite/plugin-error" >}}) -- plugin configuration issues
