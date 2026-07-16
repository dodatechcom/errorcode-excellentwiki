---
title: "[Solution] Ruby ActiveRecord::RecordNotFound / StatementInvalid Fix"
description: "Fix ActiveRecord RecordNotFound and StatementInvalid errors. Learn how to handle missing records and database query issues in Rails."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["activerecord", "recordnotfound", "statementinvalid", "rails", "ruby"]
weight: 5
---

# ActiveRecord::RecordNotFound / StatementInvalid

ActiveRecord errors occur when database operations fail, either because a record doesn't exist or because the SQL query is invalid.

## Description

ActiveRecord is the ORM layer in Ruby on Rails. `RecordNotFound` is raised when `find` can't locate a record, and `StatementInvalid` occurs when SQL queries are malformed or fail.

Common causes:

- **Record doesn't exist** — using `find` with a non-existent ID
- **Invalid SQL** — malformed query syntax
- **Missing table/column** — schema doesn't match the query
- **Database connection issues** — connection lost or timeout

## Common Causes

```ruby
# Cause 1: Record not found
User.find(99999)  # ActiveRecord::RecordNotFound: Couldn't find User with 'id'=99999

# Cause 2: Invalid SQL
User.where("invalid_column = ?", value)  # ActiveRecord::StatementInvalid: PG::UndefinedColumn

# Cause 3: Missing table
User.connection.execute("SELECT * FROM nonexistent_table")  # ActiveRecord::StatementInvalid

# Cause 4: Type mismatch
User.where(id: "not_a_number")  # ActiveRecord::StatementInvalid
```

## How to Fix

### Fix 1: Use find_by instead of find

```ruby
# Wrong
User.find(99999)  # RecordNotFound

# Correct
user = User.find_by(id: 99999)
user || handle_not_found
```

### Fix 2: Use find_or_create

```ruby
# Wrong
user = User.find(params[:id])  # RecordNotFound

# Correct
user = User.find_or_create_by(id: params[:id]) do |u|
  u.name = "Default"
end
```

### Fix 3: Validate SQL queries

```ruby
# Wrong
User.where("invalid_column = ?", value)  # StatementInvalid

# Correct
User.where(column_name: value) if User.column_names.include?("column_name")
```

### Fix 4: Handle database errors

```ruby
# Wrong
User.create!(bad_data)  # StatementInvalid

# Correct
begin
  User.create!(bad_data)
rescue ActiveRecord::StatementInvalid => e
  Rails.logger.error "Database error: #{e.message}"
end
```

## Examples

```ruby
# Example 1: Safe record lookup
def find_user(id)
  User.find_by(id: id) or raise ActiveRecord::RecordNotFound
end

# Example 2: Batch operations
User.where(id: [1, 2, 3]).find_each do |user|
  process(user)
end
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [TypeError]({{< relref "/languages/ruby/typeerror-ruby" >}}) — wrong object type for an operation
- [IOError]({{< relref "/languages/ruby/io-error" >}}) — input/output operation failed
