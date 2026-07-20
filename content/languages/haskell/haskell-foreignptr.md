---
title: "[Solution] Haskell ForeignPtr — Foreign Pointer Errors"
description: "Fix ForeignPtr errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1027
---

`ForeignPtr` wraps raw C pointers with automatic garbage collection. Errors involve using a finalized pointer after its finalizer runs, incorrect alignment, or mismatched `Storable` types.

## Common Causes

- Dereferencing a `ForeignPtr` after its finalizer has run
- Using the wrong `Storable` type when casting
- Forgetting `mallocForeignPtr` vs `mallocForeignPtrArray`
- Accessing freed memory due to incorrect `withForeignPtr` usage

## How to Fix

### 1. Use withForeignPtr to safely access the pointer

```haskell
import Foreign.ForeignPtr
import Foreign.Ptr
import Foreign.Storable

readVal :: ForeignPtr Int -> IO Int
readVal fptr = withForeignPtr fptr $ \ptr -> peek ptr
```

### 2. Allocate with the correct function

```haskell
import Foreign.ForeignPtr
import Foreign.Storable

-- Single value
fptr <- mallocForeignPtr :: IO (ForeignPtr Int)

-- Array of n values
fptr <- mallocForeignPtrArray 10 :: IO (ForeignPtr Int)
```

### 3. Finalize pointers properly

```haskell
import Foreign.ForeignPtr

-- ForeignPtr automatically calls finalizer when GC'd
-- You can also add a finalizer explicitly
fptr <- mallocForeignPtr
addForeignPtrFinalizer freeForeignPtr fptr
```

### 4. Cast pointers carefully

```haskell
import Foreign.ForeignPtr
import Foreign.Ptr

castFPtr :: ForeignPtr Int -> ForeignPtr Double
castFPtr = castForeignPtr
```

### 5. Use withForeignPtr for the entire lifetime of the access

```haskell
import Foreign.ForeignPtr
import Foreign.Storable

copyData :: ForeignPtr Int -> ForeignPtr Int -> Int -> IO ()
copyData src dst n = do
  withForeignPtr src $ \sptr ->
    withForeignPtr dst $ \dptr ->
      copyBytes dptr sptr (n * sizeOf (undefined :: Int))
```

## Examples

Allocating and writing a C-compatible buffer:

```haskell
import Foreign.ForeignPtr
import Foreign.Storable
import Foreign.Marshal.Array (withArray)

writeBuffer :: [Int] -> IO (ForeignPtr Int)
writeBuffer xs = do
  fptr <- mallocForeignPtrArray (length xs)
  withForeignPtr fptr $ \ptr -> pokeArray ptr xs
  return fptr
```

## Related Errors

- [Haskell Storable Error](../haskell-storable)
- [Haskell FFI Import Error](../haskell-ffi-import)
- [Haskell Marshal Error](../haskell-marshal)
