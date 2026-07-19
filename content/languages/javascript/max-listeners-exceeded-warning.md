---
title: "[Solution] MaxListenersExceeded Warning — Possible Memory Leak Fix"
description: "Fix MaxListenersExceeded warning when too many listeners are added to an EventEmitter. Remove unused listeners."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# MaxListenersExceeded Warning

More than 10 (default) listeners added to a single EventEmitter.

## Fix

```javascript
// Remove listeners when done
const handler = () => { ... };
emitter.on('event', handler);
// Later:
emitter.removeListener('event', handler);

// Or increase limit if intentional
emitter.setMaxListeners(50);
```

## Detect Leaks

```javascript
const emitter = require('events');
emitter.defaultMaxListeners = 20; // increase warning threshold
```
