---
title: "[Solution] Go test golden file error — Testing Error Fix"
description: "Fix Go golden file test errors."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# golden file test errors

Golden files store expected output for comparison tests.

## How to Fix

### Fix 1: Use update flag to regenerate

```go
var update = flag.Bool("update", false, "update golden files")

func TestGolden(t *testing.T) {
    got := generateOutput()
    golden := filepath.Join("testdata", t.Name()+".golden")
    if *update {
        os.WriteFile(golden, []byte(got), 0644)
    }
    expected, _ := os.ReadFile(golden)
    if got != string(expected) {
        t.Errorf("output differs from golden file")
    }
}
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
