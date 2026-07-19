---
title: "[Solution] Go test embed error — Testing Error Fix"
description: "Fix Go embed in test files."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test embed errors

Embedding files in test files requires the embed directive in the correct position.

## How to Fix

### Fix 1: Proper embed in test file

```go
package mypackage_test

import _ "embed"

//go:embed testdata/input.json
var testInput []byte

func TestWithEmbeddedFile(t *testing.T) {
    var data map[string]interface{}
    json.Unmarshal(testInput, &data)
    // test with data
}
```

## Related Errors

- [embed-errors]({{< relref "/languages/go/embed-errors" >}}) — embed errors.
- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
