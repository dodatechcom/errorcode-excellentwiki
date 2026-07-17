---
title: "[Solution] TypeScript TS18046 — Variable is of type 'unknown'"
description: "Fix TypeScript TS18046: Variable is of type 'unknown'. Handle unknown types safely in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts18046", "unknown", "type-guard", "assertion", "safety"]
weight: 5
---

# TS18046 — Variable is of type 'unknown'

TS18046 occurs when you try to use a value of type `unknown` in a way that requires a more specific type. `unknown` is the type-safe counterpart of `any` — you must narrow it before use.

## Common Causes

```typescript
// Cause 1: catch clause variable is unknown
try {
  throw new Error("oops");
} catch (e) {
  console.log(e.message); // TS18046: e is 'unknown'
}

// Cause 2: JSON.parse returns unknown
const data = JSON.parse('{"name": "Alice"}');
console.log(data.name); // TS18046

// Cause 3: Function returning unknown
function parse(input: string): unknown {
  return JSON.parse(input);
}
const result = parse("{}");
result.foo; // TS18046
```

## How to Fix

### Fix 1: Type guard

```typescript
try {
  throw new Error("oops");
} catch (e) {
  if (e instanceof Error) {
    console.log(e.message); // OK
  }
}
```

### Fix 2: Type assertion

```typescript
const data = JSON.parse('{"name": "Alice"}') as { name: string };
console.log(data.name);
```

### Fix 3: Define a return type

```typescript
function parse(input: string): { name: string } {
  return JSON.parse(input);
}
```

### Fix 4: Use a validation library

```typescript
import { z } from "zod";
const schema = z.object({ name: z.string() });
const data = schema.parse(JSON.parse(input));
```

## Related Errors

- [TS7006: Parameter implicitly has 'any' type]({{< relref "/languages/typescript/ts7006-parameter" >}}) — any type instead of unknown.
- [TS2571: Object is of type 'unknown']({{< relref "/languages/typescript/ts2571-unknown" >}}) — object unknown variant.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — unresolved identifier.
