---
title: "Missing Default Resource"
description: "Fix missing default resource qualifier errors for Android resource fallback"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because resource has no default (unqualified) fallback

## Common Causes

- Resource exists only in qualified folder like values-es
- No res/values/strings.xml default entry
- Drawable has only density-specific versions
- Device uses locale or config not covered by any qualifier

## Fixes

- Always provide a default (unqualified) resource
- Add base strings in values/strings.xml
- Provide default drawable in drawable/ folder
- Test with multiple device configurations

## Code Example

```kotlin
<!-- BAD: only exists in values-fr -->
<string name="hello">Bonjour</string>

<!-- GOOD: default in values/strings.xml -->
<string name="hello">Hello</string>
<!-- With French override in values-fr/strings.xml -->
<string name="hello">Bonjour</string>
```

# Check for missing defaults
./gradlew lintDebug | grep "MissingTranslation" 
