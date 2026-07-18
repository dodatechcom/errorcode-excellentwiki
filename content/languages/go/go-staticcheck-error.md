---
title: "[Solution] Go Staticcheck Error — How to Fix"
description: "Fix Go staticcheck errors. Handle lint violations, unused code, deprecated APIs, and code style issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Staticcheck Error

Fix Go staticcheck errors. Handle lint violations, unused code, deprecated APIs, and code style issues.

## Why It Happens

- staticcheck finds deprecated function calls that should be replaced
- Unused variables and imports cause staticcheck warnings
- Static check errors are in generated code and should be ignored
- Different staticcheck configurations conflict across packages

## Common Error Messages

```
SA1019: .* is deprecated
```
```
SA4006: this value of .* is never used
```
```
S1034: assign .* to .* instead
```
```
staticcheck: unused function
```

## How to Fix It

### Solution 1: Fix deprecated API calls

```go
// Before: ioutil.ReadAll(r)
// After: io.ReadAll(r)
// Before: ioutil.ReadFile(f)
// After: os.ReadFile(f)
```

### Solution 2: Remove unused code

```go
// staticcheck will flag unused variables, imports, and functions
// Remove them or use _ for unused imports you want to keep
import _ "github.com/lib/pq"
```

### Solution 3: Suppress specific checks

```go
// nolint:staticcheck // SA1019: legacy code temporarily retained
var deprecatedVar = "old"
```

### Solution 4: Run staticcheck in CI

```go
// go install honnef.co/go/tools/cmd/staticcheck@latest
// staticcheck ./...
// Or use golangci-lint which includes staticcheck
```

## Common Scenarios

- staticcheck flags a deprecated function that is still needed for compatibility
- Generated code triggers staticcheck warnings
- Staticcheck runs very slowly on large codebases

## Prevent It

- Use nolint directives for intentional suppressions
- Exclude generated code from staticcheck analysis
- Run staticcheck incrementally on changed packages in CI
