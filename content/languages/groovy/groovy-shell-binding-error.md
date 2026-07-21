---
title: "Groovy GroovyShell Script Binding Error"
description: "Fix Groovy GroovyShell binding errors when executing scripts with incorrect variable binding setup."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

GroovyShell binding errors occur when a script executed via GroovyShell cannot access variables from its binding, either because the binding was not set up correctly or the script references undefined variables.

## Common Causes

- Variable not added to binding before script execution
- Script modifies binding variables but changes are not visible to caller
- Binding variable name has typo in script vs binding setup
- Using wrong GroovyShell instance for execution
- Script classloader differs from calling code

## How to Fix

```groovy
// WRONG: Variable not in binding
def binding = new Binding()
binding.setVariable("x", 10)
def shell = new GroovyShell(binding)
shell.evaluate("println y")  // MissingPropertyException

// CORRECT: Add all required variables
def binding = new Binding()
binding.setVariable("x", 10)
binding.setVariable("y", 20)
def shell = new GroovyShell(binding)
shell.evaluate("println y")
```

```groovy
// WRONG: Assuming script changes are visible
def binding = new Binding()
binding.setVariable("result", 0)
def shell = new GroovyShell(binding)
shell.evaluate("result = 42")
println binding.getVariable("result")  // 0, not 42!

// CORRECT: Read back after execution
shell.evaluate("result = 42")
println binding.getVariable("result")  // 42 -- need to check after run
```

## Examples

```groovy
// Example 1: Pass variables to script
def binding = new Binding()
binding.setVariable("name", "Alice")
binding.setVariable("age", 30)
def shell = new GroovyShell(binding)
def result = shell.evaluate("""
    def greeting = "Hello, \${name}! Age: \${age}"
    greeting
""")
println result

// Example 2: Script with imports
def shell = new GroovyShell()
def result = shell.evaluate("""
    import groovy.json.JsonOutput
    def data = [name: "test", value: 123]
    JsonOutput.prettyPrint(JsonOutput.toJson(data))
""")
println result

// Example 3: Secure binding
def binding = new Binding()
binding.setVariable("safeVar", "allowed")
binding.setProperty("secret", "hidden")  // may not be accessible
```

## Related Errors

- [Binding error](binding-error) -- variable binding problems
- [Missing property error](groovy-missingproperty) -- property not found
