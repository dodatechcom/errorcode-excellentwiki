---
title: "[Solution] Rails Association Mismatch Error"
description: "Fix Rails association name mismatch or wrong association type. Resolve ActiveRecord association configuration errors."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when an ActiveRecord association is defined incorrectly, such as using `belongs_to` where `has_many` is needed, or referencing a class that does not exist.

## Common Causes

- `belongs_to` used on both sides of a one-to-many relationship
- Association references a class that was renamed or does not exist
- `class_name` option does not match the actual model class
- Foreign key column is missing or named incorrectly
- `:through` association references a non-existent intermediate association

## How to Fix

1. Verify the association types match:

```ruby
# One-to-many: correct
class Author < ApplicationRecord
  has_many :books
end

class Book < ApplicationRecord
  belongs_to :author
end
```

2. Use `class_name` when the model name differs from the association name:

```ruby
class Order < ApplicationRecord
  belongs_to :customer, class_name: 'User'
end
```

3. Check `:through` associations have valid intermediaries:

```ruby
class Assembly < ApplicationRecord
  has_many :manifests
  has_many :parts, through: :manifests
end

class Manifest < ApplicationRecord
  belongs_to :assembly
  belongs_to :part
end
```

4. Verify foreign key columns exist:

```ruby
Schema.define do
  create_table :books do |t|
    t.references :author, null: false, foreign_key: true
    t.string :title
  end
end
```

## Examples

```ruby
# belongs_to on both sides -- wrong
class User < ApplicationRecord
  belongs_to :posts  # ERROR: should be has_many
end

# Wrong class_name
class Order < ApplicationRecord
  belongs_to :buyer, class_name: 'Customers'
end
# NameError: uninitialized constant Customers

# Fix: use singular 'Customer'
belongs_to :buyer, class_name: 'Customer'
```
