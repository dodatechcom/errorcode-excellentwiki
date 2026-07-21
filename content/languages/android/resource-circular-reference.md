---
title: "Circular Resource Reference"
description: "Fix circular resource reference errors in Android XML resource files"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails due to infinite loop in resource references

## Common Causes

- Style A references style B which references style A
- Color resource references another color that cycles back
- String template references itself recursively
- Theme parent chain forms a loop

## Fixes

- Remove circular parent references in styles
- Check color resource chain for cycles
- Use direct values instead of referencing other resources
- Use Android Studio resource validation

## Code Example

```kotlin
<!-- BAD: circular reference -->
<style name="Theme.A" parent="Theme.B" />
<style name="Theme.B" parent="Theme.A" />

<!-- GOOD: linear chain -->
<style name="Theme.A" parent="Theme.MaterialComponents.DayNight" />
<style name="Theme.B" parent="Theme.A" />
```

# Find circular references in styles
grep -r 'parent=' app/src/main/res/values*/styles*.xml
# Ensure parent chain is always one-directional
