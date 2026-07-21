---
title: "[Solution] Lua Xml Parse Error"
description: "Fix Lua XML parsing errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

XML parsing errors occur when parsing XML documents.

## Common Causes

- Malformed XML
- Unclosed tags
- Invalid attributes
- Missing root element

## How to Fix

### 1. Use xml parser correctly

```lua
local xml = require("xml")
local tree = xml.parse(xmlString)
```

### 2. Handle parse errors

```lua
local function safeParseXml(str)
  local ok, result = pcall(xml.parse, str)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Parse XML safely
local function parseXmlSafe(xmlStr)
  local xml = require("xml")
  
  local ok, doc = pcall(xml.parse, xmlStr)
  if not ok then
    return nil, "Parse error: " .. tostring(doc)
  end
  
  return doc
end

local doc, err = parseXmlSafe("<root><item>text</item></root>")
if doc then
  print(doc.root.item[1])
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Syntax error](/languages/lua/lua-syntax-error)
- [Type error](/languages/lua/lua-type-error)
