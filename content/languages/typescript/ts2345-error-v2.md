---
title: "[Solution] TypeScript TS2345 v2 — Argument Type Mismatch Fix"
description: "Fix TypeScript TS2345 when passing wrong argument types to functions. Handle type coercion, generics, and callback parameter types."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# TS2345 — Argument Type Mismatch (v2)

This variant of TS2345 covers complex argument type mismatches including callback parameters, generic inference failures, and situations where the expected type is a complex mapped or conditional type.

## What This Error Means

Common error messages:

- `TS2345: Argument of type 'string' is not assignable to parameter of type 'number'`
- `TS2345: Argument of type '(x: number) => string' is not assignable to parameter of type '(x: number) => number'`
- `TS2345: Argument of type 'User' is not assignable to parameter of type 'Partial<User>'`
- `TS2345: Type '0' is not assignable to type '1'`

This error fires when you call a function with arguments whose types don't match the parameter types in the function signature.

## Common Causes

```typescript
// Cause 1: Passing wrong primitive
function greet(name: string) { return `Hello, ${name}`; }
greet(42); // TS2345

// Cause 2: Callback type mismatch
function onComplete(callback: (result: number) => void) {
  callback(42);
}
onComplete((result) => result.toString()); // TS2345: returns string, not void

// Cause 3: Array type mismatch
function process(items: string[]) {}
process([1, 2, 3]); // TS2345

// Cause 4: Generic inference from argument
function wrap<T>(value: T): T[] { return [value]; }
const result: number[] = wrap('hello'); // TS2345

// Cause 5: Object shape mismatch
interface Config { host: string; port: number; }
function connect(config: Config) {}
connect({ host: 'localhost' }); // TS2345: missing port
```

## How to Fix

### Fix 1: Convert argument types

```typescript
function greet(name: string) { return `Hello, ${name}`; }
greet(String(42)); // or greet('42')
```

### Fix 2: Match callback return type

```typescript
function onComplete(callback: (result: number) => void) {}

// Fix: don't return a value
onComplete((result) => {
  console.log(result);
  // no return needed
});
```

### Fix 3: Map values before passing

```typescript
function process(items: string[]) {}
process([1, 2, 3].map(String));
```

### Fix 4: Explicitly provide generic type

```typescript
function wrap<T>(value: T): T[] { return [value]; }
const result = wrap<number>(42); // explicit T
```

### Fix 5: Use Partial or required properties

```typescript
interface Config { host: string; port: number; }

// Option A: provide all required fields
connect({ host: 'localhost', port: 3000 });

// Option B: make config partial
function connect(config: Partial<Config> & Pick<Config, 'host'>) {}
```

## Examples

```typescript
function fetchData<T>(url: string, transform: (raw: unknown) => T): Promise<T> {
  return fetch(url).then(r => r.json()).then(transform);
}

// Error: transform returns string, but T is expected as number
const data = fetchData<number>('/api', (raw: unknown) => String(raw));
```

```typescript
// Fix: match the transform to the expected type
const data = fetchData<number>('/api', (raw: unknown) => Number(raw));
```

## Related Errors

- [TS2345]({{< relref "/languages/typescript/ts2345" >}}) — basic argument type mismatch
- [TS2322]({{< relref "/languages/typescript/ts2322" >}}) — type not assignable
- [TS2769]({{< relref "/languages/typescript/ts2769" >}}) — no overload matches this call
