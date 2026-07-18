---
title: "[Solution] Go WASM Error — How to Fix"
description: "Fix Go WASM errors. Handle WebAssembly compilation, JavaScript interop, and runtime configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go WASM Error

Fix Go WASM errors. Handle WebAssembly compilation, JavaScript interop, and runtime configuration.

## Why It Happens

- Go WASM compilation fails because of wrong GOOS/GOARCH settings
- JavaScript interop does not work because of wrong function signatures
- WASM binary is too large for web deployment

## Common Error Messages

```
go build: GOOS=js GOARCH=wasm required
```
```
wasm: js.Global is not defined
```
```
wasm: invalid function signature
```
```
wasm: binary too large
```

## How to Fix It

### Solution 1: Compile Go to WASM

```bash
GOOS=js GOARCH=wasm go build -o main.wasm
# Copy the JS glue file
cp $(go env GOROOT)/lib/wasm/wasm_exec.js .
```

### Solution 2: Use JavaScript interop

```go
package main
import "syscall/js"

func main() {
    document := js.Global().Get("document")
    p := document.Call("createElement", "p")
    p.Set("innerHTML", "Hello from Go!")
    document.Get("body").Call("appendChild", p)
    // Keep the Go program running
    select {}
}
```

### Solution 3: Reduce WASM binary size

```bash
# Use wasm-opt from Binaryen
wasm-opt -Oz main.wasm -o main_opt.wasm
# Or strip debug info
go build -ldflags="-s -w" -o main.wasm
```

### Solution 4: Run WASM in browser

```html
<script src="wasm_exec.js"></script>
<script>
const go = new Go();
WebAssembly.instantiateStreaming(fetch("main.wasm"), go.importObject).then(result => {
    go.run(result.instance);
});
</script>
```

## Common Scenarios

- Go WASM binary does not compile because of wrong GOOS/GOARCH
- JavaScript calls from Go do not work because of wrong function signatures
- WASM binary is very large and slow to load

## Prevent It

- Always use GOOS=js GOARCH=wasm for WASM compilation
- Use the wasm_exec.js glue file for Go-JavaScript interop
- Use wasm-opt to reduce binary size
