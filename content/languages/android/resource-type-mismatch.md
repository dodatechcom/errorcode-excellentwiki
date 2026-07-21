---
title: "Resource Type Mismatch"
description: "Fix resource type mismatch errors when accessing Android resources"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Code references a resource but uses the wrong accessor type

## Common Causes

- Accessing string resource with R.drawable reference
- Using getString on a layout resource ID
- Wrong R inner class for resource type
- View binding type mismatch in generated code

## Fixes

- Use correct R inner class: R.string, R.layout, R.drawable
- Match accessor method to resource type
- Check resource file extension to determine type
- Use Android Studio autocomplete to avoid type errors

## Code Example

```kotlin
// Wrong:
val res = resources.getString(R.drawable.ic_launcher)
// Correct:
val icon = ContextCompat.getDrawable(this, R.drawable.ic_launcher)
val text = resources.getString(R.string.app_name)
val layout = LayoutInflater.from(this).inflate(R.layout.activity_main, null)
```

# Resource types:
# R.string.  - strings.xml
# R.drawable. - drawable resources
# R.layout.  - layout XML
# R.id.      - view IDs
# R.color.   - color resources
# R.style.   - style resources
