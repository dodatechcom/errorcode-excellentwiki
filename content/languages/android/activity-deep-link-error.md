---
title: "Activity Deep Link Error"
description: "Fix Android activity deep link handling and intent processing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Activity does not open from deep link or processes intent data incorrectly

## Common Causes

- Intent data URI not parsed correctly
- Deep link opens wrong activity
- Intent extras not extracted in onCreate
- App Links not verified for domain

## Fixes

- Parse intent.data URI in onCreate
- Verify intent-filter matches deep link pattern
- Use intent.extras to extract parameters
- Configure App Links with Digital Asset Links

## Code Example

```kotlin
class DeepLinkActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val uri = intent?.data
        uri?.let { link ->
            val path = link.lastPathSegment
            val query = link.getQueryParameter("id")
            navigateToScreen(path, query)
        }
    }
}

// Or in existing activity:
override fun onNewIntent(intent: Intent?) {
    super.onNewIntent(intent)
    setIntent(intent)
    handleDeepLink(intent?.data)
}
```

# Verify deep link:
# adb shell am start -a android.intent.action.VIEW #   -d "myapp://screen/123" com.example.app
