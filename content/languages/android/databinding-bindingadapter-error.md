---
title: "BindingAdapter Error"
description: "Fix custom BindingAdapter attribute errors in Android DataBinding"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom BindingAdapter attribute is not recognized or crashes during inflation

## Common Causes

- @BindingAdapter annotation name does not match XML attribute
- BindingAdapter method parameters do not match usage
- Missing @JvmStatic on BindingAdapter method
- Attribute name case sensitivity mismatch

## Fixes

- Ensure BindingAdapter attribute name matches XML usage exactly
- Match method parameters to attribute types
- Add @JvmStatic or put in companion object
- Check for camelCase vs snake_case mismatches

## Code Example

```kotlin
@BindingAdapter("imageUrl")
@JvmStatic
fun loadImage(imageView: ImageView, url: String?) {
    Glide.with(imageView.context)
        .load(url)
        .into(imageView)
}

@BindingAdapter(value = ["startColor", "endColor"], requireAll = true)
@JvmStatic
fun setGradient(view: View, startColor: Int, endColor: Int) {
    // Set gradient
}
```

<!-- In layout XML -->
<ImageView
    app:imageUrl="@{user.avatarUrl}" />

<!-- Multiple attributes -->
<View
    app:startColor="@{color.start}"
    app:endColor="@{color.end}" />
