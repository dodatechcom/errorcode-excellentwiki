---
title: "[Solution] Ruby NameError — Undefined Local Variable Fix"
description: "Fix Ruby NameError: undefined local variable or method. Check variable scope, spelling, and require statements."
languages: ["ruby"]
severities: ["error"]
error_types: ["name"]
tags: ["nameerror", "variable", "undefined", "scope"]
weight: 40
---

# NameError — Undefined Local Variable Fix

A `NameError` is raised when Ruby encounters an identifier (variable or constant) that hasn't been defined in the current scope.

## Description

Ruby variables must be defined before they're used. A `NameError` means Ruby doesn't recognize the name you've referenced. This often happens due to typos, scope issues, or missing requires.

Common scenarios:

- **Typo in variable name** — `naem` instead of `name`.
- **Variable out of scope** — defined inside a method but referenced outside.
- **Missing require** — constant from another file not loaded.
- **Method called as variable** — missing parentheses or receiver.

## Common Causes

```ruby
# Cause 1: Typo in variable name
greeting = "Hello"
puts greetng  # NameError: undefined local variable or method 'greetng'

# Cause 2: Variable defined in wrong scope
def set_name
  name = "Alice"
end
puts name  # NameError: undefined local variable or method 'name'

# Cause 3: Missing require
puts JSON.parse('{"key": "value"}')  # NameError if json not required

# Cause 4: Constant not defined
puts MY_CONSTANT  # NameError: uninitialized constant MY_CONSTANT
```

## Solutions

### Fix 1: Check variable names for typos

```ruby
# Wrong
user_nmae = "Alice"
puts user_name  # NameError

# Correct
user_name = "Alice"
puts user_name  # "Alice"
```

### Fix 2: Return values from methods instead of using local variables

```ruby
# Wrong
def get_name
  name = "Alice"
end
puts name  # NameError — name is local to the method

# Correct
def get_name
  "Alice"
end
puts get_name  # "Alice"
```

### Fix 3: Require necessary files

```ruby
# Wrong
data = JSON.parse('{"key": "value"}')  # NameError

# Correct
require 'json'
data = JSON.parse('{"key": "value"}')
```

### Fix 4: Define constants before use

```ruby
# Wrong
puts MAX_RETRIES  # NameError

# Correct
MAX_RETRIES = 3
puts MAX_RETRIES  # 3
```

## Related Errors

- [NoMethodError](no-method-error) — undefined method on an object.
- [LoadError](load-error) — cannot load such file.
- [ArgumentError](argument-error) — wrong number of arguments.
