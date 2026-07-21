---
title: "[Solution] Vite SSR Bundle Error"
description: "Fix Vite SSR bundle errors when server-side rendering build fails due to module resolution or externalization issues."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite SSR Bundle Error

Vite's SSR mode bundles server-side code separately from the client. An SSR bundle error occurs when Vite cannot properly bundle or externalize modules for the server, preventing the SSR build from completing.

## Common Causes

- A dependency is not listed in `ssr.noExternal` and uses syntax incompatible with Node
- A package uses `require()` in ESM mode which causes bundling failures
- The `ssr.external` list excludes a module that Vite cannot resolve
- Node native addons like `.node` files are imported without proper handling

## How to Fix

1. Add problematic packages to `ssr.noExternal` to force bundling:

```javascript
// vite.config.js
export default defineConfig({
  ssr: {
    noExternal: ['problematic-package', 'another-package']
  }
});
```

2. Mark packages as external to skip bundling them:

```javascript
export default defineConfig({
  ssr: {
    external: ['fs', 'path', 'node-native-addon']
  }
});
```

3. Check that the entry point for SSR exists and exports correctly:

```javascript
// server entry -- must export render function
export function render(url) {
  return `<html><body>Rendered: ${url}</body></html>`;
}
```

4. Build the SSR bundle with debug output:

```bash
npx vite build --ssr src/entry-server.js --logLevel info
```

## Examples

```bash
# Build error output
error during build:
Error: Node built-in module "fs" is not bundled in SSR mode.
Add it to ssr.external or ssr.noExternal in vite.config.js.
```

```javascript
// vite.config.js with SSR configuration
export default defineConfig({
  ssr: {
    external: ['some-native-module'],
    noExternal: ['lodash-es', 'date-fns']
  },
  build: {
    rollupOptions: {
      input: {
        client: 'index.html',
        server: 'src/entry-server.js'
      }
    }
  }
});
```

## Related Errors

- [SSR Error]({{< relref "/tools/vite/ssr-error" >}}) -- general SSR failures
- [SSR Load Module]({{< relref "/tools/vite/ssrloadmodule" >}}) -- SSR module loading issues
- [SSR External]({{< relref "/tools/vite/ssr-external" >}}) -- SSR externalization problems
