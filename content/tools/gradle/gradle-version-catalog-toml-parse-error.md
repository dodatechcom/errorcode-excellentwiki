---
title: "Gradle Version Catalog TOML Parse Error"
description: "Gradle version catalog TOML file contains syntax errors that prevent the catalog from being parsed during project configuration."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Version Catalog TOML Parse Error

Gradle reads version catalogs from TOML files. A parse error means the TOML syntax is invalid, preventing Gradle from reading dependency definitions.

## Common Causes

- Missing quotes around values that contain special characters
- Incorrect TOML table syntax with missing brackets
- Duplicate key definitions in the same table
- Version reference points to a non-existent key

## How to Fix

1. Validate the TOML file syntax:

```bash
# Check for syntax errors
python3 -c "import tomllib; tomllib.load(open('gradle/libs.versions.toml', 'rb'))"
```

2. Ensure string values are properly quoted:

```toml
# Incorrect -- unquoted value with special characters
[versions]
spring-boot = 3.2.2

# Correct -- quotes around version strings
[versions]
spring-boot = "3.2.2"
```

3. Verify version references exist:

```toml
[versions]
kotlin = "1.9.22"

[libraries]
kotlin-stdlib = { module = "org.jetbrains.kotlin:kotlin-stdlib", version.ref = "kotlin" }
# version.ref must match a key in [versions]
```

4. Check for duplicate keys:

```bash
grep -n "^\[" gradle/libs.versions.toml
```

## Examples

```toml
# Correct version catalog structure
[versions]
kotlin = "1.9.22"
junit = "5.10.1"

[libraries]
kotlin-stdlib = { module = "org.jetbrains.kotlin:kotlin-stdlib", version.ref = "kotlin" }
junit-jupiter = { group = "org.junit.jupiter", name = "junit-jupiter", version.ref = "junit" }

[bundles]
testing = ["junit-jupiter"]

[plugins]
kotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version.ref = "kotlin" }
```

```bash
# Error output
Could not parse version catalog 'libs': 
  line 8: key 'kotlin' already exists in table '[versions]'
```

## Related Errors

- [TOML File Syntax]({{< relref "/tools/gradle/gradle-toml-file-syntax" >}}) -- general TOML issues
- [Version Catalog Accessor Error]({{< relref "/tools/gradle/gradle-version-catalog-accessor-error" >}}) -- accessor generation failures
