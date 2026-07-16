---
title: "[Solution] TypeScript Member Not Found in Enum — Enum Value Access Fix"
description: "Fix TypeScript 'Member not found in enum' errors. Understand enum reverse mappings, string enums, and proper enum value access."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["enum-error", "enum", "member-not-found", "string-enum", "reverse-mapping"]
weight: 5
---

# TypeScript: Member not found in enum

This error occurs when you try to access a member on an enum value that doesn't exist, or when you try to use a string enum value as a number enum, or access an enum via bracket notation with an invalid key.

## Common Causes

- **Typo in enum member name** — accessing `Color.Reed` instead of `Color.Red`
- **Using numeric enum value as key** — trying to access `Color[2]` when only values 0 and 1 exist
- **String enum accessed as numeric** — string enums don't support reverse mapping
- **Accessing enum member that was removed** — refactoring removed a member but references remain

## How to Fix

```typescript
// Cause 1: Typo in member name
enum Color {
  Red = "red",
  Green = "green",
  Blue = "blue",
}

const c = Color.Reed;  // TS2339: Property 'Reed' does not exist on typeof Color

// Fix: check the correct name
const c = Color.Red;

// Cause 2: Numeric enum — invalid key access
enum Direction {
  Up,    // 0
  Down,  // 1
  Left,  // 2
}

const name = Direction[3];  // TS7053: Element implicitly has an 'any' type — no index 3

// Fix: only access valid numeric keys
const name = Direction[0];  // "Up"

// Cause 3: String enum reverse mapping doesn't work
enum Status {
  Active = "active",
  Inactive = "inactive",
}

const key = Status.Active;  // "active"
const reverse = Status["active"];  // TS2339: doesn't work with string enums

// Fix: use Record or string lookup
const reverseMap: Record<string, keyof typeof Status> = {
  active: "Active",
  inactive: "Inactive",
};
```

## Examples

```typescript
// Example 1: Iterating enum members
enum Fruit {
  Apple = "apple",
  Banana = "banana",
  Cherry = "cherry",
}

// Get all values
const values = Object.values(Fruit);  // ["apple", "banana", "cherry"]

// Get all keys
const keys = Object.keys(Fruit);  // ["Apple", "Banana", "Cherry"]

// Example 2: Type-safe enum check
function processColor(color: Color): void {
  switch (color) {
    case Color.Red:
      console.log("Red");
      break;
    case Color.Green:
      console.log("Green");
      break;
    case Color.Blue:
      console.log("Blue");
      break;
    default:
      const _exhaustive: never = color;  // compile error if case is missing
  }
}

// Example 3: Enum as object key
const config: Record<Status, string> = {
  [Status.Active]: "Config for active",
  [Status.Inactive]: "Config for inactive",
};
```

## Related Errors

- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339" >}}) — general property access on type
- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — enum value assigned to wrong type
- [TS2749: Referenced value is not a class]({{< relref "/languages/typescript/ts2749" >}}) — enum used as a class
