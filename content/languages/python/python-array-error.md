---
title: "[Solution] Python array Module Error — Typed Array Failures"
description: "Fix Python array module errors including typecode errors, overflow, append/extend issues, memory errors, and incompatible types. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 252
---

# Python array Module Error — Typed Array Failures

The `array` module provides efficient arrays of numeric values using typecodes. Errors occur when values overflow the typecode range, incompatible types are used, or memory is exhausted.

## Common Causes

```python
# Cause 1: Overflow for the typecode
import array

arr = array.array("b", [])  # 'b' = signed char, range -128 to 127
arr.append(128)  # OverflowError: byte must be in range(-128, 127)

# Cause 2: Incompatible type in array
import array

arr = array.array("i", [])  # 'i' = signed int
arr.append("hello")  # TypeError: 'str' object cannot be interpreted as an integer

# Cause 3: Extending with incompatible iterable
import array

arr = array.array("f", [1.0, 2.0])  # 'f' = float
arr.extend([3, "four"])  # TypeError: 'str' object cannot be interpreted as float

# Cause 4: Memory error for very large arrays
import array

arr = array.array("q", [])  # 'q' = signed long long
# arr.extend(range(10**12))  # MemoryError if not enough RAM

# Cause 5: Invalid typecode character
import array

arr = array.array("x", [])  # ValueError: invalid typecode
```

## How to Fix

### Fix 1: Choose the right typecode

```python
import array

# Typecode ranges:
# 'b' = signed char: -128 to 127
# 'B' = unsigned char: 0 to 255
# 'h' = signed short: -32768 to 32767
# 'H' = unsigned short: 0 to 65535
# 'i' = signed int: typically -2^31 to 2^31-1
# 'I' = unsigned int: 0 to 2^32-1
# 'l' = signed long: platform dependent
# 'L' = unsigned long: platform dependent
# 'q' = signed long long: -2^63 to 2^63-1
# 'Q' = unsigned long long: 0 to 2^64-1
# 'f' = float: single precision
# 'd' = double: double precision

# Use 'B' for byte values 0-255
arr = array.array("B", [0, 128, 255])
arr.append(256)  # OverflowError

# Use 'H' for values up to 65535
arr = array.array("H", [0, 32767, 65535])

# Use 'i' for general integers
arr = array.array("i", [0, -100000, 100000])
```

### Fix 2: Validate types before insertion

```python
import array

def safe_append(arr, value):
    try:
        arr.append(value)
        return True
    except (TypeError, OverflowError) as e:
        print(f"Cannot add {value!r} to array of type '{arr.typecode}': {e}")
        return False

arr = array.array("i", [])
safe_append(arr, 42)       # True
safe_append(arr, "hello")  # False — TypeError
safe_append(arr, 2**32)    # False — OverflowError
```

### Fix 3: Extend with type-checked iterables

```python
import array

def safe_extend(arr, iterable):
    validated = []
    for item in iterable:
        try:
            if arr.typecode in ("f", "d"):
                validated.append(float(item))
            elif arr.typecode in ("b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"):
                validated.append(int(item))
            else:
                validated.append(item)
        except (TypeError, ValueError) as e:
            print(f"Skipping {item!r}: {e}")
    arr.extend(validated)

arr = array.array("i", [])
safe_extend(arr, [1, 2, 3, "four", 5.5, "six"])
print(arr)  # array('i', [1, 2, 3, 5])
```

### Fix 4: Monitor memory usage for large arrays

```python
import array
import sys

def create_large_array(typecode, size):
    try:
        arr = array.array(typecode)
        arr.extend(range(size))
        return arr
    except MemoryError:
        print(f"Cannot allocate array of {size} {typecode} elements")
        # Try smaller size
        return None

# Check memory footprint
arr = array.array("i", range(1000000))
print(f"Array size: {sys.getsizeof(arr)} bytes")  # Much smaller than list
print(f"Per element: {sys.getsizeof(arr) / len(arr):.1f} bytes")

# Compare with list
lst = list(range(1000000))
print(f"List size: {sys.getsizeof(lst)} bytes")  # Much larger
```

### Fix 5: Convert between array types safely

```python
import array

def convert_array(source, target_typecode):
    try:
        return array.array(target_typecode, source)
    except (TypeError, OverflowError) as e:
        print(f"Conversion failed: {e}")
        # Manual conversion with clamping
        if target_typecode in ("b",):
            min_val, max_val = -128, 127
        elif target_typecode in ("B",):
            min_val, max_val = 0, 255
        elif target_typecode in ("h",):
            min_val, max_val = -32768, 32767
        elif target_typecode in ("H",):
            min_val, max_val = 0, 65535
        else:
            raise

        clamped = [max(min_val, min(max_val, int(x))) for x in source]
        return array.array(target_typecode, clamped)

arr = array.array("i", [0, 100, 200, -100, -200])
small = convert_array(arr, "b")  # Some values will be clamped
print(small)  # array('b', [0, 100, 127, -100, -127])
```

## Examples

```python
# Real-world: Efficient pixel buffer
import array

class PixelBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # RGBA: 4 bytes per pixel
        self.buffer = array.array("B", [0] * (width * height * 4))

    def set_pixel(self, x, y, r, g, b, a=255):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("Pixel out of bounds")
        idx = (y * self.width + x) * 4
        self.buffer[idx] = min(255, max(0, r))
        self.buffer[idx + 1] = min(255, max(0, g))
        self.buffer[idx + 2] = min(255, max(0, b))
        self.buffer[idx + 3] = min(255, max(0, a))

    def get_pixel(self, x, y):
        idx = (y * self.width + x) * 4
        return tuple(self.buffer[idx:idx + 4])

buf = PixelBuffer(100, 100)
buf.set_pixel(50, 50, 255, 128, 0)
print(buf.get_pixel(50, 50))  # (255, 128, 0, 255)

# Real-world: Numerical data storage
import array

def store_sensor_data(readings):
    """Store sensor readings as compact float array."""
    arr = array.array("d")  # double precision
    for reading in readings:
        if isinstance(reading, (int, float)):
            arr.append(float(reading))
        else:
            print(f"Skipping non-numeric value: {reading}")
    return arr

data = store_sensor_data([23.5, 24.1, "error", 22.8, None, 25.0])
print(data)  # array('d', [23.5, 24.1, 22.8, 25.0])
```

## Related Errors

- [OverflowError](/languages/python/overflowerror/) — value exceeds typecode range
- [TypeError](/languages/python/typeerror/) — wrong type for array typecode
- [MemoryError](/languages/python/memoryerror/) — insufficient memory
- [IndexError](/languages/python/indexerror/) — out of bounds access
