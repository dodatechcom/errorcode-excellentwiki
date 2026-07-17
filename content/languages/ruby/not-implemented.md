---
title: "[Solution] Ruby NotImplementedError — Method Not Implemented Fix"
description: "Fix Ruby NotImplementedError. Implement abstract methods in subclasses and use proper inheritance patterns."
languages: ["ruby"]
severities: ["error"]
error_types: ["not_implemented"]
weight: 350
---

# NotImplementedError — Method Not Implemented Fix

A `NotImplementedError` is raised when an abstract method is called without being overridden in a subclass.

## Description

`NotImplementedError` is used to define abstract methods that subclasses must implement. It's raised when the base class method is called instead of a subclass implementation.

Common scenarios:

- **Abstract base class** — method defined but not implemented.
- **Interface method** — method declared but no implementation.
- **Partial implementation** — subclass doesn't override all methods.
- **Template method** — base class method that should be overridden.

## Common Causes

```ruby
# Cause 1: Abstract method not overridden
class Shape
  def area
    raise NotImplementedError, "#{self.class} must implement #area"
  end
end

class Circle < Shape
  # Forgot to implement #area
end

Circle.new.area  # NotImplementedError

# Cause 2: Interface not fully implemented
class Animal
  def speak; raise NotImplementedError; end
  def move; raise NotImplementedError; end
end

class Dog < Animal
  def speak; "Woof!"; end
  # Forgot to implement #move
end

Dog.new.move  # NotImplementedError

# Cause 3: Calling super in abstract method
class Base
  def process
    raise NotImplementedError
  end
end

class Child < Base
  def process
    super  # NotImplementedError
  end
end
```

## Solutions

### Fix 1: Implement all abstract methods

```ruby
# Wrong
class Circle < Shape
  # Missing #area implementation
end

# Correct
class Circle < Shape
  def initialize(radius)
    @radius = radius
  end

  def area
    Math::PI * @radius ** 2
  end
end
```

### Fix 2: Use abstract class pattern

```ruby
class AbstractBase
  def process
    raise NotImplementedError, "#{self.class} must implement #process"
  end

  def self.abstract!
    define_method(:process) { raise NotImplementedError }
  end
end

class Concrete < AbstractBase
  def process
    # Implementation
  end
end
```

### Fix 3: Check if method is implemented before calling

```ruby
class Shape
  def area
    raise NotImplementedError
  end
end

shape = Circle.new(5)
if shape.respond_to?(:area)
  puts shape.area
else
  puts "Area not implemented for #{shape.class}"
end
```

### Fix 4: Use modules for mixins

```ruby
module Printable
  def print
    raise NotImplementedError, "#{self.class} must implement #print"
  end
end

class Document
  include Printable

  def print
    puts "Printing document..."
  end
end
```

## Related Errors

- [ScriptError](script-error) — parent class for script errors.
- [NoMethodError](no-method-error) — method doesn't exist at all.
- [ArgumentError](argument-error) — wrong number of arguments.
