---
title: "Type-Safe Navigation Error"
description: "Fix Compose type-safe navigation route definition and usage errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Type-safe navigation routes cause compile-time or runtime errors

## Common Causes

- Route class not properly defined with @Serializable
- Route arguments not matching destination parameters
- Navigation action not finding target route
- Kotlin serialization plugin not applied

## Fixes

- Define route as @Serializable data class
- Ensure route properties match destination arguments
- Use NavController.navigate with route object
- Apply Kotlin serialization plugin

## Code Example

```kotlin
// Define type-safe routes
@Serializable
data class ProductDetail(val productId: Int)

@Serializable
data class SearchResult(val query: String, val page: Int = 1)

// Navigation:
navController.navigate(ProductDetail(productId = 123))
navController.navigate(SearchResult(query = "shoes"))

// Destination:
composable<ProductDetail> { backStackEntry ->
    val route = backStackEntry.toRoute<ProductDetail>()
    ProductScreen(route.productId)
}
```

# @Serializable on route classes
# Route properties become arguments
# Use toRoute<T>() to extract arguments
# Kotlin serialization plugin required
