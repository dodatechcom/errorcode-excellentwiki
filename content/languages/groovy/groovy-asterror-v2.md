---
title: "[Solution] Groovy AST Transformation Error"
description: "Fix Groovy AST transformation errors when compile-time code generation fails. Debug AST transformations and annotation processing."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ast", "transformation", "annotation", "compile-time", "groovy"]
weight: 5
---

## What This Error Means

An AST transformation error occurs when Groovy's compile-time code generation fails during AST transformations. This can happen with custom AST transformations, built-in transforms, or annotation processing.

## Common Causes

- Invalid annotation usage
- Custom AST transformation has bugs
- Conflicting AST transformations
- Incorrect transformation target
- Compilation phase issues

## How to Fix

```groovy
// WRONG: Incorrect annotation usage
@Canonical
class Person {
    String name
    int age
    Person() {}  // May conflict with @Canonical generated constructor
}

// CORRECT: Let @Canonical generate constructors
@Canonical
class Person {
    String name
    int age
}
```

```groovy
// WRONG: Custom AST with incorrect phase
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.SOURCE)
@GroovyASTTransformation(phase = CompilePhase.CANONICALIZATION)
class MyTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        // May fail if wrong phase
    }
}

// CORRECT: Use appropriate phase
@GroovyASTTransformation(phase = CompilePhase.SEMANTIC_ANALYSIS)
class MyTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        // Correct phase for type resolution
    }
}
```

```groovy
// WRONG: Missing source unit handling
class MyTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        // No error handling
    }
}

// CORRECT: Handle errors gracefully
class MyTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        try {
            // Transformation code
        } catch (Exception e) {
            source.addError("Transform failed: ${e.message}", nodes[0])
        }
    }
}
```

## Examples

```groovy
// Example 1: Built-in AST transformations
@CompileStatic  // CompilePhase.CANONICALIZATION
class MyService {
    String process(String input) {
        return input.toUpperCase()
    }
}

// Example 2: @Builder AST transform
@Builder
class User {
    String name
    int age
}
def user = User.builder().name("Alice").age(30).build()

// Example 3: Debug AST output
// groovyc -ast groovy --dumpAST MyScript.groovy
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-metaclasserror]({{< relref "/languages/groovy/groovy-metaclasserror" >}}) — metaclass error
- [groovy-casterror]({{< relref "/languages/groovy/groovy-casterror" >}}) — cast error
