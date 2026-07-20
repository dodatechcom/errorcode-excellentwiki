---
title: "[Solution] Haskell FFI Import — Foreign Function Interface Errors"
description: "Fix FFI import errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1029
---

FFI imports let Haskell call C (and other foreign) functions. Errors involve wrong calling conventions, mismatched types between Haskell and C, or missing `ccall`/`stdcall` specifiers.

## Common Causes

- Missing `foreign import ccall` declaration
- Type mismatch between Haskell and C types (e.g. `CInt` vs `Int`)
- Using `unsafe` import for functions that call back into Haskell
- Forgetting to link against the C library

## How to Fix

### 1. Write the foreign import correctly

```haskell
{-# LANGUAGE ForeignFunctionInterface #-}

import Foreign.C.Types
import Foreign.C.String

foreign import ccall "strlen"
  c_strlen :: CString -> IO CSize
```

### 2. Use the correct Haskell FFI types

```haskell
import Foreign.C.Types

-- C int    -> Haskell CInt
-- C double -> Haskell CDouble
-- C char*  -> Haskell CString
-- void     -> Haskell ()
```

### 3. Use unsafe for fast, non-callback functions

```haskell
foreign import ccall unsafe "my_fast_function"
  fastFunc :: CInt -> CInt
```

### 4. Link the library in your cabal file

```cabal
executable myapp
  build-depends: base
  extra-libraries: myclib
  -- or
  pkgconfig-depends: zlib
```

### 5. Use newForeignPtr for memory management

```haskell
import Foreign.ForeignPtr
import Foreign.Ptr

foreign import ccall "&free"
  c_free :: FunPtr (Ptr a -> IO ())

allocAndUse :: IO ()
allocAndUse = do
  ptr <- mallocBytes 100
  fptr <- newForeignPtr c_free ptr
  -- use fptr safely
  return ()
```

## Examples

Calling a C math function:

```haskell
{-# LANGUAGE ForeignFunctionInterface #-}

import Foreign.C.Types

foreign import ccall "math.h sin"
  c_sin :: CDouble -> CDouble

main :: IO ()
main = print (c_sin (1.0 :: CDouble))
```

## Related Errors

- [Haskell Storable Error](../haskell-storable)
- [Haskell ForeignPtr Error](../haskell-foreignptr)
- [Haskell Marshal Error](../haskell-marshal)
