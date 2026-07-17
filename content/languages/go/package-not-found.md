---
title: "[Solution] Go Package Not Found Error Fix"
description: "Fix Go no required module provides package error. Check import paths, run go mod tidy, and verify module configuration."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# No Required Module Provides Package — Fix

A "no required module provides package" error occurs when your code imports a package that isn't available in any module listed in `go.mod`.

## Description

Go modules track dependencies in `go.mod`. When you import a package, Go looks for it in the modules listed in `go.mod`. If the package isn't in any required module — either because it was never added, or because the import path is wrong — this error occurs.

Common scenarios:

- **Missing go mod tidy** — new import not yet added to go.mod.
- **Wrong import path** — typo or incorrect module path.
- **Indirect dependency not listed** — package is a dependency of a dependency.
- **Module not published** — importing a module that doesn't exist on the proxy.
- **Fork not registered** — using a fork without updating go.mod.

## Common Causes

```bash
# Cause 1: Forgot to run go mod tidy
import "github.com/some/new/package"

go build
# no required module provides package github.com/some/new/package

# Cause 2: Wrong import path
import "github.com/some/packagee"  # typo: packagee

# Cause 3: Package in dependency not in go.mod
# Package is in a module that's not a direct dependency

# Cause 4: Private module not configured
import "github.com/private-org/internal/pkg"
# Module proxy doesn't have it
```

## How to Fix

### Fix 1: Run go mod tidy to add missing dependencies

```bash
# Wrong — manually adding to go.mod
require github.com/some/package v1.0.0

# Correct — let Go figure it out
go mod tidy
```

### Fix 2: Verify import path is correct

```go
// Wrong — typo
import "github.com/some/packagee"

// Correct
import "github.com/some/package"
```

### Fix 3: Add missing direct dependency

```bash
# If go mod tidy doesn't find it, add explicitly
go get github.com/some/package@v1.0.0
go mod tidy
```

### Fix 4: Configure private module access

```bash
# For private modules
# Set GOPRIVATE to skip proxy
go env -w GOPRIVATE=github.com/private-org/*

# Configure git for private repos
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

### Fix 5: Check module path in go.mod

```go
// go.mod — ensure module path matches your import
module github.com/username/myproject  // Must match your code's import path

require (
    github.com/dependency v1.0.0
)
```

### Fix 6: Use replace directive for forks

```go
// go.mod — use replace for forks
module github.com/username/myproject

require (
    github.com/original/pkg v1.0.0
)

replace github.com/original/pkg => github.com/yourfork/pkg v1.0.1-fork
```

## Examples

```bash
# This triggers: no required module provides package github.com/nonexistent/pkg
cat > main.go << 'EOF'
package main

import "github.com/nonexistent/pkg"

func main() {
    pkg.DoSomething()
}
EOF

go mod init example.com/test
go build
# no required module provides package github.com/nonexistent/pkg
```

## Related Errors

- [go-mod-not-found]({{< relref "/languages/go/go-mod-not-found" >}}) — go.mod file not found.
- [go-mod-version]({{< relref "/languages/go/go-mod-version" >}}) — Go version mismatch.
- [go-sum-mismatch]({{< relref "/languages/go/go-sum-mismatch" >}}) — go.sum checksum mismatch.
