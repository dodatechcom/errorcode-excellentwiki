---
title: "[Solution] Rails Validations — Custom Validator, Conditional, Uniqueness Scope Errors"
description: "Fix Rails validation errors. Handle custom validators, conditional validation, uniqueness scope, and validation failures."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, validations, custom_validator, uniqueness"]
severity: "error"
---

# Rails Validations Errors

## Error Message

```
ActiveRecord::RecordInvalid: Validation failed: Email has already been taken
# or
NoMethodError: undefined method `validate_each' for ...
# or
ActiveModel::UnknownAttributeError: unknown attribute 'email' for User
```

## Common Causes

- Uniqueness validation without database-level uniqueness constraint
- Custom validator missing `validate_each` method
- Conditional validations using wrong syntax
- Scope on uniqueness validation causing false negatives

## Solutions

### Solution 1: Use Database-Level Uniqueness Constraints

Add a database unique index in addition to model validation.

```ruby
# db/migrate/20260101000000_add_unique_index_to_users.rb
class AddUniqueIndexToUsers < ActiveRecord::Migration[7.0]
  def change
    add_index :users, :email, unique: true
  end
end

# model
class User < ApplicationRecord
  validates :email, presence: true, uniqueness: { case_sensitive: false }
end
```

### Solution 2: Create Custom Validators

Implement `validate_each` for reusable validation logic.

```ruby
# app/validators/email_validator.rb
class EmailValidator < ActiveModel::EachValidator
  def validate_each(record, attribute, value)
    unless value =~ URI::MailTo::EMAIL_REGEXP
      record.errors.add(attribute, (options[:message] || "is not a valid email"))
    end
  end
end

# Usage
class User < ApplicationRecord
  validates :email, presence: true, email: true
end
```

### Solution 3: Use Conditional Validations Correctly

Apply validations only when conditions are met.

```ruby
class User < ApplicationRecord
  # Only validate if name is present
  validates :email, presence: true, if: :name_present?

  # Validate on specific actions
  validates :password, presence: true, on: :create

  # Multiple conditions
  validates :phone, presence: true, if: -> { admin? || manager? }

  # Unless condition
  validates :avatar, presence: true, unless: -> { guest? }

  private

  def name_present?
    name.present?
  end
end
```

### Solution 4: Scope Uniqueness Validation Properly

Use `scope` to handle scoped uniqueness correctly.

```ruby
class Enrollment < ApplicationRecord
  belongs_to :user
  belongs_to :course

  # Uniqueness within course scope
  validates :user_id, uniqueness: { scope: :course_id }

  # Scoped uniqueness with message
  validates :email, uniqueness: {
    scope: :organization_id,
    message: "already enrolled in this organization"
  }
end
```

## Prevention Tips

- Always add a database unique index alongside model uniqueness validation
- Use `validate_each` for custom validators, not `validates_each`
- Use lambdas for conditional validations to avoid premature evaluation
- Test validations with both valid and invalid inputs

## Related Errors

- [ActiveRecord::RecordInvalid]({{< relref "/languages/ruby/activerecord-validation" >}})
- [ActiveModel::UnknownAttributeError]({{< relref "/languages/ruby/type-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
