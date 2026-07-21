---
title: "DataBinding Layout Error"
description: "Fix Android DataBinding layout configuration and binding expression errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataBinding layout fails to inflate or binding expressions do not evaluate

## Common Causes

- layout tag missing around root view
- Binding expression syntax has typos
- Variable type not imported in layout
- viewBinding and dataBinding both enabled causing conflict

## Fixes

- Wrap root view with <layout> tag
- Use correct expression syntax with @{}
- Add import statement in layout data block
- Enable only dataBinding, not both features

## Code Example

```kotlin
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <import type="com.example.models.User" />
        <variable
            name="user"
            type="User" />
    </data>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{user.name}" />
    </LinearLayout>
</layout>
```

// In Activity:
binding.user = User("John", 25)
binding.lifecycleOwner = this  // Required for LiveData
