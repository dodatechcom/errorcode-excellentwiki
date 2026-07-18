---
title: "[Solution] Groovy Closure Call Wrong Number of Arguments"
description: "Fix Groovy closure call error with wrong number of arguments. Handle closure delegation and argument matching."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The closure call error occurs when a Groovy closure is invoked with a number of arguments that does not match its definition. Groovy closures enforce argument count matching at runtime.

## Why It Happens

- Closure defined with fixed parameters but called with wrong count: The closure expects exactly N arguments but receives M.
- Spread operator generates wrong number of arguments: The `*.` operator may produce unexpected argument counts.
- Delegation changes effective argument context: The delegate object may intercept method calls.
- Closure used as SAM interface with wrong arity: The functional interface expects a different number of parameters.
- Closure argument count varies dynamically: The closure does not use variable arguments.

## How to Fix It

Use flexible parameter syntax with variable arguments:

```groovy
// WRONG: Fixed parameter count
def add = { a, b -> a + b }
add(1)  // Error: Wrong number of arguments

// CORRECT: Variable arguments
def sum = { Object[] args -> args.sum() }
sum(1)
sum(1, 2, 3)
```

Check argument count before calling:

```groovy
def myClosure = { a, b, c -> "${a}-${b}-${c}" }

def args = [1, 2, 3]
if (args.size() == 3) {
    myClosure(*args)
} else {
    println "Expected 3 arguments, got ${args.size()}"
}
```

Use optional parameters with defaults:

```groovy
def configure = { String name, int timeout = 30, boolean verbose = false ->
    println "Name: $name, Timeout: $timeout, Verbose: $verbose"
}

configure("server")           // Uses defaults
configure("server", 60)       // Custom timeout
configure("server", 60, true) // All arguments
```

Handle spread operator carefully:

```groovy
def items = [[1, 2], [3, 4, 5]]
// WRONG: Different argument counts causes error
items.collect { it.collect { a, b -> a + b } }

// CORRECT: Variable arguments
items.collect { it.collect { args -> args.sum() } }
```

Use curry for partial application:

```groovy
def multiply = { a, b -> a * b }
def double = multiply.curry(2)
println double(5)  // 10
```

## Common Mistakes

- Defining closure with exact parameters instead of varargs when argument count may vary.
- Not accounting for delegate changing closure behavior.
- Forgetting that implicit `it` counts as one parameter.
- Using spread operator on lists with different sizes.
- Not understanding that closure delegation affects method resolution.

## Related Pages

- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-metaclass-error]({{< relref "/languages/groovy/groovy-metaclasserror-v2" >}}) - metaclass error
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-spock-error]({{< relref "/languages/groovy/groovy-spock-error" >}}) - Spock test errors
