---
title: "[Solution] Go embed Error — How to Fix"
description: "Fix Go embed errors. Handle embedded file access, directory embedding, and build constraints."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go embed Error

Fix Go embed errors. Handle embedded file access, directory embedding, and build constraints.

## Why It Happens

- Embedded files cannot be accessed because of incorrect import path
- embed directive syntax is wrong causing compilation failure
- Embedded directory does not exist at compile time
- embed does not work with go generate

## Common Error Messages

```
//go:embed: no matching files found
```
```
embed: pattern contains no files
```
```
embed: file not found
```
```
embed: pattern must not contain '..'
```

## How to Fix It

### Solution 1: Embed files correctly

```go
import "embed"

//go:embed static/index.html
var indexHTML string

//go:embed static/*
var staticFiles embed.FS

//go:embed templates/*.html
var templateFS embed.FS
```

### Solution 2: Serve embedded files

```go
func main() {
    http.Handle("/static/", http.FileServer(http.FS(staticFiles)))
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte(indexHTML))
    })
}
```

### Solution 3: Access embedded files

```go
// Read a file
data, _ := staticFiles.ReadFile("static/app.js")
// Read directory
entries, _ := staticFiles.ReadDir("static")
for _, e := range entries { fmt.Println(e.Name()) }
```

### Solution 4: Handle embed with build tags

```go
//go:build !embed
//go:embed static/*
var staticFiles embed.FS

// For dev: load from filesystem
// For prod: use embed
```

## Common Scenarios

- embed: no matching files found because the directory does not exist
- Embedded files are empty because the path is wrong
- embed does not work with go run because it needs compilation

## Prevent It

- Ensure embedded paths exist at compile time
- Use embed.FS for multiple files and http.FileServer for serving
- Test embedded files in both development and production builds
