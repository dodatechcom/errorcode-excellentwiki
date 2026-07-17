---
title: "[Solution] TypeScript TS2722 — Cannot invoke object which is possibly 'callable'"
description: "Fix TypeScript TS2722: Cannot invoke object which is possibly 'callable'. Narrow type before calling."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2722 — Cannot invoke an object which is possibly 'callable'

TS2722 occurs when you try to call a value that might be a function but could also be `null` or `undefined`.

## Common Causes

```typescript
// Cause 1: Nullable callback
type Callback = (() => void) | null;
let cb: Callback = getCallback();
cb(); // TS2722: cb is possibly null

// Cause 2: Optional function property
interface Config {
  onError?: (err: Error) => void;
}
const config: Config = {};
config.onError(new Error("oops")); // TS2722

// Cause 3: Function from nullable source
const handler = document.getElementById("btn")?.onclick;
handler(); // TS2722
```

## How to Fix

### Fix 1: Add null check

```typescript
if (cb) {
  cb();
}
```

### Fix 2: Use optional chaining

```typescript
cb?.();
```

### Fix 3: Use non-null assertion

```typescript
cb!();
```

### Fix 4: Provide default function

```typescript
const handler = config.onError ?? (() => {});
handler(new Error("oops"));
```

## Related Errors

- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null property access.
- [TS2532: Object is possibly 'undefined']({{< relref "/languages/typescript/ts2532-object" >}}) — undefined property access.
- [TS2349: This expression is not callable]({{< relref "/languages/typescript/ts2349-not-callable" >}}) — non-callable expression.
