---
title: "[Solution] FactoryBot — create/build, Trait, Sequence, Transient Errors"
description: "Fix FactoryBot errors. Handle create/build failures, trait conflicts, sequence, and association issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, factory_bot, factory, test, build"]
severity: "error"
---

# FactoryBot Errors

## Error Message

```
FactoryBot::AssociationConflict: can't define singleton
# or
FactoryBot::InvalidDefinitionError: Trait not registered
# or
ActiveRecord::RecordInvalid: Validation failed: ...
```

## Common Causes

- Factory references a trait that doesn't exist
- Validation failures when creating records
- Naming conflict between factory and trait
- Missing associations or required attributes

## Solutions

### Solution 1: Define Factories Correctly

Create factories with proper defaults and associations.

```ruby
# spec/factories/users.rb
FactoryBot.define do
  factory :user do
    name { "Alice" }
    email { "alice@example.com" }
    password { "password123" }

    trait :admin do
      role { "admin" }
    end

    trait :with_posts do
      transient do
        post_count { 3 }
      end

      after(:create) do |user, evaluator|
        create_list(:post, evaluator.post_count, user: user)
      end
    end
  end
end
```

### Solution 2: Use Traits for Variations

Create named trait blocks for different record states.

```ruby
# spec/factories/posts.rb
FactoryBot.define do
  factory :post do
    title { "Default Title" }
    body { "Default body content" }
    user

    trait :published do
      published_at { Time.current }
    end

    trait :draft do
      published_at { nil }
    end

    trait :long do
      title { "A" * 200 }
      body { "B" * 10000 }
    end
  end
end

# Usage
create(:post)                        # default
create(:post, :published)            # with published_at
create(:post, :draft, title: "Draft")  # draft with custom title
```

### Solution 3: Use Sequences for Unique Values

Generate unique values with sequences.

```ruby
FactoryBot.define do
  factory :user do
    sequence(:name) { |n| "User#{n}" }
    sequence(:email) { |n| "user#{n}@example.com" }

    # With block for complex generation
    sequence(:username, aliases: [:user]) do |n|
      "user_#{SecureRandom.hex(4)}_#{n}"
    end
  end
end

# Each call gets a unique value
create(:user).email  # => "user1@example.com"
create(:user).email  # => "user2@example.com"
```

### Solution 4: Handle Associations and Transient Attributes

Use transient attributes to configure associated records.

```ruby
FactoryBot.define do
  factory :order do
    customer
    status { "pending" }

    transient do
      item_count { 2 }
    end

    after(:create) do |order, evaluator|
      create_list(:order_item, evaluator.item_count, order: order)
    end

    trait :completed do
      status { "completed" }
      completed_at { Time.current }
    end
  end
end

# Create order with 3 items
create(:order, item_count: 3)

# Create completed order with default 2 items
create(:order, :completed)
```

## Prevention Tips

- Use `create` for persisted records, `build` for unpersisted
- Use traits for variations instead of inline overrides
- Use sequences for unique values across test runs
- Use `transient` attributes to configure associated record counts

## Related Errors

- [ActiveRecord::RecordInvalid]({{< relref "/languages/ruby/activerecord-validation" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
