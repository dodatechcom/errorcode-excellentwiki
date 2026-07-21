---
title: "Material Component Styling Error"
description: "Fix Material Design component styling and customization errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Material components do not reflect custom styling or appear with wrong appearance

## Common Causes

- Component style not overriding default Material style
- XML attributes not matching Material component API
- MaterialButton style not applying shape
- TextInputLayout error color not customizable

## Fixes

- Use Material theme attributes for styling
- Use style attribute to apply custom style
- Override Material style in theme or directly
- Use Material shape appearance for custom shapes

## Code Example

```kotlin
<!-- MaterialButton styling -->
<com.google.android.material.button.MaterialButton
    style="@style/Widget.Material3.Button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:cornerRadius="16dp"
    app:backgroundTint="@color/custom_color" />

<!-- TextInputLayout styling -->
<com.google.android.material.textfield.TextInputLayout
    style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
    app:errorEnabled="true"
    app:errorTextColor="@color/error_color"
    ...>
```

# Material theme attributes to override:
# colorPrimary, colorSecondary, colorSurface
# shapeAppearanceSmallComponent, shapeAppearanceLargeComponent
# Use AppCompat theme attributes for XML views
