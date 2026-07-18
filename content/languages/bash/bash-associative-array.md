---
title: "[Solution] Bash Associative Array Invalid Subscript Error Fix"
description: "Fix 'associative array: invalid subscript' in Bash. Resolve key format and declaration issues with Bash associative arrays."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Associative Array Invalid Subscript Error Fix

The `associative array: invalid subscript` error occurs when you use an invalid key format with a Bash associative array or misuse indexed array syntax on an associative array.

## What This Error Means

Bash associative arrays (declared with `declare -A`) require string keys. When you use numeric indices or special characters improperly, Bash throws an invalid subscript error. This is distinct from regular indexed array behavior.

A typical error:

```
bash: name: invalid subscript
```

## Why It Happens

Common causes include:

- **Using numeric index on associative array** — `arr[0]="value"` on a `declare -A` array.
- **Missing `declare -A`** — Treating a regular array as associative.
- **Using special characters in keys without quotes** — `arr[my key]="value"` fails without quotes.
- **Accessing with wrong variable type** — Mixing indexed and associative arrays.
- **Unset associative array being reused** — After `unset`, the type is lost.

## How to Fix It

### Fix 1: Always declare -A before using associative arrays

```bash
# WRONG: Not declaring
config[host]="localhost"  # Treated as indexed array

# RIGHT: Declare as associative
declare -A config
config[host]="localhost"
config[port]="3306"
```

### Fix 2: Use string keys, not numeric

```bash
# WRONG: Using numeric keys on associative array
declare -A arr
arr[0]="value"

# RIGHT: Use string keys
declare -A arr
arr[first]="value"
arr[second]="other"
```

### Fix 3: Quote keys with special characters

```bash
# WRONG: Space in key causes error
declare -A arr
arr[my key]="value"

# RIGHT: Quote the key
declare -A arr
arr["my key"]="value"
echo "${arr[my key]}"
```

### Fix 4: Preserve type after unset

```bash
# WRONG: unset destroys the type
declare -A config
config[host]="localhost"
unset config  # Destroys associative array type
config[port]="3306"  # Now treated as indexed array

# RIGHT: Unset individual elements
declare -A config
config[host]="localhost"
config[port]="3306"
unset 'config[host]'  # Preserves array type
```

### Fix 5: Use proper iteration

```bash
declare -A config=(
    [host]="localhost"
    [port]="3306"
    [db]="mydb"
)

# RIGHT: Iterate over keys
for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done
```

## Common Mistakes

- **Assuming numeric keys work the same as indexed arrays** — Associative arrays use string keys only.
- **Forgetting to redeclare after `unset`** — The variable loses its associative type.
- **Not quoting keys with spaces** — Always quote keys containing special characters.

## Related Pages

- [Bash Associative Array Error](bash-associative-array-error) — General associative array issues
- [Bash Array Error](bash-array-error) — Indexed array problems
- [Bash Unset Error](bash-unset-error) — Variable unset issues
