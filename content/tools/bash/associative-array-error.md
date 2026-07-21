---
title: "[Solution] Bash Associative Array Error"
description: "Fix Bash associative array errors when declaring or using key-value hash arrays."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Associative Array Error

Bash associative arrays fail to declare or access correctly.

```
bash: declare: -A: invalid option
bash: mapfile: array subscript must be numeric
```

## Common Causes

- Using bash version < 4.0 (no associative array support)
- Missing -A flag in declare statement
- Accessing with numeric index instead of key
- Key contains special characters
- Associative array in subshell lost

## How to Fix

### Declare Associative Array

```bash
#!/bin/bash
# Requires bash 4.0+

declare -A config
config[host]="localhost"
config[port]="8080"
config[user]="admin"

echo "${config[host]}:${config[port]}"
```

### Check Bash Version

```bash
# Verify bash version supports associative arrays
if ((BASH_VERSINFO[0] < 4)); then
    echo "Associative arrays require bash 4.0+" >&2
    exit 1
fi
```

### Access All Keys and Values

```bash
declare -A env_vars
env_vars[DB_HOST]="localhost"
env_vars[DB_PORT]="5432"

# List all keys
echo "Keys: ${!env_vars[@]}"

# List all values
echo "Values: ${env_vars[@]}"

# Iterate over all entries
for key in "${!env_vars[@]}"; do
    echo "$key = ${env_vars[$key]}"
done
```

### Initialize from Command Output

```bash
declare -A git_status
while IFS=: read -r key value; do
    git_status["$key"]="$value"
done < <(git remote -v | awk '{print $1 ":" $2}')
```

### Prevent Subshell Loss

```bash
# Wrong - associative array lost after pipe
declare -A result
echo "a:b" | while IFS=: read -r k v; do
    result[$k]=$v
done
echo "${result[a]}"  # Empty

# Correct - use process substitution
declare -A result
while IFS=: read -r k v; do
    result[$k]=$v
done < <(echo "a:b")
echo "${result[a]}"  # b
```

## Examples

```bash
#!/bin/bash
declare -A users=(
    ["alice"]="admin"
    ["bob"]="editor"
    ["charlie"]="viewer"
)

for user in "${!users[@]}"; do
    role="${users[$user]}"
    echo "User: $user, Role: $role"
done
```
