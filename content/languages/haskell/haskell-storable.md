---
title: "[Solution] Haskell Storable — Storable Typeclass Errors"
description: "Fix Storable instance errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1028
---

The `Storable` typeclass defines how Haskell types are represented in memory for FFI interop. Errors involve missing instances, wrong `sizeOf` or `alignment`, or undefined behavior from incorrect `peek`/`poke` implementations.

## Common Causes

- Missing `Storable` instance for a type used with FFI
- Wrong `sizeOf` returning an incorrect byte count
- Incorrect `peek`/`poke` implementation causing memory corruption
- Using `ForeignPtr` with a type that lacks a `Storable` instance

## How to Fix

### 1. Derive or define Storable for your types

```haskell
{-# LANGUAGE DeriveGeneric #-}

import Foreign.Storable
import GHC.Generics

data Point = Point Double Double
  deriving (Generic)

instance Storable Point where
  sizeOf _ = 2 * sizeOf (undefined :: Double)
  alignment _ = alignment (undefined :: Double)
  poke ptr (Point x y) = do
    pokeByteOff ptr 0 x
    pokeByteOff ptr (sizeOf (undefined :: Double)) y
  peek ptr = do
    x <- peekByteOff ptr 0
    y <- peekByteOff ptr (sizeOf (undefined :: Double))
    return (Point x y)
```

### 2. Check sizeOf matches the C struct layout

```haskell
import Foreign.Storable

-- Verify: sizeOf (undefined :: Double) == 8 on most platforms
-- sizeOf (undefined :: Int) == 4 or 8 depending on architecture
```

### 3. Use genericStorable for simple product types

```haskell
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}

import GHC.Generics (Generic)
import Foreign.Storable (Storable)

newtype MyInt = MyInt Int
  deriving (Show, Generic, Storable)
```

### 4. Use pokeByteOff and peekByteOff for struct-like layouts

```haskell
import Foreign.Storable

writePair :: Ptr (Int, Int) -> (Int, Int) -> IO ()
writePair ptr (a, b) = do
  pokeByteOff ptr 0 a
  pokeByteOff ptr (sizeOf a) b
```

### 5. Use allocaBytes for stack allocation

```haskell
import Foreign.Storable
import Foreign.Marshal.Alloc (allocaBytes)

example :: IO Int
example = allocaBytes 64 $ \ptr -> do
  poke ptr (42 :: Int)
  peek ptr
```

## Examples

A Storable instance for a C-compatible struct:

```haskell
import Foreign.Storable

data Header = Header
  { headerMagic :: Int
  , headerVersion :: Int
  , headerFlags :: Int
  }

instance Storable Header where
  sizeOf _ = 3 * sizeOf (undefined :: Int)
  alignment _ = alignment (undefined :: Int)
  poke ptr (Header m v f) = do
    pokeByteOff ptr 0 m
    pokeByteOff ptr (sizeOf (undefined :: Int)) v
    pokeByteOff ptr (2 * sizeOf (undefined :: Int)) f
  peek ptr = Header
    <$> peekByteOff ptr 0
    <*> peekByteOff ptr (sizeOf (undefined :: Int))
    <*> peekByteOff ptr (2 * sizeOf (undefined :: Int))
```

## Related Errors

- [Haskell ForeignPtr Error](../haskell-foreignptr)
- [Haskell FFI Import Error](../haskell-ffi-import)
- [Haskell Marshal Error](../haskell-marshal)
