---
title: "[Solution] Go test temporary directory error — Testing Error Fix"
description: "Fix Go test temporary directory issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test temporary directory errors

`t.TempDir()` creates a temporary directory that is cleaned up automatically.

## How to Fix

```go
func TestWithTempDir(t *testing.T) {
    dir := t.TempDir()
    path := filepath.Join(dir, "output.txt")
    os.WriteFile(path, []byte("data"), 0644)
    // dir is automatically removed after test
}
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
