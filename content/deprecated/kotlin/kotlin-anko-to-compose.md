---
title: "[Solution] Deprecated Function Migration: Anko to Jetpack Compose"
description: "Migrate from deprecated Anko DSL to Jetpack Compose for Android UI."
deprecated_function: "Anko"
replacement_function: "Jetpack Compose"
languages: ["kotlin"]
deprecated_since: "Deprecated 2019"
---

# [Solution] Deprecated Function Migration: Anko to Jetpack Compose

The `Anko` has been deprecated in favor of `Jetpack Compose`.

## Migration Guide

Anko was deprecated in 2019. Jetpack Compose is Google's modern declarative UI toolkit.

## Before (Deprecated)

```kotlin
import org.jetbrains.anko.*

verticalLayout {
    val name = editText { hint = "Name" }
    val age = editText { hint = "Age" }
    button("Submit") {
        onClick {
            toast("Hello, ${name.text}!")
        }
    }
}
```

## After (Modern)

```kotlin
@Composable
fun UserForm() {
    var name by remember { mutableStateOf("") }
    var age by remember { mutableStateOf("") }

    Column {
        TextField(
            value = name,
            onValueChange = { name = it },
            label = { Text("Name") }
        )
        Button(onClick = { /* handle submit */ }) {
            Text("Submit")
        }
    }
}
```

## Key Differences

- Compose uses @Composable functions
- State managed with remember/mutableStateOf
- No XML layouts needed
- Declarative UI paradigm
