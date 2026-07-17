---
title: "[Solution] C++ yaml-cpp - parse error"
description: "Fix C++ yaml-cpp parse errors. Handle malformed YAML input."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["yaml-cpp", "yaml", "parse", "syntax", "config"]
weight: 5
---

# yaml-cpp - parse error

yaml-cpp parse errors occur when YAML input has syntax errors such as wrong indentation, invalid characters, or malformed documents.

## Common Causes

```yaml
# Cause 1: Wrong indentation
name: Alice
age: 30
  address: 123 Main St  # error: unexpected indent

# Cause 2: Missing colon
name Alice  # error: key without colon

# Cause 3: Unclosed quote
name: "Alice  # error: unterminated string
```

## How to Fix

### Fix 1: Use error handling

```cpp
#include <yaml-cpp/yaml.h>

try {
    YAML::Node config = YAML::LoadFile("config.yaml");
} catch (const YAML::Exception& e) {
    std::cerr << "YAML parse error: " << e.what() << std::endl;
}
```

### Fix 2: Validate YAML syntax

```bash
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

### Fix 3: Fix indentation

```yaml
name: Alice
age: 30
address: 123 Main St
```

## Related Errors

- [RapidJSON - parse error]({{< relref "/languages/cpp/rapidjson-error" >}}) — JSON parse error.
- [nlohmann/json - parse error]({{< relref "/languages/cpp/nlohmann-json-error" >}}) — JSON parse error.
- [Boost.JSON - parse error]({{< relref "/languages/cpp/boost-json-error" >}}) — JSON parse error.
