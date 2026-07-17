---
title: "[Solution] Haskell IOException File Not Found"
description: "Fix Haskell IOException when file operations fail. Handle missing files, permissions, and I/O exceptions properly."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["io", "exception", "file", "ioerror", "haskell"]
weight: 5
---

## What This Error Means

An IOException in Haskell occurs when file or I/O operations fail, most commonly when a file doesn't exist. Haskell's IO monad can throw IOErrors for missing files, permission issues, and other system-level failures.

## Common Causes

- File does not exist at specified path
- Insufficient file permissions
- Directory doesn't exist
- File is already open by another process
- Incorrect file path

## How to Fix

```haskell
-- WRONG: No error handling
import System.IO

main = do
  contents <- readFile "data.txt"  -- Throws IOError if missing
  putStrLn contents

-- CORRECT: Check file existence first
import System.Directory (doesFileExist)

main = do
  exists <- doesFileExist "data.txt"
  if exists
    then do
      contents <- readFile "data.txt"
      putStrLn contents
    else putStrLn "File not found"
```

```haskell
-- WRONG: Exception not caught
import System.IO

main = do
  handle <- openFile "data.txt" ReadMode  -- May throw
  contents <- hGetContents handle
  putStrLn contents
  hClose handle

-- CORRECT: Use try or catch
import Control.Exception (try, SomeException)
import System.IO

main = do
  result <- try (readFile "data.txt") :: IO (Either SomeException String)
  case result of
    Right contents -> putStrLn contents
    Left err       -> putStrLn $ "Error: " ++ show err
```

```haskell
-- WRONG: Hardcoded path
main = readFile "/home/user/data.txt" >>= putStrLn

-- CORRECT: Use configurable path
import System.Environment (lookupEnv)

main = do
  maybePath <- lookupEnv "DATA_FILE"
  case maybePath of
    Just path -> readFile path >>= putStrLn
    Nothing   -> putStrLn "DATA_FILE environment variable not set"
```

## Examples

```haskell
-- Example 1: Safe file reading
import System.IO
import Control.Exception (try, IOException)

safeReadFile :: FilePath -> IO (Maybe String)
safeReadFile path = do
  result <- try (readFile path) :: IO (Either IOException String)
  return $ case result of
    Right contents -> Just contents
    Left _         -> Nothing

-- Example 2: Directory operations
import System.Directory

listFiles :: FilePath -> IO [FilePath]
listFiles dir = do
  exists <- doesDirectoryExist dir
  if exists
    then getDirectoryContents dir
    else return []

-- Example 3: Resource cleanup
import System.IO (withFile, IOMode(ReadMode), hGetContents)

main = withFile "data.txt" ReadMode $ \handle -> do
  contents <- hGetContents handle
  putStrLn contents
  -- File automatically closed when block exits
```

## Related Errors

- [haskell-missing-module]({{< relref "/languages/haskell/haskell-missing-module" >}}) — missing module
- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match
- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
