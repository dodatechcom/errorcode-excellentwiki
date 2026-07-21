---
title: "[Solution] Lua Yaml Parse Error"
description: "Fix Lua YAML parsing errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

YAML parsing errors occur when parsing YAML documents.

## Common Causes

- Indentation errors
- Invalid syntax
- Missing quotes
- Flow mapping errors

## How to Fix

### 1. Use yaml parser correctly

```lua
local yaml = require("yaml")
local data = yaml.load(yamlString)
```

### 2. Handle parse errors

```lua
local function safeParseYaml(str)
  local yaml = require("yaml")
  local ok, result = pcall(yaml.load, str)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Parse YAML safely
local function parseYamlSafe(yamlStr)
  local yaml = require("yaml")
  
  local ok, data = pcall(yaml.load, yamlStr)
  if not ok then
    return nil, "Parse error: " .. tostring(data)
  end
  
  return data
end

local data, err = parseYamlSafe("name: test\nvalue: 42")
if data then
  print(data.name, data.value)
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Syntax error](/languages/lua/lua-syntax-error)
- [Type error](/languages/lua/lua-type-error)
