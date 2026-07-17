---
title: "[Solution] C++ Boost.Program_options - option error"
description: "Fix C++ Boost.Program_options errors. Handle command-line argument parsing failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["boost", "program-options", "command-line", "argument", "parsing"]
weight: 5
---

# Boost.Program_options - option error

Boost.Program_options errors occur when command-line arguments are invalid, missing, or have wrong types.

## Common Causes

```cpp
// Cause 1: Unknown option
po::options_description desc("Options");
desc.add_options()("help", "help message");
po::variables_map vm;
po::parse_command_line(argc, argv, desc); // unknown option

// Cause 2: Missing required value
desc.add_options()("port", po::value<int>(), "port");
// --port without value

// Cause 3: Invalid value type
desc.add_options()("count", po::value<int>(), "count");
// --count abc (not an int)
```

## How to Fix

### Fix 1: Use try-catch

```cpp
try {
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);
} catch (const po::error& e) {
    std::cerr << "Error: " << e.what() << std::endl;
    std::cerr << desc << std::endl;
}
```

### Fix 2: Provide default values

```cpp
desc.add_options()("port", po::value<int>()->default_value(8080), "port");
```

### Fix 3: Handle unknown options

```cpp
try {
    auto parsed = po::parse_command_line(argc, argv, desc);
    po::store(parsed, vm);
} catch (const po::unknown_option& e) {
    std::cerr << "Unknown option: " << e.get_option_name() << std::endl;
}
```

## Related Errors

- [Boost.Test - test error]({{< relref "/languages/cpp/boost-test-error" >}}) — test errors.
- [Boost.Asio - async error]({{< relref "/languages/cpp/boost-asio-error" >}}) — async errors.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — invalid argument.
