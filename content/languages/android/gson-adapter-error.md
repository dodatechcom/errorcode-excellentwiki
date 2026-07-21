---
title: "Gson Adapter Error"
description: "Fix Gson TypeAdapter and serialization configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gson fails to serialize or deserialize objects correctly

## Common Causes

- Default Gson cannot handle Kotlin nullability
- Gson field naming policy mismatch
- Custom TypeAdapter not properly registered
- Transient fields not excluded from serialization

## Fixes

- Use GsonBuilder with Kotlin support
- Set fieldNamingPolicy to match JSON format
- Register custom TypeAdapter with GsonBuilder
- Use @Transient to exclude fields

## Code Example

```kotlin
val gson = GsonBuilder()
    .setFieldNamingPolicy(FieldNamingPolicy.LOWER_CASE_WITH_UNDERSCORES)
    .setPrettyPrinting()
    .create()

// Custom TypeAdapter:
class DateAdapter : TypeAdapter<Date>() {
    override fun write(out: JsonWriter, value: Date) {
        out.value(dateFormat.format(value))
    }
    override fun read(input: JsonReader): Date {
        return dateFormat.parse(input.nextString()) ?: Date()
    }
}

// Register:
val gson = GsonBuilder()
    .registerTypeAdapter(Date::class.java, DateAdapter())
    .create()
```

# GsonBuilder for configuration
# @Transient to exclude fields
# setFieldNamingPolicy for JSON key mapping
