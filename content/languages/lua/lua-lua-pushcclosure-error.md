---
title: "[Solution] Lua lua_pushcclosure C API Error Fix"
description: "Fix Lua lua_pushcclosure C API errors when creating closures with upvalues in C."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1137
---

## What This Error Means

An lua_pushcclosure error occurs when creating a C closure with upvalues. The function pops n upvalues from the stack and creates a closure. Common issues include wrong upvalue count or upvalue type mismatch.

## Common Causes

- Wrong number of upvalues (n does not match stack values)
- Upvalues of wrong type or missing from stack
- Using upvalue indices incorrectly in the C function
- Forgetting that upvalues are shared between closures
- Not using lua_upvalueindex properly

## How to Fix

```c
// WRONG: Wrong number of upvalues
lua_pushnumber(L, 42);  // One upvalue
lua_pushcclosure(L, my_func, 2);  // Expects 2 upvalues, only 1 on stack!

// CORRECT: Match upvalue count
lua_pushnumber(L, 42);  // Upvalue 1
lua_pushcclosure(L, my_func, 1);  // One upvalue
```

```c
// WRONG: Accessing upvalue incorrectly
static int my_func(lua_State *L) {
    double val = lua_tonumber(L, 1);  // Accesses argument, not upvalue!
    return 0;
}

// CORRECT: Use lua_upvalueindex
static int my_func(lua_State *L) {
    double val = lua_tonumber(L, lua_upvalueindex(1));  // Upvalue
    return 0;
}
```

```c
// WRONG: Multiple closures sharing the same upvalue
lua_pushnumber(L, 0);  // Counter
lua_pushcclosure(L, counter1, 1);
lua_pushcclosure(L, counter2, 1);
// counter1 and counter2 share the same upvalue!

// CORRECT: Push separate upvalues for each closure
lua_pushnumber(L, 0);
lua_pushcclosure(L, counter1, 1);
lua_pushnumber(L, 0);
lua_pushcclosure(L, counter2, 1);
```

```c
// Creating closures with multiple upvalues
static int make_accumulator(lua_State *L) {
    double initial = luaL_checknumber(L, 1);
    lua_pushnumber(L, initial);  // Upvalue 1
    lua_pushcclosure(L, accumulator_func, 1);
    return 1;
}

static int accumulator_func(lua_State *L) {
    double *val = lua_touserdata(L, lua_upvalueindex(1));
    // ... use upvalue
    return 0;
}
```

```c
// Complete example
static int counter_func(lua_State *L) {
    int *count = (int *)lua_touserdata(L, lua_upvalueindex(1));
    *count = *count + 1;
    lua_pushinteger(L, *count);
    return 1;
}

static int new_counter(lua_State *L) {
    int *count = (int *)lua_newuserdata(L, sizeof(int));
    *count = 0;
    lua_pushcclosure(L, counter_func, 1);
    return 1;
}
```

## Examples

```c
// Creating a filtered function
static int filter_func(lua_State *L) {
    lua_Number threshold = lua_tonumber(L, lua_upvalueindex(1));
    lua_Number value = luaL_checknumber(L, 1);
    lua_pushboolean(L, value > threshold);
    return 1;
}

static int make_filter(lua_State *L) {
    lua_Number threshold = luaL_checknumber(L, 1);
    lua_pushnumber(L, threshold);
    lua_pushcclosure(L, filter_func, 1);
    return 1;
}
```

## Related Errors

- [Lua C API error](lua-capi-error) - C API issue
- [Lua luaL_setfuncs error](lua-lual-setfuncs-error) - function registration issue
- [Lua type error](lua-type-error) - type issue
