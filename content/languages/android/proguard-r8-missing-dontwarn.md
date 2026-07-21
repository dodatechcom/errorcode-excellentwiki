---
title: "R8 Missing Dontwarn Rule"
description: "Fix R8 dontwarn warnings for missing classes in Android release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build warns about missing classes that R8 cannot find during optimization

## Common Causes

- Third-party library has optional dependency not present
- AndroidX library references classes not in build
- Kotlin stdlib classes not found
- Google Play Services classes missing from classpath

## Fixes

- Add -dontwarn rule for missing class
- Use -ignorewarnings to suppress all
- Add the missing dependency if truly needed
- Use -dontwarn on specific packages only

## Code Example

```kotlin
# Common dontwarn rules
-dontwarn javax.annotation.**
-dontwarn org.codehaus.mojo.animal_sniffer.**
-dontwarn okhttp3.internal.platform.**
-dontwarn org.conscrypt.**
-dontwarn org.bouncycastle.**
-dontwarn org.openjsse.**
```

# To find which classes are missing:
./gradlew assembleRelease --info 2>&1 | grep "Warning:"
# Add dontwarn for each missing class
