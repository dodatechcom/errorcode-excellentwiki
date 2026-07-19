---
title: "[Solution] IntelliJ IDEA Surround with error"
description: "Fix IntelliJ IDEA surround with template failures. Resolve code wrapping, block statement, and template application errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "surround-with", "templates", "code-generation", "refactoring"]
severity: "error"
---

# Surround with error

## Error Message

```
Surround with error
Cannot surround: selection contains incomplete statements
Surround with try-catch: no exceptions caught in scope
Surround with if: boolean expression required
Template 'Surround with Live Template' failed: parse error
```

## Common Causes

- Selected code contains incomplete or syntactically invalid statements
- The surround template requires a specific code structure not present
- Boolean expression is required for if/while templates but not provided
- Live Template for surround is misconfigured or corrupted
- Selection spans multiple scopes or contains declarations

## Solutions

### Solution 1: Use Surround With Menu

Access the Surround With menu to choose from available code wrapping templates.

```
# Select the code to surround:
# 1. Highlight the statements (click and drag)
# 2. Press Ctrl+Alt+T (Windows/Linux) or ⌘⌥T (macOS)

# Available templates:
#   if / if-else / else
#   while / for / for-each
#   try / try-catch / try-finally / try-catch-finally
#   synchronized
#   Comment with block comment
#   Live Templates (custom templates)

# Select template → Press Enter
# The IDE wraps the selected code
```

### Solution 2: Fix Boolean Expression for If Templates

Ensure the code produces a boolean value when using if/while surround templates.

```java
// Before selecting for surround:
// Ensure you have a boolean expression:

// Good (boolean expression):
boolean isActive = user.isActive();
if (isActive) {  // ready for surround
    processUser(user);
}

// For while/for templates:
// The selection should contain the loop body
// The IDE will ask for the condition

// After surround:
if (user.isActive()) {
    processUser(user);
}
```

### Solution 3: Create Custom Surround Live Templates

Create custom surround templates for frequently used code patterns.

```
File → Settings → Editor → Live Templates
# Select 'Surround Templates' group
# Click '+' → Live Template

# Abbreviation: sync
# Description: Surround with synchronized block
# Template text:
synchronized ($END$) {
    $SELECTION$
}

# Applicable in: Java → Statement
# Click 'Edit Variables' to configure
# Apply → Now available via Ctrl+Alt+T

# Example custom template - null check:
if ($SELECTION$ != null) {
    $END$
}
```

### Solution 4: Select Correct Code Scope

Ensure the selection contains complete statements that can be safely wrapped.

```
# Correct selection for surround:
# Select complete statements, not partial expressions:

// Good selection:
String result = calculate();
logger.info(result);  // select both lines

// Bad selection (partial):
String result = calculate();
logger.info(res  // selection cuts mid-expression

# Tips for proper selection:
# 1. Click at the start of first line
# 2. Shift+Click at the end of last line
# 3. Or use keyboard: Home → Shift+Down → Shift+End
# 4. Verify selection includes complete lines

# For multiple blocks:
# Select entire blocks including braces
```

## Prevention Tips

- Use Surround With (Ctrl+Alt+T) for quick code wrapping instead of manual typing
- Create custom Live Templates for your team's common code patterns
- Use Surround With Comment to quickly add block comments around code sections
- The 'Surround with Live Template' option provides the most flexible templates

## Related Errors

- [Extract Error]({{< relref "/tools/intellij/extract-error" >}})
- [Generate Error]({{< relref "/tools/intellij/generate-error" >}})
- [Refactoring Failed]({{< relref "/tools/intellij/refactoring-error" >}})
