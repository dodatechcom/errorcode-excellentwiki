---
title: "[Solution] Kotlin DSL Builder — @DslMarker and Implicit Receiver Conflict"
description: "Fix Kotlin DSL builder errors with @DslMarker and implicit receiver conflicts. Learn correct type-safe builder patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1032
---

## What This Error Means

DSL builder errors occur when implicit receivers in nested scopes conflict, or when @DslMarker prevents accidental access to outer receiver functions. These are common in type-safe builder patterns.

## Common Causes

- Nested DSL scopes accidentally accessing outer receiver
- Missing @DslMarker annotation causing ambiguity
- Builder function not inline, preventing non-local return
- Conflicting extension functions on different receivers

```kotlin
// Accidentally accessing outer receiver
html {
    head {
        title { "Title" }
        meta { }  // Can accidentally call html-level functions
    }
}
```

## How to Fix

**1. Use @DslMarker to restrict scope**

```kotlin
@DslMarker
annotation class HtmlDsl

@HtmlDsl
class HtmlBuilder {
    fun head(init: HeadBuilder.() -> Unit) { ... }
}

@HtmlDsl
class HeadBuilder {
    fun title(init: TitleBuilder.() -> Unit) { ... }
    fun meta() { ... }
}
```

**2. Make builder functions inline**

```kotlin
// CORRECT: Inline for non-local return support
inline fun html(init: HtmlBuilder.() -> Unit): HtmlBuilder {
    return HtmlBuilder().apply(init)
}
```

**3. Use @ReceiverContext for explicit receiver access**

```kotlin
@DslMarker
annotation class RouterDsl

@RouterDsl
class RouteBuilder {
    fun path segment: String) { ... }
}

@RouterDsl
class RouterBuilder {
    @RouterDsl
    fun route(path: String, init: RouteBuilder.() -> Unit) { ... }
}
```

**4. Explicit receiver qualification**

```kotlin
html {
    head {
        this@html.title = "Page Title"  // Explicit outer receiver
    }
}
```

## Examples

```kotlin
// Example 1: JSON builder DSL
@DslMarker
annotation class JsonDsl

@JsonDsl
class JsonObjectBuilder {
    private val map = mutableMapOf<String, Any>()

    infix fun String.to(value: Any) { map[this] = value }
    fun obj(init: JsonObjectBuilder.() -> Unit) = JsonObjectBuilder().apply(init).also { map["nested"] = it }
    fun build(): Map<String, Any> = map
}

fun json(init: JsonObjectBuilder.() -> Unit) = JsonObjectBuilder().apply(init).build()

val result = json {
    "name" to "Alice"
    "age" to 30
}

// Example 2: HTML builder
fun html(init: HTML.() -> Unit) = HTML().apply(init)

@DslMarker
annotation class HtmlDsl

@HtmlDsl
class HTML {
    fun head(init: Head.() -> Unit) = Head().apply(init)
    fun body(init: Body.() -> Unit) = Body().apply(init)
}

// Example 3: Gradle-style dependency builder
class DependencyBuilder {
    val dependencies = mutableListOf<String>()

    fun implementation(dep: String) { dependencies.add("implementation(\"$dep\")") }
    fun testImplementation(dep: String) { dependencies.add("testImplementation(\"$dep\")") }
}

fun dependencies(init: DependencyBuilder.() -> Unit) = DependencyBuilder().apply(init)
```

## Related Errors

- [Extension error](extension-error) — extension function issue
- [Inline function error](kotlin-inline-function-error) — inline issues
- [DSL builder scope error](kotlin-dsl-builder-error) — builder scope
