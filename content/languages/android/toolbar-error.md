---
title: "Toolbar Configuration Error"
description: "Fix Material Toolbar and ActionBar configuration errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Toolbar or ActionBar does not display correctly or navigation does not work

## Common Causes

- ActionBar not set as support action bar
- Toolbar not defined in layout XML
- Navigation click listener not responding
- Title not updating on fragment changes

## Fixes

- Set setSupportActionBar(toolbar) in Activity
- Use com.google.android.material.appbar.MaterialToolbar
- Set navigation icon click listener
- SupportActionBar?.title = "New Title" in fragments

## Code Example

```kotlin
<!-- Layout XML -->
<com.google.android.material.appbar.MaterialToolbar
    android:id="@+id/toolbar"
    android:layout_width="match_parent"
    android:layout_height="?attr/actionBarSize"
    app:title="My App"
    app:navigationIcon="@drawable/ic_back" />

// In Activity:
setSupportActionBar(toolbar)
supportActionBar?.setDisplayHomeAsUpEnabled(true)

toolbar.setNavigationOnClickListener {
    onBackPressedDispatcher.onBackPressed()
}

// In Fragment:
(requireActivity() as AppCompatActivity).supportActionBar?.title = "Fragment Title
```

# MaterialToolbar for Material Design
# setSupportActionBar() to connect with ActionBar
# setNavigationOnClickListener for back button
