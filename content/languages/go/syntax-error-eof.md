---
title: "[Solution] Go syntax error: unexpected EOF — Compile Error Fix"
description: "Fix Go syntax error unexpected EOF."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# syntax error: unexpected EOF

The error `syntax error: unexpected EOF` occurs when the parser reaches the end of the file before completing a construct.

## Common Causes

- **Unclosed function** — missing closing brace
- **Unclosed string** — missing closing quote
- **Truncated file** — file was partially written

## How to Fix

### Fix 1: Check matching braces

```bash
gofmt -e file.go 2>&1
```

## Examples

```go
package main

func main() {
    fmt.Println("hello")
// missing closing brace
```

Output:
```
syntax error: unexpected EOF
```

## Related Errors

- [syntax-error-unexpected]({{< relref "/languages/go/syntax-error-unexpected" >}}) — other syntax errors.
- [undefined-name]({{< relref "/languages/go/undefined-name" >}}) — undefined names.
