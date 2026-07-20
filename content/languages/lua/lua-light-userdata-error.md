---
title: "[Solution] Lua Light Userdata Pointer Error Fix"
description: "Fix Lua light userdata errors when passing raw C pointers to Lua."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1116
---

## What This Error Means

A light userdata error occurs when using light userdata in Lua. Light userdata are raw C pointers without metatables or garbage collection, leading to dangling pointer risks.

## Common Causes

- Using freed memory through a light userdata pointer
- Confusing light userdata with full userdata
- Not being able to attach metatables to light userdata
- Type confusion (two different types sharing the same pointer value)
- Light userdata comparison semantics

## How to Fix

```c
// WRONG: Light userdata pointing to freed stack memory
void create_light_userdata(lua_State *L) {
    int local_var = 42;
    lua_pushlightuserdata(L, &local_var);  // Stack address!
    // local_var goes out of scope...
}

// CORRECT: Point to static or heap-allocated memory
static int global_value = 42;
void create_light_userdata(lua_State *L) {
    lua_pushlightuserdata(L, &global_value);
}
```

```c
// WRONG: Cannot set metatable on light userdata
lua_pushlightuserdata(L, ptr);
luaL_newmetatable(L, "MyType");
lua_setmetatable(L, -2);  // No effect on light userdata!

// CORRECT: Use full userdata if you need metatables
void **ud = (void **)lua_newuserdata(L, sizeof(void *));
*ud = ptr;
luaL_newmetatable(L, "MyType");
lua_setmetatable(L, -2);
```

```c
// WRONG: Type confusion with light userdata
// Two different types with same address
lua_pushlightuserdata(L, (void *)0x1);  // Could represent anything

// CORRECT: Use full userdata with type tags
typedef struct { int type; void *ptr; } TaggedPtr;
TaggedPtr *tp = lua_newuserdata(L, sizeof(TaggedPtr));
tp->type = 1;  // Type identifier
tp->ptr = actual_ptr;
```

```lua
-- Light userdata comparison in Lua
local ptr1 = ffi.new("int[1]")
local ptr2 = ffi.new("int[1]")
-- Light userdata compare by identity, not value
```

```c
// Safe usage pattern
void push_resource(lua_State *L, Resource *res) {
    Resource **ud = (Resource **)lua_newuserdata(L, sizeof(Resource *));
    *ud = res;
    luaL_newmetatable(L, "Resource");
    lua_setmetatable(L, -2);
}
```

## Examples

```c
// Light userdata for unique keys (common pattern)
lua_pushlightuserdata(L, NULL);  // Unique key
lua_pushboolean(L, 1);
lua_settable(L, LUA_REGISTRYINDEX);
```

## Related Errors

- [Lua userdata error](lua-userdata-error) - userdata issue
- [Lua C API error](lua-capi-error) - C API issue
- [Lua type error](lua-type-error) - type issue
