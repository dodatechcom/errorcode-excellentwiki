---
title: "Vite Asset Import Error"
description: "Vite fails to resolve or process asset file imports."
tools: ["vite"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Vite Asset Import Error

A Vite asset import error occurs when Vite cannot resolve or process imported asset files like images, fonts, or other static resources.

## Common Causes

- Asset file does not exist at the specified path
- Incorrect import path (relative or absolute)
- Asset not included in the build
- Missing asset configuration in vite.config

## How to Fix

### Check Asset Path

```bash
ls -la src/assets/logo.png
```

### Use Correct Import Syntax

```javascript
// Static asset import
import logo from './assets/logo.png';

// Dynamic asset import
const imagePath = new URL('./assets/image.png', import.meta.url).href;

// In template
<img src={new URL('./assets/logo.png', import.meta.url).href} />
```

### Configure Asset Handling

```javascript
// vite.config.js
export default defineConfig({
  build: {
    assetsDir: 'assets',
    assetsInlineLimit: 4096, // inline files < 4KB as base64
  },
});
```

### Include Assets Directory

```bash
# Ensure assets directory is in the project root or src/
ls src/assets/
```

### Fix Dynamic Import Paths

```javascript
// Use import.meta.glob for dynamic imports
const images = import.meta.glob('./assets/*.{png,jpg,jpeg}', { eager: true });

// Or use new URL()
const imageUrl = new URL(`./assets/${filename}.png`, import.meta.url).href;
```

## Examples

```javascript
// Error: Cannot find module './assets/logo.png'
import logo from './assets/logo.png';
// Fix: ensure file exists at the specified path

// Error: The "glob" pattern "./assets/*.svg" didn't match any files
const svgs = import.meta.glob('./assets/*.svg');
// Fix: check file extensions and paths
```

## Related Errors

- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
- [CSS Error]({{< relref "/tools/vite/vite-css-error" >}}) — CSS processing error
- [Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
