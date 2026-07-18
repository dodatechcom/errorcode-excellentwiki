---
title: "[Solution] Haskell: variable not in scope error"
description: "Resolve Haskell variable not in scope errors by checking imports, exports, and lexical scoping rules."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `Variable not in scope` error in Haskell means the compiler cannot find a reference to a particular name in the current lexical environment. Haskell has strict scoping rules, and every variable, function, or operator must be visible at the point where it is used. The error message typically reads `Variable not in scope: someName :: Type`, indicating that the identifier was not declared, imported, or is otherwise inaccessible in the current module.

## Why It Happens

This error has several common root causes. The most frequent is a simple typo in a variable or function name. Haskell is case-sensitive, so `myFunc` and `myfunc` are different identifiers. Another cause is referencing a name that is defined in a different module but has not been imported. Even if a module is imported, the name might not be exported from that module. You may also encounter this error when using a variable from an inner scope in an outer scope, since Haskell does not allow referencing locally bound variables outside their defining `let` or `where` block. Shadowing, where a local binding hides an outer one of the same name, can also lead to confusion and apparent scope errors. Finally, attempting to use a type constructor as a value or vice versa can produce misleading scope errors.

## How to Fix It

**Check for typos** by reviewing the exact spelling and capitalization:

```haskell
-- WRONG: typo in function name
main = prinlt "hello"

-- CORRECT:
main = putStrLn "hello"
```

**Add missing imports** at the top of your module:

```haskell
-- WRONG: mapM_ is not imported by default
module Main where
main = mapM_ print [1, 2, 3]

-- CORRECT: import Data.Traversable or use Prelude
module Main where
import Prelude
main = mapM_ print [1, 2, 3]
```

**Ensure the name is exported** from the defining module:

```haskell
-- Module A.hs
module A (myHelper) where  -- only myHelper is exported
myHelper = 42
secret = 99  -- not exported

-- Module B.hs
import A
x = myHelper  -- OK
-- y = secret  -- ERROR: Variable not in scope
```

**Fix scoping issues with where or let blocks:**

```haskell
-- WRONG: helper used outside its scope
main = helper
  where
    helper = putStrLn "hi"

-- This is actually correct. WRONG would be:
-- helper = putStrLn "hi"
-- main = helper
-- (if helper is defined after main without where)
```

**Use GHCi to test names interactively:**

```haskell
ghci> :t map
map :: (a -> b) -> [a] -> [b]
ghci> :i Data.List.sort
-- check if sort is available
```

## Common Mistakes

- Confusing `print` with `putStrLn` (both exist but behave differently)
- Forgetting that operator names like `++` need no import from Prelude
- Assuming all definitions in a module are automatically available
- Shadowing outer variables and then expecting the outer value inside the shadowed block
- Misspelling qualified import names like `Data.Map.lookup`

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Module not found in Haskell](/languages/haskell/haskell-module-not-found-new)
- [Import error in Haskell](/languages/haskell/haskell-import-error-new)
- [Ambiguous type variable in Haskell](/languages/haskell/haskell-ambiguous-type-new)
