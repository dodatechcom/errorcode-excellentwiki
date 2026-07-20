---
title: "[Solution] toml Decode Error Fix"
description: "Fix Go TOML decode errors. Handle malformed TOML, missing sections, and type conversion."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# toml Decode Error

The `github.com/BurntSushi/toml` package fails to decode TOML configuration files due to syntax errors, type mismatches between TOML values and Go struct fields, missing required keys, or incorrect use of inline tables. TOML is strict about types — a string where an integer is expected causes a hard error.

## Common Causes

```go
// Cause 1: TOML syntax error — missing quotes around string with spaces
// config.toml: name = Hello World   (wrong)
// config.toml: name = "Hello World"  (correct)

// Cause 2: Type mismatch — TOML integer assigned to Go string
type Config struct {
    Port string `toml:"port"` // expects string
}
// config.toml: port = 8080   (integer, not string)

// Cause 3: Missing nested table
type Config struct {
    Database Database `toml:"database"`
}
// config.toml missing [database] section — zero value, no error

// Cause 4: Non-existent file
_, err := toml.DecodeFile("config.toml", &cfg)
// open config.toml: no such file or directory

// Cause 5: TOML array of tables parsed into wrong Go type
// [[servers]]
// name = "s1"
// If Servers is not a slice, decode fails
```

## How to Fix

### Fix 1: Use toml.DecodeFile with proper error handling

```go
import (
    "fmt"
    "log"

    "github.com/BurntSushi/toml"
)

type Config struct {
    Server   Server   `toml:"server"`
    Database Database `toml:"database"`
}

type Server struct {
    Host string `toml:"host"`
    Port int    `toml:"port"`
}

type Database struct {
    Driver string `toml:"driver"`
    DSN    string `toml:"dsn"`
}

func loadConfig(path string) (*Config, error) {
    var cfg Config
    if _, err := toml.DecodeFile(path, &cfg); err != nil {
        return nil, fmt.Errorf("decode config: %w", err)
    }
    return &cfg, nil
}
```

### Fix 2: Use toml.Decode for string-based config

```go
tomlData := `
[server]
host = "localhost"
port = 8080

[database]
driver = "mysql"
dsn = "user:pass@tcp(localhost:3306)/db"
`

var cfg Config
if _, err := toml.Decode(tomlData, &cfg); err != nil {
    log.Fatal(err)
}
```

### Fix 3: Use default values for optional fields

```go
func loadConfig(path string) Config {
    cfg := Config{
        Server: Server{Host: "0.0.0.0", Port: 3000},
    }
    toml.DecodeFile(path, &cfg)
    return cfg
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/BurntSushi/toml"
)

type Config struct {
    AppName  string `toml:"app_name"`
    Debug    bool   `toml:"debug"`
    Port     int    `toml:"port"`
    Database struct {
        Host string `toml:"host"`
        Port int    `toml:"port"`
    } `toml:"database"`
}

func main() {
    var cfg Config
    if _, err := toml.DecodeFile("config.toml", &cfg); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("App: %s, Port: %d, DB: %s:%d\n",
        cfg.AppName, cfg.Port, cfg.Database.Host, cfg.Database.Port)
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — similar type mismatch issues with JSON
- [go-yaml-error]({{< relref "/languages/go/go-yaml-error" >}}) — YAML parsing has comparable struct-tag pitfalls
- [go-viper-error]({{< relref "/languages/go/go-viper-error" >}}) — Viper wraps multiple config formats including TOML
