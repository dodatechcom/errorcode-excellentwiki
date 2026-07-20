---
title: "[Solution] Lua C API Userdata Creation Error Fix"
description: "Fix Lua C API userdata errors when creating and managing userdata objects."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1115
---

## What This Error Means

A userdata error occurs in the Lua C API when creating, manipulating, or garbage collecting userdata. Userdata blocks hold raw C data in Lua variables.

## Common Causes

- Not allocating enough memory for the userdata block
- Forgetting to set a metatable for userdata
- Memory corruptions from writing past the userdata bounds
- Using freed userdata after garbage collection
- Not handling __gc metamethod correctly

## How to Fix

```c
// WRONG: Allocating wrong size
struct Point { double x, y; };
void *data = lua_newuserdata(L, sizeof(struct Point *));  // Wrong size!

// CORRECT: Allocate enough space
struct Point *p = (struct Point *)lua_newuserdata(L, sizeof(struct Point));
p->x = 3.0;
p->y = 4.0;
```

```c
// WRONG: Userdata without metatable
lua_newuserdata(L, sizeof(int));
*(int *)lua_touserdata(L, -1) = 42;
// No metatable - no type safety!

// CORRECT: Attach a metatable
luaL_newmetatable(L, "MyType");
lua_setmetatable(L, -2);
```

```c
// WRONG: Using userdata after it's been collected
lua_newuserdata(L, sizeof(int));
int *p = (int *)lua_touserdata(L, -1);
*p = 42;
lua_pop(L, 1);  // Userdata may be GC'd
// lua_gc(L, LUA_GCCOLLECT, 0);
// printf("%d\n", *p);  // Potential use-after-free!
```

```c
// WRONG: Missing __gc metamethod leading to memory leaks
static int new_buffer(lua_State *L) {
    size_t size = luaL_checkinteger(L, 1);
    char *buf = (char *)lua_newuserdata(L, sizeof(char *));
    buf = (char *)malloc(size);  // Allocated separately
    // No __gc to free this malloc'd memory!
    return 1;
}

// CORRECT: Use __gc to free resources
static int buffer_gc(lua_State *L) {
    char **buf = (char **)lua_touserdata(L, 1);
    if (*buf) {
        free(*buf);
        *buf = NULL;
    }
    return 0;
}

static int new_buffer(lua_State *L) {
    size_t size = luaL_checkinteger(L, 1);
    char **buf = (char **)lua_newuserdata(L, sizeof(char *));
    *buf = (char *)malloc(size);
    luaL_newmetatable(L, "Buffer");
    lua_pushcfunction(L, buffer_gc);
    lua_setfield(L, -2, "__gc");
    lua_setmetatable(L, -2);
    return 1;
}
```

```c
// Complete userdata example
static int point_new(lua_State *L) {
    double x = luaL_checknumber(L, 1);
    double y = luaL_checknumber(L, 2);
    struct Point *p = (struct Point *)lua_newuserdata(L, sizeof(struct Point));
    p->x = x;
    p->y = y;
    luaL_setmetatable(L, "Point");
    return 1;
}
```

## Examples

```c
// Safe userdata with full lifecycle management
typedef struct { double x, y; } Point;

static int Point_new(lua_State *L) {
    Point *p = lua_newuserdata(L, sizeof(Point));
    p->x = luaL_optnumber(L, 1, 0);
    p->y = luaL_optnumber(L, 2, 0);
    luaL_setmetatable(L, "Point");
    return 1;
}

static int Point_tostring(lua_State *L) {
    Point *p = luaL_checkudata(L, 1, "Point");
    lua_pushfstring(L, "(%g, %g)", p->x, p->y);
    return 1;
}
```

## Related Errors

- [Lua userdata error](lua-userdata-error) - userdata issue
- [Lua C API error](lua-capi-error) - C API issue
- [Lua type error](lua-type-error) - type issue
