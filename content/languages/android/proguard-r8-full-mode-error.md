---
title: "R8 Full Mode Error"
description: "Fix R8 full mode and aggressive optimization errors in release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
R8 full mode optimization causes unexpected behavior or crashes

## Common Causes

- Full mode removing classes needed at runtime
- Aggressive optimization changing program behavior
- Missing keep rules in full mode
- R8 warnings not addressed

## Fixes

- Test release builds thoroughly
- Add comprehensive keep rules
- Use -dontwarn for optional dependencies
- Verify with retrace tool

## Code Example

```kotlin
# Enable full mode in gradle.properties:
android.enableR8.fullMode=true

# Additional keep rules for full mode:
-keep class * extends android.os.Parcelable { *; }
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    !static !transient <fields>;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}
```

# R8 full mode: more aggressive optimization
# Requires more comprehensive keep rules
# Test release builds extensively
# Use retrace for crash deobfuscation
