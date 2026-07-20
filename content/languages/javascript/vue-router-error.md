---
title: "[Solution] JavaScript Vue Router Navigation Error — How to Fix"
description: "Fix JavaScript Vue Router route configuration, navigation guard, dynamic routing, and hash/history mode errors."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 802
---

# JavaScript Vue Router Navigation Error

A `NavigationFailure`, `TypeError`, or `RangeError` occurs when Vue Router encounters invalid route definitions, navigation guards throw, dynamic route segments mismatch, or the router mode is misconfigured.

## Why It Happens

Vue Router errors arise from duplicate named routes, guards that do not call `next()`, async route resolution failures, missing params in dynamic routes, and hash/history mode server configuration issues.

## Common Error Messages

- `NavigationDuplicated: Avoided redundant navigation to current location`
- `TypeError: Cannot read properties of undefined (reading 'params')`
- `Error: Route with name 'xxx' already exists`
- `Uncaught (in promise): Error: Redirected when going from "/a" to "/b"`
- `Error: No match found for location with path`

## How to Fix It

### Fix 1: Proper route configuration

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('./User.vue'),
    // ❌ Wrong - missing props
    // ✅ Correct
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
```

### Fix 2: Navigation guards must call next()

```javascript
// ❌ Wrong - missing next() causes infinite loop
// router.beforeEach((to, from) => {
//   if (to.path === '/admin') {
//     // forgot to call next()
//   }
// })

// ✅ Correct
router.beforeEach((to, from, next) => {
  if (to.path === '/admin' && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})
```

### Fix 3: Dynamic route params

```vue
<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

// ❌ Wrong - accessing param before route resolved
// const id = route.params.id

// ✅ Correct
const id = computed(() => route.params.id)

function navigate() {
  router.push({ name: 'User', params: { id: 123 } })
}
</script>
```

### Fix 4: Hash vs History mode

```javascript
// ❌ Wrong - history mode without server config
// export default createRouter({
//   history: createWebHistory(),
//   routes
// })

// ✅ Correct for production - use hash mode or configure server
const router = createRouter({
  history: createWebHashHistory(), // simpler for static hosting
  routes
})
```

## Examples

Dynamic route matching with optional segments:

```javascript
const routes = [
  // ❌ Wrong order - /user/new matches :id first
  // { path: '/user/:id', component: User },
  // { path: '/user/new', component: NewUser },

  // ✅ Correct - specific before dynamic
  { path: '/user/new', component: NewUser },
  { path: '/user/:id', component: User }
]
```

## Related Errors

- [Vue Error](/languages/javascript/vue-error)
- [Nuxt Error](/languages/javascript/nuxt-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
