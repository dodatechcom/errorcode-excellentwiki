---
title: "[Solution] Julia Macro Expansion Error — How to Fix"
description: "Fix Julia macro expansion errors. Learn how macros work at parse time, debug macro hygiene issues, and write macros that expand correctly in all contexts."
languages: ["julia"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Julia macros are expanded at parse time, before the code is compiled. When a macro generates code that references undefined variables, has incorrect syntax, or violates scoping rules, the expansion fails with a compile-time error.

The most common cause is the macro generating code that references variables not in scope at the call site. Macros operate on expressions, not values, and the generated code must be valid in the context where the macro is called.

Another frequent cause is incorrect expression manipulation. Macros work with `Expr` objects, and if the expression structure is malformed (wrong number of arguments, missing head symbol, etc.), the expansion fails.

Macro hygiene issues cause variable name conflicts. Julia macros are hygienic by default, meaning they generate temporary variable names to avoid conflicts. But if you intentionally want to inject variables into the caller's scope, you need to use `esc()`.

Quoting and interpolation in macros can produce unexpected results. If you interpolate a value into a quoted expression incorrectly, the macro generates code that does not do what you intended.

Multi-line macros that do not handle all code paths can generate incomplete expressions. The macro must return a valid expression in every case.

Macros that depend on runtime values fail because macros execute at parse time, not runtime. You cannot call a function inside a macro definition and expect it to run when the macro is called.

## Common Error Messages

```
ERROR: syntax: "macro" at none:1 expected "end"
```

```
ERROR: UndefVarError: x not defined in generated code
```

```
ERROR: syntax: unexpected "end" in expression
```

```
ERROR: LoadError: macro expansion error — invalid expression
```

## How to Fix It

### Understand macro quoting and interpolation

```julia
# Simple macro with quoting
macro sayhello()
    return :(println("Hello, World!"))
end

@sayhello  # Prints: Hello, World!

# Macro with argument interpolation
macro repeat_str(s, n)
    return :(repeat($s, $n))
end

@repeat_str("ha", 3)  # "hahaha"
```

### Use esc() for caller context variables

```julia
# Without esc — variable is captured in macro scope
macro set_var(val)
    return :(x = $val)  # x is a macro-generated variable
end

# With esc — variable is in caller's scope
macro set_var2(val)
    return esc(:(x = $val))  # x is the caller's x
end

# Usage
x = 0
@set_var2 42
println(x)  # 42
```

### Handle expression structure correctly

```julia
macro my_if(condition, body)
    return quote
        if $condition
            $body
        end
    end
end

# Or using Expr constructor
macro my_if2(condition, body)
    return Expr(:if, condition, body)
end

@my_if true println("yes")
```

### Debug macro expansion

```julia
# See the expanded code
macroexpand(Main, :(@sayhello))

# Or use MacroTools
using MacroTools
println(MacroTools.prettify(macroexpand(Main, :(@repeat_str("ha", 3)))))
```

### Write macros that generate valid expressions

```julia
macro with_cleanup(expr)
    return quote
        local result = try
            $expr
        catch e
            println("Error: ", e)
            nothing
        end
        result
    end
end

@with_cleanup error("test")  # Prints: Error: test
```

## Common Scenarios

- Building a domain-specific language (DSL) with custom macros
- Creating debugging macros that log function calls
- Writing convenience macros that reduce boilerplate code

## Prevent It

- Use `@macroexpand` to inspect the generated code before using a macro
- Keep macros simple and avoid complex logic inside the macro body
- Use `esc()` when you need to reference variables from the caller's scope
