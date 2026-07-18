---
title: "[Solution] Go Fuzz Error — How to Fix"
description: "Fix Go fuzz errors. Handle fuzz target setup, corpus management, crash reproduction, and coverage guidance."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Fuzz Error

Fix Go fuzz errors. Handle fuzz target setup, corpus management, crash reproduction, and coverage guidance.

## Why It Happens

- Fuzz target function signature does not match the required format
- Fuzz corpus contains invalid inputs causing the target to panic
- Fuzz test takes too long without finding new coverage paths
- Crash file is not properly saved for reproduction

## Common Error Messages

```
fuzz: target must accept testing.F
```
```
fuzz: corpus contains invalid input
```
```
fuzz: test timed out after
```
```
fuzz: unable to find a crash
```

## How to Fix It

### Solution 1: Write proper fuzz targets

```go
func FuzzParseJSON(f *testing.F) {
    f.Add([]byte(`{"name": "test"}`))
    f.Add([]byte(`null`))
    f.Fuzz(func(t *testing.T, data []byte) {
        var result interface{}
        err := json.Unmarshal(data, &result)
        if err != nil { return }
        encoded, _ := json.Marshal(result)
        var result2 interface{}
        json.Unmarshal(encoded, &result2)
    })
}
```

### Solution 2: Manage fuzz corpus

```go
// Seed corpus in testdata/fuzz/<FuzzFuncName>/
// Add with f.Add() or manually
// Run: go test -fuzz=FuzzParseJSON -fuzztime=30s
```

### Solution 3: Reproduce crashes

```go
// Fuzz saves crash to testdata/fuzz/FuzzParseJSON/crash-<hash>
// Reproduce: go test -run=FuzzParseJSON/<crash-hash>
```

### Solution 4: Set fuzz time limits

```go
// go test -fuzz=FuzzParseJSON -fuzztime=10s
// go test -fuzz=FuzzParseJSON -fuzztime=0s (until first crash)
```

## Common Scenarios

- Fuzz target fails because the function signature is wrong
- Fuzz test does not find bugs because the corpus is too narrow
- A crash is found but the reproduction case is not saved

## Prevent It

- Use f.Add to seed the corpus with interesting inputs
- Run fuzz tests regularly in CI with a reasonable time limit
- Check testdata/fuzz/ for crash files and add them as regression tests
