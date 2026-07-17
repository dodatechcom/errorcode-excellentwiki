---
title: "IOException in Haskell"
description: "Haskell raises IOException when file, network, or I/O operations fail"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["io", "exception", "file", "network", "ioerror"]
weight: 5
---

## What This Error Means

An `IOException` occurs when an I/O operation fails due to file not found, permission denied, network errors, or other system-level failures. Haskell handles these through the `IO` monad and exception handling.

## Common Causes

- File does not exist
- Permission denied
- Disk full during write
- Network connection failed
- Invalid file path

## How to Fix

Handle IO exceptions:

```haskell
import System.IO.Error (tryIOError, isDoesNotExistError)
import Control.Exception (try, SomeException)

safeReadFile :: FilePath -> IO (Maybe String)
safeReadFile path = do
    result <- try (readFile path) :: IO (Either SomeException String)
    case result of
        Right contents -> return (Just contents)
        Left ex -> do
            putStrLn $ "Error: " ++ show ex
            return Nothing
```

Check file existence first:

```haskell
import System.Directory (doesFileExist)

readConfig :: FilePath -> IO (Maybe String)
readConfig path = do
    exists <- doesFileExist path
    if exists
        then Just <$> readFile path
        else return Nothing
```

Use `tryIOError` for specific handling:

```haskell
import System.IO.Error (tryIOError, isDoesNotExistError, isPermissionError)

safeRead :: FilePath -> IO (Either String String)
safeRead path = do
    result <- tryIOError (readFile path)
    case result of
        Right contents -> return (Right contents)
        Left e
            | isDoesNotExistError e -> return (Left "File not found")
            | isPermissionError e -> return (Left "Permission denied")
            | otherwise -> return (Left $ show e)
```

## Examples

```haskell
main = do
    contents <- readFile "nonexistent.txt"
    putStrLn contents
-- *** Exception: nonexistent.txt: No such file or directory
```

## Related Errors

- [MonadFail error]({{< relref "/languages/haskell/haskell-monad-error" >}})
- [Pattern match failure]({{< relref "/languages/haskell/pattern-match" >}})
