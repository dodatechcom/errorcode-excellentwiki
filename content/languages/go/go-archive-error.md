---
title: "[Solution] archive/tar Invalid Header Fix"
description: "Fix Go tar archive errors. Handle invalid headers, checksum mismatches, and format issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# archive/tar Invalid Header

The `archive/tar` package fails when reading tar archives with invalid headers, checksum mismatches, truncated data, or unsupported formats. Tar files have a 512-byte header block for each entry, and corruption in any header field causes parse errors.

## Common Causes

```go
// Cause 1: Data is not a valid tar archive
reader := tar.NewReader(file)
header, err := reader.Next()
// archive/tar: invalid tar header

// Cause 2: Truncated archive file
// File transfer interrupted — file is incomplete
header, err := reader.Next()
// unexpected EOF in tar archive

// Cause 3: Checksum mismatch
// Header block corrupted during write or storage
// tar header: checksum mismatch

// Cause 4: Using tar.NewReader on gzip data
// Need gzip.NewReader first, then tar.NewReader
tar.NewReader(gzipFile) // wrong — should decompress first

// Cause 5: Cross-platform path issues
// Windows paths in tar: C:\Users\...
// Linux tar expects: /Users/...
```

## How to Fix

### Fix 1: Decompress gzip before reading tar

```go
import (
    "archive/tar"
    "compress/gzip"
    "fmt"
    "io"
    "os"
)

func readTarGz(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()

    gz, err := gzip.NewReader(f)
    if err != nil {
        return fmt.Errorf("gzip reader: %w", err)
    }
    defer gz.Close()

    tarReader := tar.NewReader(gz)
    for {
        header, err := tarReader.Next()
        if err == io.EOF {
            break
        }
        if err != nil {
            return fmt.Errorf("tar reader: %w", err)
        }
        fmt.Printf("File: %s (%d bytes)\n", header.Name, header.Size)
    }
    return nil
}
```

### Fix 2: Validate tar headers before processing

```go
func extractFile(tarReader *tar.Reader, header *tar.Header, dest string) error {
    // Validate header
    if header.Name == "" {
        return fmt.Errorf("empty header name")
    }
    if header.Size < 0 {
        return fmt.Errorf("invalid size: %d", header.Size)
    }

    // Prevent path traversal
    if strings.Contains(header.Name, "..") {
        return fmt.Errorf("invalid path: %s", header.Name)
    }

    switch header.Typeflag {
    case tar.TypeReg:
        return extractRegularFile(tarReader, header, dest)
    case tar.TypeDir:
        return os.MkdirAll(filepath.Join(dest, header.Name), 0755)
    }
    return nil
}
```

### Fix 3: Write tar archives with proper headers

```go
func createTar(files []string, writer io.Writer) error {
    tarWriter := tar.NewWriter(writer)
    defer tarWriter.Close()

    for _, filePath := range files {
        info, err := os.Stat(filePath)
        if err != nil {
            return err
        }

        header := &tar.Header{
            Name:    filePath,
            Size:    info.Size(),
            Mode:    int64(info.Mode()),
            ModTime: info.ModTime(),
        }

        if err := tarWriter.WriteHeader(header); err != nil {
            return err
        }

        file, err := os.Open(filePath)
        if err != nil {
            return err
        }
        defer file.Close()

        if _, err := io.Copy(tarWriter, file); err != nil {
            return err
        }
    }
    return nil
}
```

## Examples

```go
package main

import (
    "archive/tar"
    "fmt"
    "io"
    "log"
    "os"
)

func main() {
    f, err := os.Open("archive.tar")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    reader := tar.NewReader(f)
    for {
        header, err := reader.Next()
        if err == io.EOF {
            break
        }
        if err != nil {
            log.Fatal(err)
        }

        fmt.Printf("Name: %s\n", header.Name)
        fmt.Printf("Size: %d\n", header.Size)
        fmt.Printf("Mode: %v\n", header.Mode)
        fmt.Printf("Type: %d\n", header.Typeflag)
    }
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of tar stream
- [go-compress-error]({{< relref "/languages/go/go-compress-error" >}}) — gzip decompression errors
- [file-exists]({{< relref "/languages/go/file-exists" >}}) — file operation errors during extraction
