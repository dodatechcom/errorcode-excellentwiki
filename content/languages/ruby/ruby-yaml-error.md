---
title: "[Solution] Ruby YAML — safe_load, Permitted Classes, Psych Errors"
description: "Fix Ruby YAML errors. Handle YAML.safe_load, permitted classes, aliases, and Psych syntax issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, yaml, psych, safe_load, deserialization"]
severity: "error"
---

# Ruby YAML Errors

## Error Message

```
Psych::DisallowedClass: Tried to load unspecified class: Symbol
# or
Psych::BadAlias: Unknown alias: default
# or
Psych::SyntaxError: (<unknown>): did not find expected ...
```

## Common Causes

- Using `YAML.load` instead of `YAML.safe_load` on untrusted data
- Missing permitted classes when loading YAML with Symbols, Dates, or custom objects
- YAML aliases disabled by default in safe_load but expected by data
- Malformed YAML syntax from manual string building

## Solutions

### Solution 1: Use YAML.safe_load with Permitted Classes

Always use `safe_load` and explicitly permit the classes you need.

```ruby
require "yaml"

# BAD: loads arbitrary objects
YAML.load(user_input)  # dangerous!

# GOOD: safe_load with permitted classes
yaml_str = 'name: alice scores: [90, 85]'
YAML.safe_load(yaml_str)
# => {"name"=>"alice", "scores"=>[90, 85]}

# With Symbols and Dates
yaml_str = 'status: :active created: 2026-01-01'
YAML.safe_load(yaml_str, permitted_classes: [Symbol, Date])
# => {"status"=>:active, "created"=>Sun, 01 Jan 2026}
```

### Solution 2: Handle YAML Aliases

Enable aliases when YAML data uses anchor/alias syntax.

```ruby
yaml_with_aliases = <<~YAML
defaults: &defaults
  adapter: postgresql
  encoding: utf8
production:
  <<: *defaults
  database: myapp_prod
YAML

# BAD: aliases not permitted by default
YAML.safe_load(yaml_with_aliases)  # Psych::BadAlias

# GOOD: enable aliases
YAML.safe_load(yaml_with_aliases, aliases: true)
# => {"defaults"=>{"adapter"=>"postgresql", ...}, "production"=>{"adapter"=>"postgresql", ...}}
```

### Solution 3: Fix Psych YAML Syntax Errors

Build YAML properly instead of string interpolation.

```ruby
# BAD: manual YAML string can have syntax errors
yaml = "name: #{name}\nscores: #{scores}"  # scores could break syntax

# GOOD: use YAML.dump
data = { name: "alice", scores: [90, 85] }
yaml = YAML.dump(data)
# => "---\nname: alice\nscores:\n- 90\n- 85\n"

# Parse back
YAML.safe_load(yaml)  # => {"name"=>"alice", "scores"=>[90, 85]}
```

### Solution 4: Handle Custom Classes in YAML

Use `init_with` and `encode_with` for custom YAML serialization.

```ruby
class Point
  attr_reader :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def encode_with(coder)
    coder["x"] = x
    coder["y"] = y
  end

  def init_with(coder)
    @x = coder["x"]
    @y = coder["y"]
  end
end

point = Point.new(10, 20)
yaml = YAML.dump(point)
loaded = YAML.safe_load(yaml, permitted_classes: [Point])
loaded.x  # => 10
```

## Prevention Tips

- Always use `YAML.safe_load` instead of `YAML.load` on untrusted input
- Explicitly list `permitted_classes` and `aliases: true` when needed
- Use `YAML.dump` to serialize instead of string interpolation
- Validate YAML syntax with `YAML.safe_load` before processing

## Related Errors

- [TypeError]({{< relref "/languages/ruby/type-error" >}})
- [SyntaxError]({{< relref "/languages/ruby/syntax-error" >}})
- [Ruby JSON Error]({{< relref "/languages/ruby/ruby-json-error" >}})
