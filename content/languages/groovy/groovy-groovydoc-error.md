---
title: "Groovy Groovydoc Comment Syntax Error"
description: "Fix Groovy Groovydoc comment syntax errors when documentation comments use incorrect annotation or tag formats."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovydoc comment errors occur when the documentation generator encounters malformed comment syntax, invalid tags, or mismatched braces in Groovy documentation comments.

## Common Causes

- Missing closing brace in `{@link}` or `{@code}` tags
- Using `@param` with wrong parameter name
- Nested Groovydoc comments that confuse the parser
- Invalid HTML within Groovydoc blocks
- `@return` tag on a void method

## How to Fix

```groovy
// WRONG: Unclosed {@link tag
/**
 * Processes data using {@link java.util.List
 */
void process(List data) {}  // Groovydoc warning

// CORRECT: Close the tag
/**
 * Processes data using {@link java.util.List}.
 */
void process(List data) {}
```

```groovy
// WRONG: @param name does not match
/**
 * @param x the input value
 */
void process(int y) {}  // mismatch

// CORRECT: Match parameter names
/**
 * @param y the input value
 */
void process(int y) {}
```

## Examples

```groovy
/**
 * Calculates the sum of two numbers.
 *
 * @param a first number
 * @param b second number
 * @return the sum of a and b
 * @see {@link Math#addExact(int, int)}
 */
int sum(int a, int b) {
    return a + b
}

/**
 * Configuration holder for application settings.
 *
 * <p>Usage:
 * <pre><code>
 * def config = new AppConfig()
 * config.host = "localhost"
 * </code></pre>
 *
 * @author Developer
 * @since 1.0
 */
class AppConfig {
    String host
    int port
}
```

## Related Errors

- [Annotation error](groovy-annotation-error) -- annotation syntax issues
- [Compile error](groovy-compile-error) -- compilation failures
