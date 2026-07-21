---
title: "Proto DataStore Error"
description: "Fix Proto DataStore configuration and serialization errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Proto DataStore fails to read or write typed data objects

## Common Causes

- Proto file schema not properly defined
- DataStore not initialized with correct serializer
- Proto message field not matching data class
- DataStore corruption on first access

## Fixes

- Define .proto file with clear schema
- Implement DataStore Serializer for each message
- Ensure proto fields match data class properties
- Handle DataStore corruption with fallback

## Code Example

```kotlin
// settings.proto
syntax = "proto3";
option java_package = "com.example.datastore";
option java_multiple_files = true;

message UserSettings {
    bool dark_mode = 1;
    string username = 2;
    int32 font_size = 3;
}

// UserSettingsSerializer.kt
object UserSettingsSerializer : Serializer<UserSettings> {
    override val defaultValue: UserSettings = UserSettings.getDefaultInstance()

    override suspend fun readFrom(input: InputStream): UserSettings =
        try {
            UserSettings.parseFrom(input)
        } catch (exception: InvalidProtocolBufferException) {
            throw CorruptionException("Cannot read proto", exception)
        }

    override suspend fun writeTo(t: UserSettings, output: OutputStream) = t.writeTo(output)
}
```

# Initialize DataStore:
val Context.userSettingsDataStore by dataStore(
    fileName = "user_settings.pb",
    serializer = UserSettingsSerializer
)
