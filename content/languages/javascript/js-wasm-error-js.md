---
title: "[Solution] JavaScript WASM Memory Error — How to Fix"
description: "Fix JavaScript WASM memory errors. Resolve allocation, growth, and buffer issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript WASM Memory Error

A `RangeError: Out of memory` or `WebAssembly.Memory` error occurs when WebAssembly fails to allocate or grow memory, encounters buffer limits, or when shared memory is not properly configured.

## Why It Happens

WebAssembly memory is linear and must be pre-allocated. Errors arise when memory growth exceeds limits, when buffers are detached, when shared memory is used without proper configuration, or when memory is not page-aligned.

## Common Error Messages

- `RangeError: WebAssembly.Memory(): could not grow memory`
- `Error: Buffer is detached`
- `RangeError: Maximum memory size exceeded`
- `Error: SharedArrayBuffer is not defined`

## How to Fix It

### Fix 1: Configure memory properly

```javascript
// Wrong — no maximum limit
// const memory = new WebAssembly.Memory({ initial: 1 });

// Correct — set appropriate limits
const memory = new WebAssembly.Memory({
  initial: 256,   // 16MB initial
  maximum: 4096,  // 256MB maximum
  shared: false,  // set true for multi-threading
});
```

### Fix 2: Handle memory growth

```javascript
const memory = new WebAssembly.Memory({
  initial: 256,
  maximum: 4096,
});

function growMemory(pages) {
  try {
    const previousPages = memory.grow(pages);
    console.log(`Memory grew from ${previousPages} to ${previousPages + pages} pages`);
    return true;
  } catch (error) {
    console.error('Memory growth failed:', error.message);
    return false;
  }
}

growMemory(128);  // Grow by 128 pages (8MB)
```

### Fix 3: Use typed arrays

```javascript
const memory = new WebAssembly.Memory({ initial: 256 });

// Wrong — assuming buffer is always valid
// const view = new Uint8Array(memory.buffer);

// Correct — handle detached buffers
function getMemoryView() {
  try {
    return new Uint8Array(memory.buffer);
  } catch (error) {
    console.error('Buffer detached, re-creating view');
    return new Uint8Array(memory.buffer);
  }
}
```

### Fix 4: Handle shared memory

```javascript
// SharedArrayBuffer must be enabled with headers
// Cross-Origin-Opener-Policy: same-origin
// Cross-Origin-Embedder-Policy: require-corp

const memory = new WebAssembly.Memory({
  initial: 256,
  maximum: 4096,
  shared: true,
});

// Use Atomics for synchronization
Atomics.store(new Int32Array(memory.buffer), 0, 42);
console.log(Atomics.load(new Int32Array(memory.buffer), 0));
```

## Common Scenarios

- **Memory growth failed** — Module tries to allocate more than `maximum` allows.
- **Detached buffer** — Memory was grown, invalidating existing views.
- **SharedArrayBuffer not defined** — Missing COOP/COEP headers.

## Prevent It

- Set `maximum` to a reasonable limit based on expected workload.
- Re-create typed array views after memory growth.
- Ensure proper headers for shared memory support.

## Related Errors

- [RangeError](/javascript/rangeerror/) — memory limit exceeded
- [MemoryError](/javascript/memory-error/) — allocation failed
- [DetachedBuffer](/javascript/detached-buffer/) — buffer no longer valid
