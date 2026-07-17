---
title: "[Solution] Haskell 'No Instance for' Error — Missing Typeclass Instance"
description: "Fix Haskell 'No instance for' typeclass errors. Learn why the compiler can't find an instance and how to provide or derive one."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# No Instance for — Missing Typeclass Instance

A `No instance for (Typeclass Type)` error occurs when the Haskell compiler cannot find a typeclass instance for a given type. This is a compile-time error that prevents the program from building.

## Description

In Haskell, typeclasses define interfaces (like `Show`, `Eq`, `Ord`) that types can implement. When you use a function that requires a typeclass instance and the type doesn't have one, the compiler reports this error. The type either needs a derived instance, a manual instance, or the usage needs to change.

Common scenarios:

- **Using print/show on a custom type** — `Show` instance not defined.
- **Comparing custom types** — `Eq` or `Ord` instance missing.
- **Using a type in a constrained context** — a function requires `Num` but the type doesn't implement it.
- **Overloaded string literals** — `IsString` instance missing for custom types.

## Common Causes

```haskell
-- Cause 1: No Show instance for custom type
data Person = Person { name :: String, age :: Int }

-- This fails: No instance for (Show Person)
-- print (Person "Alice" 30)

-- Cause 2: No Eq instance
data Color = Red | Green | Blue

-- This fails: No instance for (Eq Color)
-- Red == Green

-- Cause 3: No Num instance where expected
data Dollars = Dollars Double

-- This fails: No instance for (Num Dollars)
-- Dollars 10 + Dollars 20

-- Cause 4: No Ord instance for sorting
-- sortBy compare [Person "Alice" 30, Person "Bob" 25]
-- Fails if Person doesn't have an Ord instance
```

## How to Fix

### Fix 1: Derive standard typeclasses automatically

```haskell
-- Wrong
data Person = Person { name :: String, age :: Int }

-- Correct — derive Show, Eq, Ord
data Person = Person { name :: String, age :: Int }
  deriving (Show, Eq, Ord)
```

### Fix 2: Write manual instances

```haskell
-- Wrong
data Dollars = Dollars Double

-- Correct — manually implement the typeclass
data Dollars = Dollars Double

instance Show Dollars where
  show (Dollars d) = "$" ++ show d

instance Eq Dollars where
  (Dollars a) == (Dollars b) = a == b

instance Num Dollars where
  (Dollars a) + (Dollars b) = Dollars (a + b)
  (Dollars a) * (Dollars b) = Dollars (a * b)
  abs (Dollars a) = Dollars (abs a)
  signum (Dollars a) = Dollars (signum a)
  fromInteger n = Dollars (fromInteger n)
  negate (Dollars a) = Dollars (negate a)
```

### Fix 3: Use newtype deriving where appropriate

```haskell
-- newtype can derive instances from the underlying type
newtype Dollars = Dollars Double
  deriving (Show, Eq, Num)
```

### Fix 4: Add constraints to function signatures

```haskell
-- Wrong — requires Show but doesn't state it
showValue x = show x

-- Correct — make the constraint explicit
showValue :: Show a => a -> String
showValue x = show x
```

## Examples

```haskell
data Temperature = Celsius Double | Fahrenheit Double

-- This fails to compile:
-- No instance for (Show Temperature)
-- main = print (Celsius 36.5)

-- Fix: add deriving
data Temperature = Celsius Double | Fahrenheit Double
  deriving (Show)

main :: IO ()
main = print (Celsius 36.5)  -- now works: Celsius 36.5
```

## Related Errors

- [pattern-match] — runtime crash from incomplete pattern matching.
- [Type mismatch] — expected and actual types don't match.
- [Variable not in scope] — referencing an undefined variable.
