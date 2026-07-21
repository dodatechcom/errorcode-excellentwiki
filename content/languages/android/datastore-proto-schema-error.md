---
title: "Proto DataStore Schema Error"
description: "Fix Proto DataStore schema evolution and backwards compatibility errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Proto DataStore fails after schema changes or cannot read old data

## Common Causes

- New proto field not having default value
- Removed field causing deserialization failure
- Proto DataStore corruption after schema change
- Multiple schema versions not handled

## Fixes

- Always provide default values for new fields
- Never remove proto fields, mark as reserved
- Handle corruption with corruptionHandler
- Test schema migration thoroughly

## Code Example

```kotlin
// settings.proto
syntax = "proto3";
option java_package = "com.example.datastore";

message UserSettings {
    bool dark_mode = 1;
    string username = 2;
    int32 font_size = 3;  // New field with default
    reserved 4;  // Previously removed field
    string theme = 5;  // New field
}

// In Kotlin serializer:
object UserSettingsSerializer : Serializer<UserSettings> {
    override val defaultValue: UserSettings = UserSettings.getDefaultInstance()
    // ... read/write methods
}
```

# Never delete proto fields, use reserved
# New fields must have defaults
# Test forward and backward compatibility
