---
title: "[Solution] yaml-cpp Type Conversion Error Fix"
description: "Fix yaml-cpp type conversion errors. Handle wrong type access, missing keys, and conversion exceptions."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["yaml", "yaml-cpp", "parsing", "type-conversion"]
weight: 5
---

# yaml-cpp Type Conversion Error Fix

Fix yaml-cpp type conversion errors. Handle wrong type access, missing keys, and conversion exceptions.

## What This Error Means

yaml-cpp throws `YAML::TypedBadConversion` or `YAML::InvalidNode` when accessing nodes incorrectly:

```
YAML::TypedBadConversion<int>: bad conversion
YAML::InvalidNode: invalid node; this may result from using non-map nodes as maps
```

## Common Causes

```cpp
// Cause 1: Accessing node as wrong type
YAML::Node node = YAML::Load("hello");
int val = node.as<int>(); // Throws - node is string

// Cause 2: Accessing missing key
YAML::Node node = YAML::Load("{}");
int val = node["missing"].as<int>(); // Throws

// Cause 3: Treating scalar as sequence/map
// Cause 4: Node out of scope when accessing
```

## How to Fix

### Fix 1: Check node type before conversion

```cpp
#include <yaml-cpp/yaml.h>

int safe_get_int(const YAML::Node& node, const std::string& key, int default_val) {
    if (node[key] && node[key].IsScalar()) {
        try {
            return node[key].as<int>();
        } catch (const YAML::TypedBadConversion<int>&) {
            return default_val;
        }
    }
    return default_val;
}
```

### Fix 2: Use Node::IsNull() checks

```cpp
#include <yaml-cpp/yaml.h>

void process_config(const YAML::Node& config) {
    if (config["database"] && config["database"].IsMap()) {
        auto db = config["database"];
        std::string host = db["host"] ? db["host"].as<std::string>() : "localhost";
        int port = db["port"] ? db["port"].as<int>() : 5432;
    }
}
```

### Fix 3: Use as with default value via try-catch

```cpp
#include <yaml-cpp/yaml.h>
#include <string>

template<typename T>
T yaml_as(const YAML::Node& node, const T& default_val) {
    try {
        return node.as<T>();
    } catch (const YAML::Exception&) {
        return default_val;
    }
}
```

## Examples

```cpp
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <string>
#include <vector>

struct Config {
    std::string host = "localhost";
    int port = 8080;
    std::vector<std::string> tags;
};

Config load_config(const std::string& filename) {
    Config config;

    try {
        YAML::Node root = YAML::LoadFile(filename);

        if (root["host"]) config.host = root["host"].as<std::string>();
        if (root["port"]) config.port = root["port"].as<int>();

        if (root["tags"] && root["tags"].IsSequence()) {
            for (const auto& tag : root["tags"]) {
                config.tags.push_back(tag.as<std::string>());
            }
        }
    } catch (const YAML::Exception& e) {
        std::cerr << "YAML error: " << e.what() << std::endl;
    }

    return config;
}

int main() {
    auto config = load_config("config.yaml");
    std::cout << "Host: " << config.host << std::endl;
    std::cout << "Port: " << config.port << std::endl;
    return 0;
}
```

## Related Errors

- [YAML-CPP Error]({{< relref "/languages/cpp/yaml-cpp-error" >}}) — yaml-cpp error
- [Nlohmann JSON Error]({{< relref "/languages/cpp/nlohmann-json-error-v2" >}}) — JSON error
- [Toml Error]({{< relref "/languages/rust/toml-error" >}}) — TOML error
