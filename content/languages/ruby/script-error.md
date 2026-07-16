---
title: "[Solution] Ruby ScriptError — Script Error Fix"
description: "Fix Ruby ScriptError. Handle script-level errors including load errors, syntax errors, and not-implemented errors."
languages: ["ruby"]
severities: ["error"]
error_types: ["script"]
tags: ["script_error", "script", "load", "syntax", "not_implemented"]
weight: 340
---

# ScriptError — Script Error Fix

A `ScriptError` is raised when there's an error in the script itself. It's the parent class for `LoadError`, `SyntaxError`, and `NotImplementedError`.

## Description

`ScriptError` is an abstract exception class. You won't typically see it directly — instead you'll see its subclasses. It represents errors in the script's code or loading process.

Common scenarios:

- **LoadError** — file not found or can't be loaded.
- **SyntaxError** — invalid Ruby syntax.
- **NotImplementedError** — abstract method not overridden.
- **Script error in require** — error in required file.

## Common Causes

```ruby
# Cause 1: LoadError (subclass of ScriptError)
require 'nonexistent_gem'  # LoadError

# Cause 2: SyntaxError (subclass of ScriptError)
eval("def foo(")  # SyntaxError

# Cause 3: NotImplementedError (subclass of ScriptError)
class Abstract
  def do_something
    raise NotImplementedError
  end
end

# Cause 4: Script error in required file
# bad_file.rb contains invalid syntax
require 'bad_file'  # ScriptError (SyntaxError)
```

## Solutions

### Fix 1: Rescue ScriptError for all script errors

```ruby
begin
  risky_operation
rescue ScriptError => e
  puts "Script error: #{e.class}: #{e.message}"
end
```

### Fix 2: Rescue specific ScriptError subclasses

```ruby
begin
  require 'some_gem'
rescue LoadError
  puts "Gem not installed"
rescue SyntaxError
  puts "Syntax error in loaded file"
rescue NotImplementedError
  puts "Method not implemented"
end
```

### Fix 3: Validate scripts before execution

```ruby
# Check syntax before running
result = system("ruby -c script.rb")
unless result
  puts "Script has syntax errors"
end
```

### Fix 4: Use proper error hierarchy in abstract classes

```ruby
class Base
  def process
    raise NotImplementedError, "#{self.class} must implement #process"
  end
end

class Concrete < Base
  def process
    # Implementation
  end
end
```

## Related Errors

- [LoadError](load-error) — cannot load such file.
- [SyntaxError](syntax-error) — syntax error in code.
- [NotImplementedError](not-implemented) — method not implemented.
