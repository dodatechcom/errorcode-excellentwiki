---
title: "Groovy CompileStatic Type Coercion Error"
description: "Fix Groovy CompileStatic errors when strict type checking prevents dynamic Groovy features from working."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When `@CompileStatic` is applied, Groovy enforces Java-like strict type checking, which causes compilation errors for dynamic features like property access on untyped variables, method categories, and dynamic method dispatch.

## Common Causes

- Property access on `def` typed variables without CompileStatic awareness
- Using GDK methods on types that don't declare them statically
- Dynamic method calls that Groovy cannot resolve at compile time
- Type coercion errors between incompatible types
- Missing explicit type declarations where `def` was used

## How to Fix

```groovy
// WRONG: @CompileStatic cannot resolve dynamic property
@CompileStatic
class Foo {
    void bar(def obj) {
        println obj.name  // compile error: can't resolve name on def
    }
}

// CORRECT: Use explicit type or @TypeChecked
@CompileStatic
class Foo {
    void bar(Person obj) {
        println obj.name  // works: Person has name property
    }
}
```

```groovy
// WRONG: GDK methods not visible under CompileStatic
@CompileStatic
class Bar {
    void test() {
        def s = "hello"
        println s.capitalize()  // compile error
    }
}

// CORRECT: Use java.lang.String methods or cast
@CompileStatic
class Bar {
    void test() {
        String s = "hello"
        println s.toUpperCase()  // java method
    }
}
```

## Examples

```groovy
// Example 1: Proper @CompileStatic usage
@CompileStatic
class Calculator {
    int add(int a, int b) { a + b }
    int multiply(int a, int b) { a * b }
}

// Example 2: Mixed static and dynamic
class FlexibleClass {
    @CompileStatic
    int staticMethod(int x) { x * 2 }
    
    def dynamicMethod(def x) { x * 2 }  // dynamic is fine
}

// Example 3: @TypeChecked for partial checking
@TypeChecked
class PartialCheck {
    void test() {
        def list = [1, 2, 3]
        println list.collect { it * 2 }  // @TypeChecked allows this
    }
}
```

## Related Errors

- [Compile error](groovy-compile-error) -- general compilation failures
- [Type mismatch error](groovy-type-mismatch) -- type incompatibility
