---
title: "[Solution] JavaScript Vue.js Runtime Error — How to Fix"
description: "Fix JavaScript Vue.js template compilation, reactivity system, component lifecycle, v-model binding, and computed property errors."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 801
---

# JavaScript Vue.js Runtime Error

A `VueError` or `TypeError` occurs when Vue's template compiler fails, the reactivity system cannot track dependencies, lifecycle hooks throw, v-model bindings mismatch, or computed properties have circular dependencies.

## Why It Happens

Vue's reactive system depends on proper property initialization and hook ordering. Errors arise from invalid template syntax, accessing reactive data outside setup, incorrect lifecycle usage, type mismatches in v-model, or computed properties that mutate dependencies.

## Common Error Messages

- `TypeError: Cannot read properties of undefined (reading 'xxx')`
- `VueCompilerError: Invalid expression`
- `Error: Maximum recursive updates exceeded`
- `Vue warn: Property or method "xxx" is not defined`
- `Error: v-model value must be a valid property`

## How to Fix It

### Fix 1: Initialize reactive data properly

```vue
<script setup>
import { ref, reactive } from 'vue'

// ❌ Wrong - accessing reactive before init
// console.log(count.value) // undefined

// ✅ Correct - initialize with default value
const count = ref(0)
const user = reactive({ name: '', age: 0 })
</script>
```

### Fix 2: Use computed properties without side effects

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([1, 2, 3])

// ❌ Wrong - mutating inside computed
// const doubled = computed(() => items.value.push(4))

// ✅ Correct - pure computation
const doubled = computed(() => items.value.map(n => n * 2))
</script>
```

### Fix 3: Correct v-model binding

```vue
<template>
  <!-- ❌ Wrong - mismatched v-model -->
  <!-- <input v-model="user.age"> -->

  <!-- ✅ Correct - ensure property exists -->
  <input v-model="user.name">
  <input v-model.number="user.age">
</template>

<script setup>
import { reactive } from 'vue'
const user = reactive({ name: '', age: 0 })
</script>
```

### Fix 4: Lifecycle hook order

```vue
<script setup>
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  console.log('Component mounted')
})

// ❌ Wrong - using destroyed instead of unmounted
// onDestroyed(() => {})

// ✅ Correct
onUnmounted(() => {
  cleanup()
})
</script>
```

## Examples

Real-world Vue reactive error when accessing deeply nested properties:

```vue
<template>
  <p>{{ user.profile.bio }}</p>
</template>

<script setup>
import { reactive, computed } from 'vue'

const user = reactive({})

// ❌ user.profile is undefined - causes TypeError
// ✅ Fix with optional chaining or defaults
const bio = computed(() => user.profile?.bio ?? 'No bio')
</script>
```

## Related Errors

- [Vue Router Error](/languages/javascript/vue-router-error)
- [Nuxt Error](/languages/javascript/nuxt-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
