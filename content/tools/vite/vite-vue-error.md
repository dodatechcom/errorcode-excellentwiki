---
title: "Vite Vue Template Compilation Error"
description: "Vite fails to compile Vue single-file component templates."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "vue", "template", "sfc", "compilation"]
weight: 5
---

# Vite Vue — Template Compilation Error

This error occurs when Vite fails to compile Vue single-file component (SFC) templates. The template syntax may be invalid or the Vue plugin may not be configured.

## Common Causes

- Vue plugin not installed or configured
- Template syntax errors
- Vue version mismatch
- Invalid v-for or v-bind syntax

## How to Fix

### Install Vue Plugin

```bash
npm install -D @vitejs/plugin-vue
```

### Configure Vue Plugin

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
});
```

### Fix Template Syntax

```vue
<!-- Wrong -->
<div v-for="item in items" :key="item.id">
  {{ item.name }
</div>

<!-- Correct -->
<div v-for="item in items" :key="item.id">
  {{ item.name }}
</div>
```

### Fix v-if/v-for Conflicts

```vue
<!-- Wrong - v-if and v-for on same element -->
<div v-for="item in items" v-if="item.active">
  {{ item.name }}
</div>

<!-- Correct -->
<template v-for="item in items" :key="item.id">
  <div v-if="item.active">{{ item.name }}</div>
</template>
```

### Check Vue Version

```bash
npm ls vue @vitejs/plugin-vue
```

## Examples

```text
[vite] Internal server error:
  Template compilation error: Element is missing end tag.
  at src/components/App.vue:15:5
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
- [Vite CSS Error]({{< relref "/tools/vite/vite-css-error" >}}) — CSS processing failure
