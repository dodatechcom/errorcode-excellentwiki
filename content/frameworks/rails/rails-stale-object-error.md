---
title: "[Solution] Rails Stale Object Error"
description: "Fix Rails ActiveRecord StaleObjectError optimistic locking. Resolve concurrent update conflicts in Rails models."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when two processes try to update the same record simultaneously, and the `lock_version` column detects the conflict.

## Common Causes

- Two users edit the same record at the same time
- Background job and web request update the same model concurrently
- `lock_version` column is missing from the table
- Optimistic locking is enabled but not handled in the controller
- Long-running transaction holds the lock too long

## How to Fix

1. Add `locking_column` if the default is not used:

```ruby
class Product < ApplicationRecord
  self.locking_column = :lock_version
end
```

2. Rescue the stale object error and retry:

```ruby
class OrdersController < ApplicationController
  def update
    @order = Order.find(params[:id])
    @order.update!(order_params)
    redirect_to @order, notice: "Order updated."
  rescue ActiveRecord::StaleObjectError
    redirect_to edit_order_path(@order), alert: "Record was modified by another user. Please retry."
  end
end
```

3. Ensure `lock_version` column exists:

```ruby
class AddLockVersionToOrders < ActiveRecord::Migration[7.1]
  def change
    add_column :orders, :lock_version, :integer, default: 0, null: false
  end
end
```

4. Use pessimistic locking for critical sections:

```ruby
order = Order.lock.find(params[:id])
order.update!(status: "shipped")
```

## Examples

```ruby
# Two processes try to update the same order
order = Order.find(1)
order.update!(status: "paid")
# ActiveRecord::StaleObjectError: Attempted to update a stale object

# Fix with retry loop
def update_with_retry(record, attrs, max_attempts: 3)
  max_attempts.times do
    begin
      record.reload.update!(attrs)
      return true
    rescue ActiveRecord::StaleObjectError
      record.reload
    end
  end
  false
end
```
