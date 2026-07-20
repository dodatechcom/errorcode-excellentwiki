---
title: "[Solution] yaml Unmarshal Error Fix"
description: "Fix Go YAML unmarshal errors. Handle malformed YAML, type conversion, and tag configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# yaml Unmarshal Error

The `gopkg.in/yaml.v3` package fails to unmarshal YAML when there are indentation errors, type mismatches between YAML values and Go struct fields, anchor/alias references are broken, or multi-line strings have wrong indicators. YAML is whitespace-sensitive, making indentation the most common error source.

## Common Causes

```go
// Cause 1: Indentation error
// wrong:
// database:
// host: localhost   (must indent under database)

// Cause 2: Type mismatch — YAML integer into Go string
type Config struct {
    Port string `yaml:"port"`
}
// yaml: port: 8080  (integer, wants string)

// Cause 3: Anchor/alias reference not found
// default: &default
//   timeout: 30
// server:
//   timeout: *default  # works
//   retry: *missing    # undefined alias

// Cause 4: YAML boolean parsed as string
type Config struct {
    Debug bool `yaml:"debug"`
}
// yaml: debug: "yes"  (string, not boolean)
// YAML treats "yes" as boolean true

// Cause 5: Multi-line string wrong indicator
// description: |     # literal block
//   line 1
//   line 2
// wrong: description: |4  # explicit indentation indicator wrong
```

## How to Fix

### Fix 1: Use proper YAML struct tags

```go
import (
    "fmt"
    "log"
    "os"

    "gopkg.in/yaml.v3"
)

type Config struct {
    Server struct {
        Host string `yaml:"host"`
        Port int    `yaml:"port"`
    } `yaml:"server"`
    Database struct {
        Driver string `yaml:"driver"`
        DSN    string `yaml:"dsn"`
    } `yaml:"database"`
}

func loadConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, err
    }

    var cfg Config
    if err := yaml.Unmarshal(data, &cfg); err != nil {
        return nil, fmt.Errorf("parse yaml: %w", err)
    }
    return &cfg, nil
}
```

### Fix 2: Use YAML decoder for streaming

```go
func decodeConfig(r io.Reader) (*Config, error) {
    var cfg Config
    decoder := yaml.NewDecoder(r)
    if err := decoder.Decode(&cfg); err != nil {
        return nil, err
    }
    return &cfg, nil
}
```

### Fix 3: Use yaml.Node for dynamic YAML processing

```go
func parseDynamic(data []byte) (map[string]interface{}, error) {
    var result map[string]interface{}
    err := yaml.Unmarshal(data, &result)
    return result, err
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "gopkg.in/yaml.v3"
)

type Config struct {
    AppName string `yaml:"app_name"`
    Debug   bool   `yaml:"debug"`
    Port    int    `yaml:"port"`
}

func main() {
    yamlData := `
app_name: myapp
debug: true
port: 8080
`
    var cfg Config
    if err := yaml.Unmarshal([]byte(yamlData), &cfg); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("App: %s, Debug: %v, Port: %d\n", cfg.AppName, cfg.Debug, cfg.Port)
}
```

## Related Errors

- [go-toml-error]({{< relref "/languages/go/go-toml-error" >}}) — TOML config parsing errors
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON unmarshal type mismatches
- [go-viper-error]({{< relref "/languages/go/go-viper-error" >}}) — Viper config loading issues
