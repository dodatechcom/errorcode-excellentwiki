---
title: "[Solution] Lua FFI Call Failed Bad Argument to C Function Fix"
description: "Fix LuaJIT FFI call failures and bad C function arguments. Learn why FFI calls fail and how to pass correct types to C."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An FFI call failure in LuaJIT occurs when a call through the Foreign Function Interface to a C library fails. This manifests as `bad argument to C function` or a segfault. The FFI provides direct access to C functions and data structures from Lua, but requires precise type declarations and memory safety.

## Why It Happens

- Wrong `ffi.cdef` declaration not matching the actual C function signature
- Passing Lua types that cannot be automatically converted to C types
- Passing invalid pointers or NULL pointers where valid memory is expected
- Using a function pointer after the library was unloaded
- Mismatched calling conventions between LuaJIT and the target C library
- Attempting to pass Lua strings where `const char*` pointers are expected but the string contains embedded null bytes

## How to Fix It

### Match cdef declarations exactly to the C header

```lua
-- WRONG: Incorrect cdef
ffi.cdef[[
    int strlen(char *s);  -- should be const char*
]]
local len = ffi.C.strlen("hello")  -- may warn or fail

-- CORRECT: Match the actual C declaration
ffi.cdef[[
    int strlen(const char *s);
]]
local len = ffi.C.strlen("hello")
print(len)  -- 5
```

### Verify argument types before FFI calls

```lua
-- WRONG: Passing wrong type
ffi.cdef[[
    void free(void *ptr);
]]
ffi.C.free(42)  -- bad argument: expected pointer

-- CORRECT: Cast to correct type first
local ptr = ffi.C.malloc(100)
ffi.C.free(ptr)  -- valid pointer
```

### Handle NULL pointers explicitly

```lua
-- WRONG: Dereferencing NULL
ffi.cdef[[
    typedef struct { int x; } Point;
]]
local p = ffi.cast("Point*", nil)
print(p.x)  -- segfault

-- CORRECT: Check for NULL before use
local p = ffi.cast("Point*", nil)
if p ~= nil then
    print(p.x)
else
    print("Pointer is NULL")
end
```

### Use ffi.string correctly for C string conversion

```lua
-- WRONG: Lua string containing null bytes
ffi.cdef[[
    int strcmp(const char *s1, const char *s2);
]]
local str = "hello\0world"  -- null byte truncates
local result = ffi.C.strcmp(str, "hello")

-- CORRECT: Use ffi strings for embedded nulls
local cstr = ffi.new("char[12]", "hello\0world")
local result = ffi.C.strcmp(cstr, "hello\0world")
```

### Load shared libraries with ffi.load

```lua
-- WRONG: Using ffi.C for a non-standard library
ffi.C.custom_function()  -- not in default C namespace

-- CORRECT: Load the specific shared library
local lib = ffi.load("custom")  -- loads libcustom.so / custom.dll
ffi.cdef[[
    int custom_function(int arg);
]]
local result = lib.custom_function(42)
```

## Common Mistakes

- Not freeing FFI-allocated memory, causing memory leaks
- Using `ffi.C` for libraries that are not part of the standard C library
- Passing Lua tables or userdata directly to FFI functions without converting them to C types
- Declaring functions in `ffi.cdef` that do not exist in the loaded library
- Not using `ffi.gc` for automatic garbage collection of FFI-allocated memory

## Related Pages

- [Lua FFI Error](lua-ffi-error) - general FFI issues
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument types
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua GC Error](lua-gc-error) - memory limit and GC issues
