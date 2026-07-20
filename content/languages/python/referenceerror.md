---
title: "[Solution] Python ReferenceError — Weak Reference Expired"
description: "Fix Python ReferenceError for weak references, expired references, and garbage collected objects. Handle weakref callbacks and prevent stale references."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 24
---

# Python ReferenceError — Weak Reference Expired

A `ReferenceError` is raised when you access a weak reference whose referent has already been garbage collected. Weak references allow you to refer to an object without preventing it from being garbage collected, but accessing the object after collection triggers this error.

## Common Causes

```python
# Cause 1: Accessing a weakref after the object is collected
import weakref

class MyClass:
    pass

obj = MyClass()
ref = weakref.ref(obj)

del obj  # Object is now eligible for garbage collection
import gc; gc.collect()
ref()  # ReferenceError: weakly-referenced object no longer exists

# Cause 2: Weak reference callback fires but reference is stored
class Cache:
    def __init__(self):
        self._cache = {}

def on_expire(key):
    print(f"{key} expired")

obj = MyClass()
cache_ref = weakref.ref(obj, lambda r: on_expire("myobj"))
del obj
gc.collect()
cache_ref()  # ReferenceError

# Cause 3: WeakValueDictionary entry collected
class Data:
    pass

d = weakref.WeakValueDictionary()
obj = Data()
d["key"] = obj

del obj
gc.collect()
d["key"]  # ReferenceError: weakly-referenced object no longer exists

# Cause 4: WeakSet member collected
s = weakref.WeakSet()
obj = Data()
s.add(obj)

del obj
gc.collect()
list(s)  # Empty — but iterating during collection may raise ReferenceError

# Cause 5: functools.lru_cache with weak references
import weakref, functools

class ExpensiveObject:
    pass

ref = weakref.ref(ExpensiveObject())
del ExpensiveObject  # If last strong ref is removed
gc.collect()
ref()  # ReferenceError
```

## How to Fix

### Fix 1: Check if the weak reference is still alive before accessing

```python
import weakref

class MyClass:
    pass

obj = MyClass()
ref = weakref.ref(obj)

# Wrong — crashes if object is collected
data = ref()

# Correct — check first
obj = ref()
if obj is not None:
    data = obj.process()
else:
    print("Object has been garbage collected")
```

### Fix 2: Use WeakValueDictionary with a fallback

```python
import weakref

class Data:
    def __init__(self, value):
        self.value = value

cache = weakref.WeakValueDictionary()

def get_or_create(key, value):
    obj = cache.get(key)
    if obj is None:
        obj = Data(value)
        cache[key] = obj
    return obj

# Safely access the cache
obj = get_or_create("key", 42)
# If the original obj was collected, a new one is created
```

### Fix 3: Keep a strong reference while using weak references

```python
import weakref

class EventBus:
    def __init__(self):
        self.listeners = weakref.WeakSet()
        self._keep_alive = []  # Prevent premature collection

    def subscribe(self, listener):
        self.listeners.add(listener)
        self._keep_alive.append(listener)  # Keep strong reference
```

### Fix 4: Use try/except ReferenceError for defensive access

```python
import weakref

def safe_deref(ref):
    try:
        return ref()
    except ReferenceError:
        return None

class MyClass:
    pass

obj = MyClass()
ref = weakref.ref(obj)
del obj
gc.collect()

result = safe_deref(ref)  # Returns None instead of raising
```

### Fix 5: Use weakref callback to handle expiration

```python
import weakref

class Resource:
    def __init__(self, name):
        self.name = name

def on_resource_expired(ref, name="unknown"):
    print(f"Resource '{name}' has been garbage collected")

obj = Resource("db_connection")
ref = weakref.ref(obj, lambda r: on_resource_expired(r, obj.name))

del obj
gc.collect()  # Prints: Resource 'db_connection' has been garbage collected
```

## Prevention Checklist

- Always check `ref()` for `None` before using the result of a weak reference.
- Use `try/except ReferenceError` when dereferencing weak references in critical code.
- Keep a strong reference alongside weak references for objects that must remain accessible.
- Use `weakref回调` (callback) to detect when objects are collected unexpectedly.
- Understand when `gc.collect()` runs — objects may not be collected immediately.

## Related Errors

- [NameError](/languages/python/nameerror/) — variable name not defined in scope.
- [AttributeError](/languages/python/attributeerror/) — attribute does not exist on the object.
- [RuntimeError](/languages/python/runtimeerror/) — object accessed during garbage collection cycle.
