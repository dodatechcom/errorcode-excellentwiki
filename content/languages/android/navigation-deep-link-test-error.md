---
title: "Deep Link Test Error"
description: "Fix Android deep link testing and verification errors in Navigation component"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Deep links do not work in testing or verification fails

## Common Causes

- Deep link URI not matching intent filter
- App Links verification failing in production
- adb command not triggering correct activity
- Test deep link not opening expected screen

## Fixes

- Test deep links with adb am start command
- Verify Digital Asset Links in production
- Check intent-filter matches deep link pattern
- Use Navigation testing library for verification

## Code Example

```kotlin
# Test deep link with adb:
adb shell am start -a android.intent.action.VIEW     -d "myapp://detail/123"     com.example.app

# Verify App Links:
adb shell dumpsys package d | grep myapp

# Navigation test:
@Test
fun deepLink_toDetailPage() {
    val navController = NavHostController(context)
    navController.setGraph(R.navigation.nav_graph)

    val deepLink = "myapp://detail/123".toUri()
    navController.handleDeepLink(Intent(Intent.ACTION_VIEW, deepLink))

    assertEquals(R.id.detailFragment, navController.currentDestination?.id)
}
```

# adb shell am start -d URI: test deep link
# Digital Asset Links: verify App Links
# Navigation testing: verify navigation
