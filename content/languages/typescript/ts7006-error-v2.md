---
title: "[Solution] TypeScript TS7006 v2 — Parameter Implicitly Has Any Type Fix"
description: "Fix TypeScript TS7006 when function parameters lack type annotations. Handle callbacks, event handlers, and higher-order functions."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# TS7006 — Parameter Implicitly Has Any Type (v2)

This variant covers TS7006 errors in callback chains, event handlers, higher-order functions, and destructured parameters where the implicit `any` is harder to infer or annotate.

## What This Error Means

Common error messages:

- `TS7006: Parameter 'e' implicitly has an 'any' type`
- `TS7006: Parameter 'err' implicitly has an 'any' type`
- `TS7006: Parameter 'item' implicitly has an 'any' type`
- `TS7006: Parameter 'data' implicitly has an 'any' type`

When `noImplicitAny` is enabled (recommended), TypeScript requires all parameters to have explicit types. This catches many runtime errors at compile time.

## Common Causes

```typescript
// Cause 1: Event handler callback
element.addEventListener('click', (e) => { // TS7006
  console.log(e.clientX);
});

// Cause 2: Promise chain
fetchData()
  .then((data) => { // TS7006
    return data.json();
  })
  .then((json) => { // TS7006
    console.log(json);
  });

// Cause 3: Array method callback
numbers.map((n) => n * 2); // TS7006 if numbers is any[]

// Cause 4: Destructured parameter
function process({ name, age }) { // TS7006 for both
  return `${name} is ${age}`;
}

// Cause 5: Higher-order function
function withLogging(fn) { // TS7006
  return (...args) => fn(...args);
}
```

## How to Fix

### Fix 1: Annotate callback parameters

```typescript
element.addEventListener('click', (e: MouseEvent) => {
  console.log(e.clientX);
});
```

### Fix 2: Type promise chain parameters

```typescript
interface ApiResponse {
  users: User[];
}

fetchData()
  .then((res: Response) => res.json())
  .then((json: ApiResponse) => {
    console.log(json.users);
  });
```

### Fix 3: Type array callbacks from inferred context

```typescript
// If array is properly typed, callback is inferred
const numbers: number[] = [1, 2, 3];
numbers.map((n) => n * 2); // n is inferred as number
```

### Fix 4: Annotate destructured parameters

```typescript
interface Person {
  name: string;
  age: number;
}

function process({ name, age }: Person) {
  return `${name} is ${age}`;
}
```

### Fix 5: Type higher-order functions with generics

```typescript
function withLogging<T extends (...args: any[]) => any>(fn: T): T {
  return (...args: Parameters<T>): ReturnType<T> => {
    console.log('Calling:', fn.name);
    return fn(...args);
  };
}
```

## Examples

```typescript
// Error with deeply nested callbacks
fetch('/api')
  .then((res) => res.json())
  .then((data) => {
    return data.users.map((user) => user.name);
  })
  .then((names) => console.log(names));
```

```typescript
// Fix: annotate the entry point or let inference flow
interface Data { users: { name: string }[]; }

fetch('/api')
  .then((res: Response) => res.json() as Promise<Data>)
  .then((data) => data.users.map((user) => user.name))
  .then((names) => console.log(names));
```

## Related Errors

- [TS7006]({{< relref "/languages/typescript/ts7006" >}}) — basic TS7006
- [TS7031]({{< relref "/languages/typescript/ts7031" >}}) — binding element implicitly has any type
- [TS2345]({{< relref "/languages/typescript/ts2345" >}}) — argument type mismatch
