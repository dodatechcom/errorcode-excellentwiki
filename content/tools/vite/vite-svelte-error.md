---
title: "Vite Svelte Compilation Error"
description: "Vite fails to compile Svelte component syntax."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Svelte — Compilation Error

This error occurs when Vite fails to compile Svelte component syntax. The Svelte plugin may not be configured correctly, or the component has syntax errors.

## Common Causes

- Svelte plugin not installed or configured
- Component syntax errors
- Svelte version mismatch
- Invalid reactive declarations

## How to Fix

### Install Svelte Plugin

```bash
npm install -D @sveltejs/vite-plugin-svelte
```

### Configure Svelte Plugin

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
});
```

### Fix Component Syntax

```svelte
<!-- Wrong -->
<script>
  let count = 0;
  function increment() {
    count + 1
  }
</script>

<!-- Correct -->
<script>
  let count = 0;
  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  Count: {count}
</button>
```

### Fix Reactive Declarations

```svelte
<script>
  // Wrong - missing $ prefix for reactive
  let doubled = count * 2;

  // Correct - use $: for reactive declarations
  let count = 0;
  $: doubled = count * 2;
</script>
```

### Check Svelte Version

```bash
npm ls svelte @sveltejs/vite-plugin-svelte
```

## Examples

```text
[vite] Internal server error:
  SvelteComponent.ts:55:2: Unexpected token
  at src/App.svelte:8:2
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
