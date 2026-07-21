---
title: "Dynamic Links Error"
description: "Fix Firebase Dynamic Links creation and handling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase Dynamic Links fail to create, open, or pass data correctly

## Common Causes

- Dynamic Link domain not configured in Firebase
- Link not created with proper parameters
- Deep link data not extracted from intent
- Link analytics not tracked

## Fixes

- Configure Dynamic Link domain in Firebase console
- Build links with FirebaseDynamicLink.Builder
- Parse link data in Activity onCreate
- Track link performance in Firebase console

## Code Example

```kotlin
val dynamicLink = Firebase.dynamicLinks.dynamicLink {
    link = Uri.parse("https://example.com/promo?campaign=summer")
    domainUriPrefix = "https://example.app.link"
    androidParameters {
        minimumVersion = 24
    }
    iosParameters("com.example.ios") {
        minimumVersion = "12.0"
    }
    googleAnalyticsParameters {
        source = "android"
        medium = "social"
        campaign = "summer_sale"
    }
}

// Get dynamic link from intent:
Firebase.dynamicLinks
    .getDynamicLink(intent)
    .addOnSuccessListener { pendingDynamicLinkData ->
        val deepLink = pendingDynamicLinkData?.link
        val campaign = deepLink?.getQueryParameter("campaign")
    }
```

# Configure in Firebase Console > Dynamic Links
# Use app.link domain for short links
# Track analytics with UTM parameters
