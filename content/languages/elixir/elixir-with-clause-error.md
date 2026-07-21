---
title: "[Solution] Elixir With Clause Error -- Mismatched With Patterns"
description: "Fix Elixir with clause errors when the do block pattern does not match the with clause output."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir With Clause Error

This error occurs when the `with` construct's `do` block receives a value that does not match any of its clauses.

## Common Causes

- With clauses not matching the actual return values of functions
- Missing `else` clause for non-matching values
- The `do` block expecting a different shape than what arrives
- Functions returning {:ok, value} when nil is expected

## How to Fix

### Ensure patterns match function returns

```elixir
# WRONG: with pattern does not match function return
result =
  with {:ok, user} <- find_user(id),
       {:ok, orders} <- get_orders(user) do
    process(orders)  # expects orders, not {:ok, orders}
  end

# CORRECT: match the unwrapped value
result =
  with {:ok, user} <- find_user(id),
       {:ok, orders} <- get_orders(user) do
    {:ok, process(orders)}
  else
    {:error, reason} -> {:error, reason}
  end
```

### Add else clause

```elixir
def complete_order(order_id) do
  with {:ok, order} <- find_order(order_id),
       {:ok, validated} <- validate(order),
       {:ok, result} <- process_payment(validated) do
    {:ok, result}
  else
    {:error, :not_found} -> {:error, "Order not found"}
    {:error, reason} -> {:error, reason}
  end
end
```

## Examples

```elixir
def register(params) do
  with :ok <- validate_params(params),
       {:ok, user} <- create_user(params),
       :ok <- send_welcome_email(user) do
    {:ok, user}
  end
end
```
