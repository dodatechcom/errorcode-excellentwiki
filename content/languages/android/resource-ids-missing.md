---
title: "Resource ID Not Generated"
description: "Fix missing resource IDs after enabling view binding or data binding in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Cannot reference expected view ID because binding class is missing the field

## Common Causes

- View ID not present in layout XML
- View binding not enabled in build.gradle
- Layout uses <include> without android:id
- ID defined with typo or wrong case

## Fixes

- Add android:id to the view in layout XML
- Enable viewBinding in build.gradle android block
- Add ID to included layout's root view
- Check ID casing matches between XML and Kotlin code

## Code Example

```kotlin
android {
    buildFeatures {
        viewBinding = true
        dataBinding = true
    }
}
```

<!-- In layout XML -->
<TextView
    android:id="@+id/tvTitle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />

<!-- In code -->
binding.tvTitle.text = "Hello" 
