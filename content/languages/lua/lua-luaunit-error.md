---
title: "[Solution] LuaUnit Test Assertion Failed Error Fix"
description: "Fix LuaUnit test assertion failures. Learn why LuaUnit tests fail and how to write correct test assertions in Lua."
languages: ["lua"]
severities: ["error"]
error-types: ["test-error"]
weight: 5
---

## What This Error Means

A LuaUnit assertion failure occurs when a test assertion does not match the expected value. LuaUnit is the most popular unit testing framework for Lua. When an assertion like `assertEquals`, `assertTrue`, or `assertNil` fails, LuaUnit reports the test as failed with details about the expected and actual values.

## Why It Happens

- The function under test returns an unexpected value
- A side effect changes state between setup and assertion
- Floating-point comparison fails due to precision differences
- Table comparison fails because of reference identity vs value equality
- Test setup or teardown does not reset state properly
- The test assumes a specific ordering that is not guaranteed
- Mock or stub functions return different values than expected

## How to Fix It

### Use precise comparison for floating-point values

```lua
-- WRONG: Exact float comparison
function testFloat()
    local result = 0.1 + 0.2
    assertEquals(result, 0.3)  -- fails due to floating point
end

-- CORRECT: Use delta comparison for floats
function testFloat()
    local result = 0.1 + 0.2
    assertAlmostEquals(result, 0.3, 1e-10)  -- within tolerance
end
```

### Reset state between tests

```lua
-- WRONG: State leaks between tests
local counter = 0
function testIncrement()
    counter = counter + 1
    assertEquals(counter, 1)  -- fails on second run
end

-- CORRECT: Use setUp and tearDown
local TestMyModule = {}
function TestMyModule:setUp()
    counter = 0
end
function TestMyModule:testIncrement()
    counter = counter + 1
    assertEquals(counter, 1)
end
```

### Compare tables correctly

```lua
-- WRONG: Comparing tables by reference
function testTables()
    local a = { 1, 2, 3 }
    local b = { 1, 2, 3 }
    assertEquals(a, b)  -- fails: different references
end

-- CORRECT: Use deep comparison
function testTables()
    local a = { 1, 2, 3 }
    local b = { 1, 2, 3 }
    assertTrue(deepEquals(a, b))  -- or use assertItemsEquals
end
```

### Handle nil and false correctly

```lua
-- WRONG: Confusing nil with false
function testNil()
    local result = getConfig("missing")
    assertEquals(result, false)  -- may be nil instead
end

-- CORRECT: Check exact type
function testNil()
    local result = getConfig("missing")
    assertNil(result)  -- if nil is expected
end
```

### Use meaningful assertion messages

```lua
-- WRONG: Generic failure message
assertEquals(getUserName(42), "Alice")

-- CORRECT: Add descriptive context
assertEquals(
    getUserName(42),
    "Alice",
    "getUserName(42) should return Alice for valid user ID"
)
```

## Common Mistakes

- Not running `LuaUnit.LuaUnit.run()` at the end of the test file
- Using `assertEquals` for boolean checks instead of `assertTrue` or `assertFalse`
- Forgetting that `assertNil` and `assertFalse` are different assertions
- Not isolating tests that modify global state
- Using `os.exit` in tests which prevents LuaUnit from reporting results

## Related Pages

- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument type
- [Lua Runtime Error](lua-runtime-error) - general runtime issue
