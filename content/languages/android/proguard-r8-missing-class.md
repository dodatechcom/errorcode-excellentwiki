---
title: "R8 Missing Class Warning"
description: "Fix R8 missing class warning and keep rules for Android release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Release build generates warnings or crashes because R8 removed needed classes

## Common Causes

- Class referenced via reflection not kept by R8
- Missing -keep rule for serialization model
- Third-party library class stripped by R8
- Interface implementation removed by R8 optimization

## Fixes

- Add -keep class rule for reflective access
- Use @Keep annotation on model classes
- Add dontwarn rules for optional dependencies
- Verify proguard-rules.pro has complete rules

## Code Example

```kotlin
# proguard-rules.pro
-keep class com.example.models.** { *; }
-keepattributes *Annotation*
-keep class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    !static !transient <fields>;
}
```

# Check what R8 is removing
./gradlew assembleRelease --info | grep "R8"
# Or use mapping.txt to trace obfuscated names
