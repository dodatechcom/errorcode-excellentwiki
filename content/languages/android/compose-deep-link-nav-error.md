---
title: "Deep Link Navigation Error"
description: "Fix deep link handling with Compose Navigation and URI parsing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Deep links do not open correct Compose destination or parse arguments

## Common Causes

- Deep link pattern not matching URI format
- Arguments not extracted from URI path
- AutoVerify not working for App Links
- Intent data not passed to Navigation

## Fixes

- Define deep link in composable with deepLinks parameter
- Extract arguments from URI path and query
- Configure Digital Asset Links for verification
- Use NavHost with handleDeepLink

## Code Example

```kotlin
composable(
    route = "product/{productId}",
    deepLinks = listOf(
        navDeepLink { uriPattern = "myapp://product/{productId}" }
    )
) { backStackEntry ->
    val productId = backStackEntry.arguments?.getString("productId")
    ProductScreen(productId = productId)
}

// Handle incoming intent in Activity:
class MainActivity : ComponentActivity() {
    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        navController.handleDeepLink(intent)
    }
}
```

# deepLinks: list of URI patterns
# uriPattern: template with {argName}
# handleDeepLink: process incoming intent
