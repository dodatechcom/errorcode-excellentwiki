---
title: "Duplicate Resource Name"
description: "Resolve duplicate resource name conflicts across Android resource directories"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because the same resource name exists in multiple resource qualifiers

## Common Causes

- Same layout name in both layout and layout-v21
- Drawable with same name in drawable and drawable-hdpi
- Values XML has duplicate string name
- Resource defined in both main and flavor source sets

## Fixes

- Rename one of the duplicate resources
- Use resource qualifiers that do not overlap
- Merge values using tools:override attribute
- Check all res/ subdirectories for naming conflicts

## Code Example

```kotlin
# BAD: two files with same name
res/layout/item_list.xml
res/layout-large/item_list.xml  # This is OK (qualifier)

# BAD: duplicate string name
<!-- values/strings.xml -->
<string name="app_name">MyApp</string>
<!-- values-ru/strings.xml -->
<string name="app_name">МоёПриложение</string>
<!-- values/strings.xml also has app_name again = ERROR -->
```

# Find duplicates
grep -r "name="app_name"" app/src/main/res/values*/
