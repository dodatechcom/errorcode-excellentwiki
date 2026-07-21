---
title: "Groovy AST Transformation Compile Error"
description: "Fix Groovy AST transformation compilation errors when custom transformations produce invalid abstract syntax trees."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

AST transformation errors occur during compilation when a Groovy AST transformation generates code that the compiler cannot process, such as invalid syntax trees, missing required nodes, or type mismatches in generated code.

## Common Causes

- Transformation generates code referencing undefined variables
- AST node type is incorrect for the target position
- Transformation does not handle all annotation use cases
- Missing imports in generated code
- Circular transformation dependencies

## How to Fix

```groovy
// WRONG: AST transformation references missing class
@CompileStatic  // may conflict with custom transformations
class MyClass {
    @CustomTransform  // transformation generates code referencing missing import
    void myMethod() {}
}

// CORRECT: Ensure all imports are in generated code
@GroovyASTTransformation
class CustomTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        // add necessary imports to the source unit
    }
}
```

```groovy
// WRONG: Generating invalid AST node structure
def methodNode = new MethodNode("test",
    ClassNode.ACC_PUBLIC,
    ClassHelper.VOID_TYPE,
    [] as Parameter[],
    [] as ClassNode[],
    new BlockStatement())  // may be null

// CORRECT: Validate AST before returning
def block = new BlockStatement()
block.addStatement(new ExpressionStatement(new ConstantExpression("ok")))
def methodNode = new MethodNode("test",
    ClassNode.ACC_PUBLIC,
    ClassHelper.VOID_TYPE,
    [] as Parameter[],
    [] as ClassNode[],
    block)
```

## Examples

```groovy
// Example 1: Simple AST annotation
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@GroovyASTTransformation(class = LoggingTransform)
@interface Loggable {}

// Example 2: AST transformation class
class LoggingTransform implements ASTTransformation {
    void visit(ASTNode[] nodes, SourceUnit source) {
        def method = nodes[1]
        def logCall = new ExpressionStatement(
            new MethodCallExpression(
                new VariableExpression("this"),
                "log",
                new ArgumentListExpression(new ConstantExpression("Called: ${method.name}"))
            )
        )
        method.code.addStatement(logCall)
    }
}
```

## Related Errors

- [AST error](groovy-ast-error) -- AST structure problems
- [Compile error](groovy-compile-error) -- general compilation failures
