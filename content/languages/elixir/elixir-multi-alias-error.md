---
title: "[Solution] Elixir Multi-alias Error -- Incorrect Alias Expansion"
description: "Fix Elixir multi-alias errors when using as: and expand: options incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Multi-alias Error

This error occurs when the `alias` or `import` module multi-alias features (`as:`, `except:`, `only:`) are used incorrectly.

## Common Causes

- Using `only:` with module names instead of function names
- Multi-alias `as:` creating conflicting names
- Importing functions with wrong arity
- Referencing aliased modules without the alias prefix

## How to Fix

### Use only: with specific functions

```elixir
# WRONG: only: expects function names, not module
import String, only: [upcase: 1, downcase: 1]

# CORRECT: import specific functions
import String, only: [upcase: 1, downcase: 1]
```

### Use multi-alias correctly

```elixir
# WRONG: incorrect multi-alias
alias MyApp.{User, Post, Comment, as: C}  # as: not valid here

# CORRECT: use separate alias for renamed module
alias MyApp.{User, Post, Comment}
alias MyApp.Comment, as: C
```

## Examples

```elixir
alias MyApp.Accounts.{User, UserToken}
alias MyApp.Blog.{Post, Comment}

def create_post(%User{} = user, attrs) do
  Post.create(attrs, user.id)
end
```
