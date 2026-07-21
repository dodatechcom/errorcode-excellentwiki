---
title: "[Solution] Deprecated Function Migration: math/rand to crypto/rand"
description: "Migrate from deprecated math/rand to crypto/rand for secure random in Go."
deprecated_function: "math/rand"
replacement_function: "crypto/rand"
languages: ["go"]
deprecated_since: "Go 1.20+"
---

# [Solution] Deprecated Function Migration: math/rand to crypto/rand

The `math/rand` has been deprecated in favor of `crypto/rand`.

## Migration Guide

math/rand is not cryptographically secure. Use crypto/rand for tokens, keys, passwords.

## Before (Deprecated)

```go
import "math/rand"

token := rand.Intn(1000000)
b := make([]byte, 32)
for i := range b {
    b[i] = byte(rand.Intn(256))
}
```

## After (Modern)

```go
import (
    "crypto/rand"
    "math/big"
)

token, err := rand.Int(rand.Reader, big.NewInt(1000000))
b := make([]byte, 32)
_, err = rand.Read(b)
```

## Key Differences

- crypto/rand uses OS entropy source
- math/rand is deterministic
- Use crypto/rand for security
- Use math/rand for simulations
