---
title: "State Injection Error"
description: "Fix Compose state injection and dependency provision for composable trees"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
State or dependencies not properly injected into composable trees

## Common Causes

- CompositionLocal not providing correct value
- State not reaching deeply nested composables
- Multiple state providers conflicting
- Default value causing crash

## Fixes

- Use CompositionLocalProvider at theme level
- Provide state at highest needed level
- Use unique CompositionLocal per type
- Set sensible defaults for all CompositionLocals

## Code Example

```kotlin
// Define injectable state
val LocalAuthState = compositionLocalOf<AuthState> { 
    error("No AuthState provided") 
}

// Provide at app level
@Composable
fun App(authState: AuthState) {
    CompositionLocalProvider(LocalAuthState provides authState) {
        MyTheme {
            NavHost(...)
        }
    }
}

// Consume anywhere in tree
@Composable
fun ProfileScreen() {
    val auth = LocalAuthState.current
    if (auth.isLoggedIn) {
        ProfileContent(auth.user)
    } else {
        LoginScreen()
    }
}
```

# CompositionLocal: context-like state injection
# Provide at highest level needed
# current: read value anywhere in tree
# Always provide before consuming
