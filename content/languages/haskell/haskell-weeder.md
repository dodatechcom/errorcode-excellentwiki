---
title: "[Solution] Haskell Weeder — Dead Code Detection Errors"
description: "Fix weeder errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["style"]
severities: ["warning"]
weight: 1038
---

Weeder finds unused code in Haskell projects by analyzing import graphs and exports. Errors involve incorrect `.weeder.dhall` configuration, false positives from TH-generated code, or missing root declarations.

## Common Causes

- Missing or incorrect root module configuration in `.weeder.dhall`
- Weeder reports false positives for Template Haskell-generated code
- The weeder version does not match the project's GHC version
- Import graphs are incomplete because of cabal build issues

## How to Fix

### 1. Create a proper .weeder.dhall configuration

```dhall
-- .weeder.dhall
{ roots = [ "Main.main", "Lib.exportedFunction" ]
, type-class-roots = True
}
```

### 2. Run weeder after a clean build

```bash
cabal build all
weeder --test
```

### 3. Exclude TH-generated code

```dhall
-- .weeder.dhall
{ roots = [ "Main.main" ]
, type-class-roots = True
, ignore = [ "MyModule.generatedFunction" ]
}
```

### 4. Check weeder version compatibility

```bash
weeder --version
# Use a version compatible with your GHC
```

### 5. Use weeder with Stack

```bash
stack build --test
weeder --test --stack
```

## Examples

Basic weeder workflow:

```bash
# 1. Build everything
cabal build all

# 2. Run weeder
weeder

# 3. Check results
# Output lists unused functions and modules

# 4. Remove or export unused code
```

A complete weeder config:

```dhall
-- .weeder.dhall
{ roots =
    [ "Main.main"
    , "Lib.publicAPI"
    , "Test.suite"
    ]
, type-class-roots = True
, ignore =
    [ "Gen.arbitrary"  -- used by QuickCheck
    ]
}
```

## Related Errors

- [Haskell HLint Error](../haskell-hlint)
- [Haskell GHCid Error](../haskell-ghcid)
- [Haskell Dead Code Warning](../haskell-dead-code)
