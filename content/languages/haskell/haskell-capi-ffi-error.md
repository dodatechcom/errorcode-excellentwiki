---
title: "[Solution] Haskell CApiFFI Error"
description: "Fix Haskell CApi FFI errors when using C API foreign function interface declarations."
languages: ["haskell"]
error-types: ["compile-error"]
severities: ["error"]
---

CApi FFI errors occur when foreign imports or exports use incorrect C types or calling conventions.

## Common Causes

- CApi FFI extension not enabled
- Incorrect C type in foreign import
- Calling convention mismatch
- Missing header file for C function

## How to Fix

### 1. Enable CApiFFI

```haskell
{-# LANGUAGE CApiFFI #-}

foreign import ccall safe "stdio.h fopen"
  fopen :: CString -> CString -> IO (Ptr FILE)
```

### 2. Match C types correctly

```haskell
{-# LANGUAGE CApiFFI #-}

import Foreign.C.String
import Foreign.C.Types
import Foreign.Ptr

foreign import ccall safe "stdlib.h atoi"
  c_atoi :: CString -> IO CInt
```

## Examples

```haskell
{-# LANGUAGE CApiFFI #-}

import Foreign.C.String
import Foreign.C.Types

foreign import ccall safe "stdlib.h abs"
  c_abs :: CInt -> IO CInt

main :: IO ()
main = do
  result <- c_abs (-42)
  print result
```

## Related Errors

- [FFI import error](/languages/haskell/haskell-ffi-import)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
