---
title: "[Solution] Go Flag Error — How to Fix"
description: "Fix Go flag errors. Handle command-line argument parsing, flag definitions, and usage."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Flag Error

Fix Go flag errors. Handle command-line argument parsing, flag definitions, and usage.

## Why It Happens

- Flag is defined twice causing panic at runtime
- Flag value is not parsed correctly because of wrong type
- Flag usage message does not include all defined flags
- Flag parsing happens before all flags are defined

## Common Error Messages

```
flag: redefined flag
```
```
flag: invalid argument
```
```
flag: value not set
```
```
flag: flag provided but not defined
```

## How to Fix It

### Solution 1: Define and parse flags

```go
import "flag"

var (
    port    = flag.Int("port", 8080, "Server port")
    verbose = flag.Bool("verbose", false, "Enable verbose logging")
    config  = flag.String("config", "config.yaml", "Config file path")
)

func main() {
    flag.Parse()
    fmt.Println(*port, *verbose, *config)
}
```

### Solution 2: Parse flags in tests

```go
func TestFlags(t *testing.T) {
    os.Args = []string{"test", "-port", "9090"}
    flag.Parse()
    // Test with -port=9090
}
```

### Solution 3: Use custom flag types

```go
type StringList []string
func (s *StringList) String() string { return strings.Join(*s, ",") }
func (s *StringList) Set(v string) error { *s = append(*s, v); return nil }

var items StringList
flag.Var(&items, "item", "Item to process")
```

### Solution 4: Use flag.ContinueOnError

```go
err := flag.CommandLine.Parse(os.Args[1:])
if err != nil {
    // Handle parse error
}
```

## Common Scenarios

- Flag panics because two flags have the same name
- Flag value is wrong because parsing happens before all flags are defined
- Custom flag type does not implement the required interface

## Prevent It

- Define all flags before calling flag.Parse
- Use flag.Visit to check which flags were explicitly set
- Implement the flag.Value interface for custom types
