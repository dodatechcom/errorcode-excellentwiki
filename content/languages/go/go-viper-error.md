---
title: "[Solution] Go Viper Error — How to Fix"
description: "Fix Go Viper configuration errors. Handle config file loading, remote config, environment binding, type assertion, and watch failures."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Viper Error

Fix Go Viper configuration errors. Handle config file loading, remote config, environment binding, type assertion, and watch failures.

## Why It Happens

- The config file path is incorrect or the file format is not recognized by Viper
- Viper cannot connect to the remote config store such as Consul or etcd
- Environment variable bindings conflict with config file values causing unexpected results
- Type assertions on Viper values fail when the actual type differs from expected

## Common Error Messages

```
viper.ConfigFileNotFoundError: config file not found
```
```
viper: unable to read config: error
```
```
viper: unable to unmarshal: error
```
```
panic: interface conversion: interface {} is type, not type
```

## How to Fix It

### Solution 1: Set up Viper with defaults and config search

```go
v := viper.New()
v.SetDefault("server.port", 8080)
v.SetConfigName("config")
v.SetConfigType("yaml")
v.AddConfigPath(".")
v.SetEnvPrefix("APP")
v.AutomaticEnv()
if err := v.ReadInConfig(); err != nil {
    if _, ok := err.(viper.ConfigFileNotFoundError); ok {
        log.Println("no config file found, using defaults")
    }
}
```

### Solution 2: Use type-safe config retrieval

```go
if v.IsSet("server.port") {
    port := v.GetInt("server.port")
}
type Config struct {
    Server struct {
        Host string `mapstructure:"host"`
        Port int    `mapstructure:"port"`
    } `mapstructure:"server"`
}
var config Config
v.Unmarshal(&config)
```

### Solution 3: Handle remote config errors

```go
v.AddRemoteProvider("consul", "localhost:8500", "config/app")
v.SetConfigType("yaml")
if err := v.ReadRemoteConfig(); err != nil {
    log.Printf("remote config error: %v", err)
}
```

### Solution 4: Watch for config changes

```go
v.WatchConfig()
v.OnConfigChange(func(e fsnotify.Event) {
    log.Printf("config changed: %s", e.Name)
    var newConfig Config
    v.Unmarshal(&newConfig)
    applyConfig(newConfig)
})
```

## Common Scenarios

- A config file is not found because the path is relative and the working directory changed
- Viper returns wrong type when accessing nested config values
- Config hot-reload fails because the file watcher stops after the first change

## Prevent It

- Always set multiple AddConfigPath locations for fallback
- Use mapstructure tags on structs for proper Viper unmarshaling
- Test config loading in different working directories to catch path issues
