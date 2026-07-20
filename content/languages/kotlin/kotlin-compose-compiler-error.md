---
title: "[Solution] Kotlin Compose Compiler Plugin — @Composable Invalid Calls"
description: "Fix Kotlin Compose compiler plugin errors. Learn why @Composable functions fail to compile and how to resolve composable call issues."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1026
---

## What This Error Means

Compose compiler plugin errors occur when @Composable functions are called in invalid contexts, the compiler plugin is misconfigured, or Kotlin version is incompatible with the Compose compiler version.

## Common Causes

- Calling @Composable functions outside of composable scope
- Kotlin version incompatible with Compose compiler version
- Missing `composeCompiler` or `compose` plugin configuration
- @Composable function used in non-suspend, non-composable context

```kotlin
// ERROR: Can't call composable from non-composable function
fun regularFunction() {
    Text("Hello")  // @Composable can only be called from @Composable context
}
```

## How to Fix

**1. Ensure Kotlin and Compose compiler versions match**

```kotlin
// build.gradle.kts
plugins {
    id("org.jetbrains.kotlin.plugin.compose") version "1.9.22"
}

composeCompiler {
    kotlinCompilerExtensionVersion = "1.5.8"
}
```

**2. Use @Composable wrapper for non-composable contexts**

```kotlin
// WRONG
class MyService {
    fun render() = Text("Hello")  // Error
}

// CORRECT
@Composable
fun ServiceRenderer(service: MyService) {
    Text(service.content)
}
```

**3. Use ComposeView in Activity/Fragment**

```kotlin
class MyActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyScreen()  // Valid composable context
        }
    }
}
```

**4. Use remember for composable lambdas**

```kotlin
@Composable
fun LazyScreen() {
    val items = remember { mutableStateListOf<Item>() }
    LazyColumn {
        items(items) { item ->
            ItemRow(item)  // Valid composable context
        }
    }
}
```

## Examples

```kotlin
// Example 1: Valid composable calling patterns
@Composable
fun Parent() {
    Child()  // OK — from composable
    AnotherChild {  // OK — trailing lambda
        GrandChild()
    }
}

// Example 2: Composable in non-UI context
@Composable
fun computeValue(): Int {
    val state = remember { mutableIntStateOf(0) }
    return state.intValue
}

// Example 3: Cross-composable conditional
@Composable
fun ConditionalContent(showBanner: Boolean) {
    if (showBanner) {
        Banner()
    }
    MainContent()  // Always called
}
```

## Related Errors

- [Compose recomposition](kotlin-compose-recomposition) — excessive recomposition
- [Gradle plugin error](kotlin-gradle-plugin-error) — plugin version
- [Multiplatform error](kotlin-multiplatform-error) — KMP source sets
