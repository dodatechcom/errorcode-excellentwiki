---
title: "[Solution] Groovy Deprecated API Usage Warning"
description: "Fix Groovy deprecated API warnings. Update code to use current API alternatives and remove obsolete method calls."
languages: ["groovy"]
error-types: ["warning"]
severities: ["medium"]
weight: 5
---

## What This Error Means

Deprecated API warnings indicate that your code uses methods, classes, or features that are marked for removal in future Groovy versions. These warnings help you update code before breaking changes occur.

## Why It Happens

- Using methods removed in newer Groovy versions: The method was deprecated and may be removed.
- Calling deprecated GDK extension methods: Groovy Development Kit methods that have been superseded.
- Using legacy collection APIs: Old-style collection methods replaced by more efficient alternatives.
- Relying on Groovy 1.x compatibility features: Features that existed for backward compatibility.
- Using deprecated annotation attributes: Annotation parameters that have been renamed or removed.

## How to Fix It

Replace deprecated methods with current alternatives:

```groovy
// WRONG: Deprecated method
def result = list.collectMany { it.subList(0, 2) }

// CORRECT: Use flatten
def result = list.collect { it.subList(0, 2) }.flatten()
```

Update deprecated annotation usage:

```groovy
// WRONG: Deprecated attribute
@groovy.transform.PackageScope
class MyClass { }

// CORRECT: Use @PackageScopeClass
@groovy.transform.PackageScopeClass
class MyClass { }
```

Handle deprecated String methods:

```groovy
// WRONG: Deprecated
def words = sentence.tokenize(" ")

// CORRECT: Use split
def words = sentence.split(" ").toList()
```

Use modern Groovy APIs:

```groovy
// WRONG: Old collect
def sizes = list.collect { it.length() }

// CORRECT: More idiomatic spread operator
def sizes = list*.length()
```

Use @Deprecated annotation in your own code:

```groovy
@Deprecated
void oldMethod() {
    // Deprecated implementation
}

void newMethod() {
    // New implementation
}
```

Check Groovy version compatibility:

```groovy
// In build.gradle
plugins {
    id 'groovy'
}

groovy {
    targetCompatibility = '1.8'
    sourceCompatibility = '1.8'
}
```

Use @SuppressWarnings for intentional deprecations:

```groovy
@SuppressWarnings('deprecation')
void legacyMethod() {
    // Using deprecated API intentionally
}
```

Migrate from deprecated GDK methods:

```groovy
// OLD: Deprecated
def result = list.collectMany { it.subList(0, 2) }

// NEW: Current API
def result = list.collect { it.subList(0, 2) }.flatten()
```

## Common Mistakes

- Ignoring deprecation warnings until upgrade breaks code. Address warnings proactively.
- Not checking Groovy version compatibility in build files. Use version ranges for dependencies.
- Using deprecated features in new code. Always use current APIs.
- Not testing code after updating deprecated APIs. Ensure behavior remains the same.
- Forgetting that deprecation warnings may become errors in future versions.
- Not checking deprecation status of third-party libraries.
- Assuming deprecation warnings are harmless. They indicate potential breaking changes.

## Related Pages

- [groovy-ast-error]({{< relref "/languages/groovy/groovy-asterror-v2" >}}) - AST transformation errors
- [groovy-compiled-class-error]({{< relref "/languages/groovy/groovy-compiled-class-error" >}}) - compiled class errors
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-metaclass-error]({{< relref "/languages/groovy/groovy-metaclasserror-v2" >}}) - metaclass error
