---
title: "[Solution] Ruby Marshal — Dump/Load, TypeMismatchError, Singleton Errors"
description: "Fix Ruby Marshal errors. Handle TypeMismatchError, singleton objects, incompatible dump, and load failures."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, marshal, serialization, dump, load"]
severity: "error"
---

# Ruby Marshal Errors

## Error Message

```
TypeError: can't dump anonymous class #<Class:0x...>
# or
TypeError: singleton object not found
# or
ArgumentError: instance of {ClassName} needs to have method `marshal_load`
```

## Common Causes

- Dumping anonymous classes, singleton methods, or singleton classes
- Loading Marshal data serialized by a different Ruby version
- Using Marshal with objects containing file handles, IO, or Proc objects
- Loading Marshal data that references classes not yet defined

## Solutions

### Solution 1: Avoid Dumping Unsupported Object Types

Marshal cannot dump anonymous classes, singleton methods, or IO objects.

```ruby
# BAD: anonymous class
obj = Class.new.new
Marshal.dump(obj)  # TypeError: can't dump anonymous class

# GOOD: use named classes
class Config
  attr_accessor :setting
  def initialize(setting)
    @setting = setting
  end
end

Marshal.dump(Config.new("prod"))  # => "\x04\x08o\x09Config\x06:\x0fsettingI\"\bprod"

# BAD: singleton methods
obj = Object.new
def obj.special; end
Marshal.dump(obj)  # TypeError: singleton method

# GOOD: use instance methods
class MyObject
  def special; "value"; end
end
Marshal.dump(MyObject.new)
```

### Solution 2: Handle Version Incompatibilities

Marshal format changes between Ruby versions. Use JSON or YAML for cross-version data.

```ruby
# Marshal format is version-specific
data = Marshal.dump("hello")  # Ruby 3.x format

# On a different Ruby version, load may fail
# Marshal.load(data)  # => may raise TypeError

# GOOD: use JSON for portable serialization
require "json"
JSON.dump({ key: "value" })  # => '{"key":"value"}'
JSON.parse('{"key":"value"}')  # => {"key"=>"value"}

# Or implement marshal_load/marshal_dump for control
class Person
  attr_reader :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def marshal_dump
    { name: @name, age: @age }
  end

  def marshal_load(data)
    @name = data[:name]
    @age = data[:age]
  end
end
```

### Solution 3: Use Marshal with Excluded Fields

Use `exclude?` or custom methods to skip sensitive data during serialization.

```ruby
class User
  attr_reader :name, :password

  def initialize(name, password)
    @name = name
    @password = password
  end

  def marshal_dump
    { name: @name }  # exclude password
  end

  def marshal_load(data)
    @name = data[:name]
    @password = nil
  end
end

user = User.new("alice", "secret")
dumped = Marshal.dump(user)
loaded = Marshal.load(dumped)
loaded.password  # => nil
```

### Solution 4: Safe Marshal.load with Allowed Classes

Use `Marshal.load` with permitted class lists to prevent arbitrary object instantiation.

```ruby
# Marshal.load with trusted data only
data = Marshal.dump("hello")
Marshal.load(data)  # => "hello"

# For untrusted data, use JSON or YAML instead
require "json"
data = '{"name": "alice"}'
JSON.parse(data)  # => {"name"=>"alice"}

# Marshal.load with restricted classes (Ruby 2.6+)
Marshal.load(data, permitted_classes: [Config])
```

## Prevention Tips

- Never use Marshal for untrusted data — it can instantiate arbitrary objects
- Prefer JSON or YAML for data exchange between Ruby versions
- Implement `marshal_dump`/`marshal_load` for custom serialization control
- Avoid storing file handles, Proc objects, or singletons in Marshal data

## Related Errors

- [TypeError]({{< relref "/languages/ruby/type-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [Ruby YAML Error]({{< relref "/languages/ruby/ruby-yaml-error" >}})
