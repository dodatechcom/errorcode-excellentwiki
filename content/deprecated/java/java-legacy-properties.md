---
title: "[Solution] Deprecated Function Migration: Properties to modern configuration"
description: "Migrate from deprecated Properties to modern configuration formats."
deprecated_function: "Properties + FileInputStream"
replacement_function: "YAML / JSON / Typesafe Config"
languages: ["java"]
deprecated_since: "Modern Java"
---

# [Solution] Deprecated Function Migration: Properties to modern configuration

The `Properties + FileInputStream` has been deprecated in favor of `YAML / JSON / Typesafe Config`.

## Migration Guide

Properties only supports flat key-value strings

Properties cannot handle structured data.

## Before (Deprecated)

```java
Properties props = new Properties();
props.load(new FileInputStream("config.properties"));
```

## After (Modern)

```java
Config config = ConfigFactory.load();
String url = config.getString("database.url");
```

## Key Differences

- YAML/JSON support nested structures
- Type safety with modern config
- Properties is limited to flat key-value
