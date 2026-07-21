---
title: "[Solution] Lua Torch Error"
description: "Fix Lua Torch7 deep learning framework errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Torch errors occur when using the Torch7 framework incorrectly.

## Common Causes

- Tensor dimension mismatch
- Missing module
- CUDA error
- Memory error

## How to Fix

### 1. Handle tensor errors

```lua
local torch = require("torch")
local a = torch.randn(3, 4)
local b = torch.randn(3, 4)
local c = a + b  -- Element-wise addition
```

### 2. Check dimensions

```lua
local function safeAdd(a, b)
  if a:size(1) ~= b:size(1) or a:size(2) ~= b:size(2) then
    return nil, "Dimension mismatch"
  end
  return a + b
end
```

## Examples

```lua
-- Torch neural network
local nn = require("nn")
local model = nn.Sequential()
model:add(nn.Linear(10, 5))
model:add(nn.ReLU())
model:add(nn.Linear(5, 2))

-- Forward pass
local input = torch.randn(1, 10)
local output = model:forward(input)
print(output)
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
- [Memory error](/languages/lua/lua-memory-limit)
