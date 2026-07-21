---
title: "Resource XML Syntax Error"
description: "Fix XML syntax errors in Android resource layout and values files"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because resource XML file has syntax or structure errors

## Common Causes

- Unclosed XML tags in layout files
- Invalid attribute names or values
- Special characters not properly escaped
- Namespace prefix not declared

## Fixes

- Use Android Studio XML validation
- Close all open tags properly
- Escape special characters with &amp; entities
- Declare namespace prefixes with xmlns:

## Code Example

```kotlin
<!-- BAD: unclosed tag -->
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"

<!-- GOOD: properly closed -->
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello" />
```

# Validate XML manually
xmllint --noout app/src/main/res/layout/activity_main.xml
