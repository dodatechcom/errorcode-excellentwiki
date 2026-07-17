---
title: "[Solution] Ruby NameError — Uninitialized Constant Fix"
description: "Fix Ruby NameError: uninitialized constant. Learn why Ruby can't find the constant and how to properly require files and define constants."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A `NameError` is raised when Ruby encounters an undefined variable or constant. The most common form is `uninitialized constant`, which means Ruby doesn't recognize the constant name in the current scope.

## Common Causes

- Missing `require` statement for a file defining the constant
- Typo in constant name
- Wrong scope for the constant
- Missing module/class namespace

## How to Fix

```ruby
# WRONG: Missing require
# In file: user.rb
class User; end

# In main script:
user = User.new  # NameError: uninitialized constant User

# CORRECT: Require the file
require_relative 'user'
user = User.new
```

```ruby
# WRONG: Typo in constant name
class MyService
  CONFIG = { timeout: 30 }
end
MyService::CONFG  # NameError: uninitialized constant MyService::CONFG

# CORRECT: Use correct constant name
MyService::CONFIG  # {:timeout=>30}
```

```ruby
# WRONG: Wrong scope
module MyApp
  class Config
    TIMEOUT = 30
  end
end
TIMEOUT  # NameError: uninitialized constant TIMEOUT

# CORRECT: Use full namespace
MyApp::Config::TIMEOUT  # 30
```

```ruby
# WRONG: Constant in wrong file order
# file1.rb: MyClass.new (class defined in file2.rb)
# file2.rb: class MyClass; end

# CORRECT: Ensure correct load order
require_relative 'file2'
require_relative 'file1'
```

## Examples

```ruby
# Example 1: Undefined constant
UNKNOWN_CONSTANT  # NameError: uninitialized constant UNKNOWN_CONSTANT

# Example 2: Module namespace
module Admin
  class User; end
end
User.new  # NameError: uninitialized constant User
Admin::User.new  # OK

# Example 3: Constant from another gem
JSON.parse("{}")  # Works if json is required
```

## Related Errors

- [NoMethodError](nomethoderror-ruby) — undefined method
- [LoadError](loaderror-ruby) — cannot load such file
- [SyntaxError](syntaxerror-ruby) — syntax error
