---
title: "[Solution] Haskell: module not imported or import error"
description: "Fix Haskell import errors by verifying module names, exports, and qualified import paths."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Haskell import error occurs when the compiler encounters an import statement that references a module it cannot find, or when a name is used that has not been imported into the current module's scope. The error may read `Module X is not imported` or `Not in scope: X`. Haskell requires explicit imports for names defined in other modules, with the exception of the Prelude which is imported automatically. Even with Prelude imported, specific names can be hidden or the module can be redefined entirely.

## Why It Happens

Import errors happen for several reasons. The module name in the import statement may be misspelled or may not match the actual module name defined in the package. The module might exist but does not export the specific name you are trying to use, since Haskell modules have explicit export lists. You may have imported a module but used a `qualified` import and then tried to use the name without the qualifier prefix. Another common cause is using `import Module hiding (something)` and then trying to use the hidden name. Package dependencies might not be installed, preventing the module from being found on the include path. The Prelude itself can be hidden or replaced with a custom prelude, removing standard names from scope.

## How to Fix It

**Verify the module name is correct:**

```haskell
-- WRONG: misspelled module name
-- import Data.Mpa

-- CORRECT:
import Data.Map
```

**Check what the module exports:**

```haskell
-- If Module A has:
module A (foo, bar) where
foo = 1
bar = 2
baz = 3  -- not exported

-- Then in Module B:
import A
-- foo and bar are available
-- baz causes: Not in scope: baz
```

**Fix qualified import usage:**

```haskell
-- WRONG: using unqualified name from qualified import
-- import qualified Data.Map as M
-- result = empty  -- Not in scope: empty

-- CORRECT: use the qualifier prefix
import qualified Data.Map as M
result = M.empty
```

**Handle hidden imports:**

```haskell
-- WRONG: trying to use hidden name
-- import Prelude hiding (length)
-- xs = length [1, 2, 3]  -- Not in scope: length

-- CORRECT: either do not hide it or import from alternative
import Prelude hiding (length)
import Data.List (length)
xs = length [1, 2, 3]
```

**Use explicit imports for clarity:**

```haskell
-- Instead of importing everything
-- import Data.Map

-- Import only what you need
import Data.Map (Map, fromList, lookup, insert)
```

**Fix import path issues in cabal or stack:**

```bash
# Ensure exposed-modules lists your module
cabal build
# Check the package database
ghc-pkg find-module MyModule
```

## Common Mistakes

- Forgetting that `import qualified` requires the module prefix on all names
- Not realizing that hiding one name does not affect other names from the same module
- Confusing module names with package names (e.g., `containers` package contains `Data.Map`)
- Assuming `import Module (foo)` also imports types and constructors used by `foo`
- Not recompiling after changing the export list of a local module

## Related Pages

- [Module not found in Haskell](/languages/haskell/haskell-module-not-found-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Parse error in Haskell](/languages/haskell/haskell-parse-error-new)
