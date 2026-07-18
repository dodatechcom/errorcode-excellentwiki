---
title: "[Solution] Groovy AST Transformation Error"
description: "Fix Groovy AST transformation errors. Resolve compile-time code generation and annotation processing issues."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

AST transformation errors occur during Groovy compilation when compile-time code transformations fail. These errors affect annotations like @Builder, @Immutable, and custom AST transforms.

## Why It Happens

- Annotation applied to incompatible construct: The annotation does not support the target element type.
- AST transform has bugs in node manipulation: The transform code has incorrect AST node handling.
- Circular dependency in transform processing: Transforms depend on each other in a cycle.
- Transform requires specific Groovy version features: The transform uses features not available in the current Groovy version.
- Missing imports for generated code: The transform generates code that references unavailable classes.

## How to Fix It

Verify annotation compatibility with target:

```groovy
import groovy.transform.CompileStatic

// WRONG: @CompileStatic on script with dynamic features
@CompileStatic
def dynamicMethod() {
    def obj = new Expando()
    obj.someMethod()  // May fail under @CompileStatic
}

// CORRECT: Remove @CompileStatic or use dynamic features carefully
def dynamicMethod() {
    def obj = new Expando()
    obj.someMethod()
}
```

Check AST transform requirements:

```groovy
import groovy.transform.builder.*

// WRONG: @Builder on class without proper setup
@Builder
class Config { }

// CORRECT: Specify builder strategy
@Builder(builderStrategy = BuilderStrategy.ONE_ARG_CONSTRUCTOR)
class Config { 
    String name
    int timeout
}
```

Handle compilation errors with error messages:

```groovy
// Use @Grab for required dependencies
@Grab('org.apache.commons:commons-lang3:3.12.0')
import org.apache.commons.lang3.StringUtils

def result = StringUtils.capitalize("hello")
```

Use compilationCustomizers for complex transforms:

```groovy
def config = new CompilerConfiguration()
config.addCompilationCustomizers(new ASTTransformationCustomizer())
```

Use @CompileStatic for type checking:

```groovy
import groovy.transform.CompileStatic

@CompileStatic
class MyService {
    String process(String input) {
        input.toUpperCase()  // Type checked at compile time
    }
}
```

Use @TypeChecked for partial type checking:

```groovy
import groovy.transform.TypeChecked

@TypeChecked
def process() {
    def list = [1, 2, 3]
    list.collect { it * 2 }  // Type checked
}
```

Handle AST transformation conflicts:

```groovy
// Some transforms conflict with each other
// Test thoroughly when combining transforms
@Builder
@Immutable
class Config {
    String name
}
```

## Common Mistakes

- Using annotations on wrong program elements. Check the annotation's @Target meta-annotation.
- Not reading AST transform documentation thoroughly. Each transform has specific requirements.
- Forgetting that transforms run at compile time. Runtime values are not available.
- Mixing incompatible AST transformations. Some transforms conflict with each other.
- Not testing with the exact Groovy version used in production.
- Not understanding that @CompileStatic changes runtime behavior.
- Forgetting that AST transforms can generate code that references unavailable classes.

## Related Pages

- [groovy-metaclass-error]({{< relref "/languages/groovy/groovy-metaclasserror-v2" >}}) - metaclass error
- [groovy-deprecated-api]({{< relref "/languages/groovy/groovy-deprecated-api" >}}) - deprecated API
- [groovy-compiled-class-error]({{< relref "/languages/groovy/groovy-compiled-class-error" >}}) - compiled class error
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
