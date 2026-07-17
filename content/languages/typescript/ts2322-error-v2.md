---
title: "[Solution] TypeScript TS2322 v2 — Type Not Assignable to Type Fix"
description: "Fix TypeScript TS2322 when complex types, generics, or union types cause assignment failures. Handle strict mode and implicit conversions."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["ts2322", "type-assignability", "generic", "union", "strict"]
weight: 5
---

# TS2322 — Type 'X' is not assignable to type 'Y' (v2)

This variant of TS2322 covers complex assignment errors involving generics, union types, conditional types, and library-provided types where the type mismatch is less obvious.

## What This Error Means

Common error messages:

- `TS2322: Type 'string' is not assignable to type 'string[]'`
- `TS2322: Type 'number | undefined' is not assignable to type 'number'`
- `TS2322: Type 'Element' is not assignable to type 'ReactElement'`
- `TS2322: Type 'Dispatch<SetStateAction<T>>' is not assignable to type '...`

These often appear when working with React hooks, third-party library types, or when strict null checks expose hidden type mismatches.

## Common Causes

```typescript
// Cause 1: Union type assigned to narrow type
let value: string | undefined = getName();
let target: string = value; // TS2322: 'undefined' not assignable

// Cause 2: React state type mismatch
const [count, setCount] = useState<number>(0);
setCount('1'); // TS2322: 'string' not assignable to 'number'

// Cause 3: Generic inference failure
function identity<T>(arg: T): T { return arg; }
const result: string = identity(42); // TS2322

// Cause 4: Library type expectation
interface Response<T> { data: T; }
const res: Response<string> = { data: 123 }; // TS2322

// Cause 5: StrictFunctionTypes with callbacks
type Handler = (e: MouseEvent) => void;
const handler: Handler = (e: Event) => {}; // TS2322
```

## How to Fix

### Fix 1: Narrow the type before assignment

```typescript
const value: string | undefined = getName();
if (value !== undefined) {
  const target: string = value; // safe
}
```

### Fix 2: Explicitly type useState

```typescript
const [count, setCount] = useState<number>(0);
setCount(Number('1')); // convert first
```

### Fix 3: Use explicit generic type parameters

```typescript
function identity<T>(arg: T): T { return arg; }
const result = identity<string>('hello'); // explicit T
```

### Fix 4: Use type assertions for known-good values

```typescript
const res: Response<string> = { data: 123 } as unknown as Response<string>;
// Better: fix the source
const res: Response<string> = { data: String(123) };
```

### Fix 5: Use compatible callback signatures

```typescript
type Handler = (e: MouseEvent) => void;
const handler: Handler = (e: MouseEvent) => {
  console.log(e.clientX);
};
```

## Examples

```typescript
interface Config {
  host: string;
  port: number;
  debug?: boolean;
}

const config: Config = {
  host: 'localhost',
  port: '3000', // TS2322: 'string' is not assignable to 'number'
};

// Fix
const config: Config = {
  host: 'localhost',
  port: 3000,
};
```

## Related Errors

- [TS2322]({{< relref "/languages/typescript/ts2322" >}}) — basic TS2322
- [TS2345]({{< relref "/languages/typescript/ts2345" >}}) — argument type mismatch
- [TS2532]({{< relref "/languages/typescript/ts2532" >}}) — object is possibly undefined
