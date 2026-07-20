---
title: "[Solution] JavaScript Nuxt.js Runtime Error — How to Fix"
description: "Fix JavaScript Nuxt.js server-side rendering errors, module configuration issues, layout nesting problems, and Universal/SPA mode conflicts."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 810
---

# JavaScript Nuxt.js Runtime Error

A `NuxtError`, `TypeError`, or `VueError` occurs when Nuxt.js encounters SSR hydration mismatches, modules fail to register, layout nesting is invalid, or runtime configuration is missing for the target mode.

## Why It Happens

Nuxt errors arise from missing `asyncData` return values, Vue component hydration mismatches between server and client, incompatible or misconfigured modules, incorrect `nuxt.config` settings for `ssr`/`target`, and duplicate layout nesting.

## Common Error Messages

- `Error: [nuxt] asyncData must return a plain object`
- `Error: Hydration completed but contains mismatches`
- `Error: Module 'xxx' is not compatible with Nuxt 3`
- `Error: Cannot find layout 'default'`
- `Error: Nuxt build error: document is not defined`

## How to Fix It

### Fix 1: asyncData must return object

```vue
<script setup>
// ❌ Wrong - returning array
// const { data } = await useFetch('/api/users')
// return data

// ✅ Correct - return plain object
const { data: users } = await useFetch('/api/users')
</script>
```

### Fix 2: Configure modules correctly

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  // ❌ Wrong - string instead of object with options
  // modules: ['@nuxtjs/tailwindcss']

  // ✅ Correct
  modules: [
    '@nuxtjs/tailwindcss',
    ['@nuxtjs/robots', { UserAgent: '*', Disallow: '/admin' }]
  ]
})
```

### Fix 3: SSR vs SPA mode

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  // ❌ Wrong - conflicting settings
  // ssr: false,
  // target: 'static'

  // ✅ Correct
  ssr: true,           // Universal mode (SSR + hydration)
  // ssr: false,       // SPA mode (no SSR)

  // or for static generation
  // ssr: true,
  // target: 'static'  // pre-rendered static site
})
```

### Fix 4: Layout nesting

```vue
<!-- layouts/default.vue -->
<template>
  <!-- ❌ Wrong - missing NuxtPage -->
  <!-- <div> -->
  <!--   <Header /> -->
  <!-- </div> -->

  <!-- ✅ Correct -->
  <div>
    <Header />
    <NuxtPage />
    <Footer />
  </div>
</template>
```

## Examples

Handle hydration mismatch with ClientOnly:

```vue
<template>
  <div>
    <p>Server and client rendered: {{ name }}</p>

    <!-- ✅ Wrap browser-only content -->
    <ClientOnly>
      <BrowserFeature />
      <template #fallback>
        <p>Loading browser feature...</p>
      </template>
    </ClientOnly>
  </div>
</template>
```

## Related Errors

- [Vue Error](/languages/javascript/vue-error)
- [JavaScript SSR Error](/languages/javascript/js-ssr-error)
- [JavaScript Hydration Error](/languages/javascript/js-hydration-error)
