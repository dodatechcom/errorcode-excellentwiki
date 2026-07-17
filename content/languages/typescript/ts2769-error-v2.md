---
title: "[Solution] TypeScript TS2769 v2 — No Overload Matches This Call Fix"
description: "Fix TypeScript TS2769 when function overloads or generic calls don't match any provided signature. Handle overloaded APIs and discriminated unions."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["ts2769", "overload", "generic", "function-call", "discriminated-union"]
weight: 5
---

# TS2769 — No Overload Matches This Call (v2)

This variant of TS2769 covers complex overload failures involving overloaded functions from libraries like React, Express, or DOM APIs where the combination of arguments doesn't match any available signature.

## What This Error Means

Common error messages:

- `TS2769: No overload matches this call. Overload 1 of 12 ...`
- `TS2769: No overload matches this call. The last overload ...`
- `TS2769: No overload matches this call. Expected 2 arguments, but got 3`

A function has multiple call signatures (overloads). TypeScript checks each one and finds that none match the arguments you provided. The error lists all available overloads.

## Common Causes

```typescript
// Cause 1: React.createElement with wrong props
createElement('div', { className: 'box' }, children); // wrong children type

// Cause 2: DOM method with wrong argument types
const el = document.querySelector('input');
el.addEventListener('click', (e: KeyboardEvent) => {}); // TS2769: expects MouseEvent

// Cause 3: Array.reduce without initial value
const nums: string[] = ['1', '2'];
nums.reduce((acc, val) => acc + Number(val)); // TS2769

// Cause 4: Overloaded library function
declare function createServer(
  opts: ServerOptions
): Server;
createServer({ port: 3000, host: 123 }); // TS2769: host should be string

// Cause 5: React setState with wrong argument shape
const [state, setState] = useState<{ count: number }>({ count: 0 });
setState({ total: 0 }); // TS2769
```

## How to Fix

### Fix 1: Match the correct overload signature

```typescript
// Check the function's type definition to see valid overloads
import { createElement, FC } from 'react';

// Ensure children type matches element type
const el = createElement('div', { className: 'box' }, 'Hello');
```

### Fix 2: Use correct event types

```typescript
el.addEventListener('click', (e: MouseEvent) => {
  console.log(e.clientX);
});
```

### Fix 3: Provide initial value to reduce

```typescript
nums.reduce((acc, val) => acc + Number(val), 0); // explicit initial value
```

### Fix 4: Match the library's expected types

```typescript
import { createServer, ServerOptions } from 'http';

const opts: ServerOptions = {
  port: 3000,
  host: 'localhost', // string, not number
};
createServer(opts);
```

### Fix 5: Use discriminated unions for setState

```typescript
type State = { count: number } | { total: number };
const [state, setState] = useState<State>({ count: 0 });
setState({ count: state.count + 1 }); // match the shape
```

## Examples

```typescript
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  return value;
}

process(true); // TS2769: no overload matches boolean
```

```typescript
// Fix: add another overload for boolean
function process(value: string): string;
function process(value: number): number;
function process(value: boolean): boolean;
function process(value: string | number | boolean): string | number | boolean {
  return value;
}

process(true); // now works
```

## Related Errors

- [TS2769]({{< relref "/languages/typescript/ts2769" >}}) — basic TS2769
- [TS2345]({{< relref "/languages/typescript/ts2345" >}}) — argument type mismatch
- [TS2322]({{< relref "/languages/typescript/ts2322" >}}) — type not assignable
