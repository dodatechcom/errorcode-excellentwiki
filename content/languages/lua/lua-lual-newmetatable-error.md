---
title: "[Solution] Lua luaL_newmetatable C API Error Fix"
description: "Fix Lua luaL_newmetatable C API errors when creating and registering metatables for userdata."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1135
---

## What This Error Means

An luaL_newmetatable error occurs when creating a new metatable in the Lua registry. This C API function either creates a new metatable or returns the existing one if the name is already registered.

## Common Causes

- Not storing the metatable reference for later use
- Conflicting metatable names between libraries
- Forgetting to set __gc and __tostring methods
- Not using luaL_setmetatable after creation
- Stack corruption from luaL_newmetatable

## How to Fix

```c
// WRONG: Creating metatable but not checking if it already exists
luaL_newmetatable(L, "MyType");
// If another library already registered "MyType", this returns the existing one

// CORRECT: Check the return value
int is_new = luaL_newmetatable(L, "MyType");
if (is_new) {
    // Only set methods for newly created metatable
    lua_pushcfunction(L, my_tostring);
    lua_setfield(L, -2, "__tostring");
}
```

```c
// WRONG: Missing __gc for userdata cleanup
luaL_newmetatable(L, "MyBuffer");
// No __gc method - memory leak!

// CORRECT: Register __gc
static int buffer_gc(lua_State *L) {
    Buffer *buf = (Buffer *)luaL_checkudata(L, 1, "MyBuffer");
    free(buf->data);
    return 0;
}

int is_new = luaL_newmetatable(L, "MyBuffer");
if (is_new) {
    lua_pushcfunction(L, buffer_gc);
    lua_setfield(L, -2, "__gc");
    lua_pushcfunction(L, buffer_tostring);
    lua_setfield(L, -2, "__tostring");
}
```

```c
// WRONG: Not setting metatable on userdata
void *ud = lua_newuserdata(L, sizeof(MyType));
// Missing: luaL_setmetatable(L, "MyType");

// CORRECT: Set metatable after creating userdata
void *ud = lua_newuserdata(L, sizeof(MyType));
luaL_setmetatable(L, "MyType");
```

```c
// WRONG: Creating metatable in wrong place
int luaopen_mylib(lua_State *L) {
    luaL_newmetatable(L, "MyType");
    // ... but the metatable is never associated with userdata
    return 0;
}

// CORRECT: Complete metatable registration
static int my_new(lua_State *L) {
    MyType *mt = (MyType *)lua_newuserdata(L, sizeof(MyType));
    mt->value = luaL_checknumber(L, 1);
    luaL_setmetatable(L, "MyType");
    return 1;
}

int luaopen_mylib(lua_State *L) {
    luaL_newmetatable(L, "MyType");
    lua_pushvalue(L, -1);
    lua_setfield(L, -2, "__index");
    lua_pushcfunction(L, my_tostring);
    lua_setfield(L, -2, "__tostring");
    lua_pop(L, 1);

    lua_newtable(L);
    lua_pushcfunction(L, my_new);
    lua_setfield(L, -2, "new");
    return 1;
}
```

```c
// Complete pattern
int luaopen_mylib(lua_State *L) {
    luaL_newmetatable(L, "MyType");
    lua_pushvalue(L, -1);
    lua_setfield(L, -2, "__index");
    luaL_setfuncs(L, my_methods, 0);
    lua_pop(L, 1);

    lua_newtable(L);
    lua_pushcfunction(L, my_new);
    lua_setfield(L, -2, "new");
    return 1;
}
```

## Examples

```c
// Safe metatable creation
int is_new = luaL_newmetatable(L, "MyVec");
if (is_new) {
    static const struct luaL_Reg mt[] = {
        {"__gc", vec_gc},
        {"__tostring", vec_tostring},
        {"__add", vec_add},
        {"__len", vec_len},
        {NULL, NULL}
    };
    luaL_setfuncs(L, mt, 0);
    lua_pushvalue(L, -1);
    lua_setfield(L, -2, "__index");
}
```

## Related Errors

- [Lua C API error](lua-capi-error) - C API issue
- [Lua userdata error](lua-userdata-error) - userdata issue
- [Lua metatable error](lua-metatable-error) - metatable issue
