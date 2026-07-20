---
title: "[Solution] Lua luaL_checktype Type Check Error Fix"
description: "Fix Lua luaL_checktype C API errors when validating function argument types."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1108
---

## What This Error Means

An luaL_checktype error occurs when the Lua C API function luaL_checktype validates that a stack value has the expected type. If the type doesn't match, it raises a Lua error.

## Common Causes

- Passing wrong argument type from Lua to C function
- Using wrong type constant (LUA_TNUMBER vs LUA_TSTRING)
- Not checking optional arguments correctly
- Stack index out of range
- Confusing luaL_checktype with luaL_opt (optional arguments)

## How to Fix

```c
// WRONG: Wrong type constant
static int myfunc(lua_State *L) {
    luaL_checktype(L, 1, LUA_TBOOLEAN);  // But user passed a number
    return 0;
}

// CORRECT: Use appropriate type or allow multiple types
static int myfunc(lua_State *L) {
    if (lua_isnumber(L, 1)) {
        double n = lua_tonumber(L, 1);
        printf("Number: %f\n", n);
    } else if (lua_isstring(L, 1)) {
        const char *s = lua_tostring(L, 1);
        printf("String: %s\n", s);
    } else {
        return luaL_argerror(L, 1, "expected number or string");
    }
    return 0;
}
```

```c
// WRONG: Not allowing nil for optional arguments
static int myfunc(lua_State *L) {
    const char *name = luaL_checkstring(L, 1);  // Error if nil
    int age = luaL_checkinteger(L, 2);          // Error if nil
    return 0;
}

// CORRECT: Use luaL_opt for optional args
static int myfunc(lua_State *L) {
    const char *name = luaL_optstring(L, 1, "default");
    int age = luaL_optinteger(L, 2, 0);
    printf("%s is %d years old\n", name, age);
    return 0;
}
```

```c
// WRONG: Confusing luaL_checktype with lua_type values
luaL_checktype(L, 1, LUA_TTABLE);  // Correct constant
// LUA_TFUNCTION vs LUA_TTHREAD etc

// CORRECT: Use proper type constants
switch (lua_type(L, 1)) {
    case LUA_TNIL:      /* ... */ break;
    case LUA_TBOOLEAN:  /* ... */ break;
    case LUA_TNUMBER:   /* ... */ break;
    case LUA_TSTRING:   /* ... */ break;
    case LUA_TTABLE:    /* ... */ break;
    case LUA_TFUNCTION: /* ... */ break;
    case LUA_TUSERDATA: /* ... */ break;
    case LUA_TTHREAD:   /* ... */ break;
    case LUA_TLIGHTUSERDATA: /* ... */ break;
    default: return luaL_argerror(L, 1, "unexpected type");
}
```

```c
// Flexible type checking for C functions
static int flex_func(lua_State *L) {
    int n = lua_gettop(L);
    for (int i = 1; i <= n; i++) {
        printf("arg %d: %s\n", i, lua_typename(L, lua_type(L, i)));
    }
    return 0;
}
```

## Examples

```c
// Safe argument checking
static int create_array(lua_State *L) {
    int nargs = lua_gettop(L);
    lua_createtable(L, nargs, 0);
    for (int i = 1; i <= nargs; i++) {
        double val = luaL_checknumber(L, i);
        lua_rawseti(L, -2, i);
    }
    return 1;
}
```

## Related Errors

- [Lua C API error](lua-capi-error) - C API issue
- [Lua argument error](lua-argument-error) - argument issue
- [Lua type error](lua-type-error) - type issue
