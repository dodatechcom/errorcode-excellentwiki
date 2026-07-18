---
title: "[Solution] Go fs Error — How to Fix"
description: "Fix Go fs errors. Handle filesystem operations, embedded filesystems, and path operations."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go fs Error

Fix Go fs errors. Handle filesystem operations, embedded filesystems, and path operations.

## Why It Happens

- fs.FS is not properly implemented causing file read failures
- Embedded filesystem paths do not match actual file locations
- File path operations produce wrong paths because of OS differences
- fs.ReadFile fails because the file does not exist in the filesystem

## Common Error Messages

```
fs: file not found
```
```
fs: invalid file name
```
```
fs: pattern has no matches
```
```
fs: read on closed file
```

## How to Fix It

### Solution 1: Use fs.FS correctly

```go
// Create FS from directory
fsys := os.DirFS("static")
data, _ := fs.ReadFile(fsys, "index.html")

// Use embedded FS
data, _ := fs.ReadFile(staticFiles, "static/index.html")
```

### Solution 2: Walk filesystem

```go
fs.WalkDir(fsys, ".", func(path string, d fs.DirEntry, err error) error {
    if err != nil { return err }
    if !d.IsDir() { fmt.Println(path) }
    return nil
})
```

### Solution 3: Use filepath correctly

```go
import "path/filepath"
filepath.Join("dir", "subdir", "file.txt")  // OS-specific
path.Join("dir", "subdir", "file.txt")  // always / separated
```

### Solution 4: Handle embedded FS

```go
//go:embed static
var staticFS embed.FS
func main() {
    subFS, _ := fs.Sub(staticFS, "static")
    http.Handle("/", http.FileServer(http.FS(subFS)))
}
```

## Common Scenarios

- fs.ReadFile fails because the path includes the embedding root
- File paths are not portable between Windows and Linux
- Embedded FS does not serve files correctly

## Prevent It

- Use fs.Sub to create sub-filesystems for embedded paths
- Use filepath.Join for OS-specific paths and path.Join for URL paths
- Test embedded FS paths carefully to ensure they match
