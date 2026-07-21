---
title: "[Solution] Elixir ExUnit Describe Error -- Incorrect Test Organization"
description: "Fix Elixir ExUnit describe errors when organizing test blocks with describe incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir ExUnit Describe Error

This error occurs when `describe` blocks in ExUnit tests are used incorrectly or nested improperly.

## Common Causes

- Nesting describe blocks (not supported in ExUnit)
- Using describe without a string tag
- Missing test module attribute setup
- Not using setup blocks correctly within describe

## How to Fix

### Use flat describe blocks

```elixir
# WRONG: nested describe
defmodule MyAppTest do
  use ExUnit.Case

  describe "outer" do
    describe "inner" do  # error: cannot nest describe
      test "works" do
        assert true
      end
    end
  end
end

# CORRECT: flat structure
defmodule MyAppTest do
  use ExUnit.Case

  describe "authentication" do
    test "valid credentials" do
      assert true
    end
  end

  describe "authorization" do
    test "admin access" do
      assert true
    end
  end
end
```

### Use setup within describe

```elixir
describe "with setup" do
  setup do
    user = %{name: "Alice", role: :admin}
    {:ok, user: user}
  end

  test "admin can access", %{user: user} do
    assert user.role == :admin
  end
end
```

## Examples

```elixir
defmodule MathTest do
  use ExUnit.Case

  describe "addition" do
    test "adds positive numbers" do
      assert 2 + 3 == 5
    end
  end

  describe "multiplication" do
    test "multiplies integers" do
      assert 2 * 3 == 6
    end
  end
end
```
