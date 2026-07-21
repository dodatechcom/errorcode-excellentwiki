---
title: "Style Attribute Resolution Error"
description: "Fix style attribute resolution errors in Android theme and style definitions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because style references an attribute that does not exist

## Common Causes

- Typo in attribute reference name
- Using custom attribute without declaring it
- Attribute from wrong namespace used in style
- Referencing non-existent parent style

## Fixes

- Check attribute name spelling exactly
- Declare custom attrs in res/values/attrs.xml
- Use app: prefix for custom attributes
- Verify parent style exists in current theme

## Code Example

```kotlin
<!-- res/values/attrs.xml -->
<declare-styleable name="CustomView">
    <attr name="customColor" format="color" />
    <attr name="customSize" format="dimension" />
</declare-styleable>

<!-- res/values/styles.xml -->
<style name="CustomViewStyle">
    <item name="customColor">#FF0000</item>
    <item name="customSize">16sp</item>
</style>
```

# Use custom attribute in layout:
app:customColor="#FF0000"
app:customSize="16sp" 
