---
title: "Swift Compilation Error in Gradle"
description: "Gradle Swift compilation fails due to missing Swift toolchain, incompatible source files, or incorrect module configuration."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Swift Compilation Error in Gradle

Gradle can compile Swift source files using native plugins. A Swift compilation error occurs when the Swift compiler is missing or the source files contain syntax errors.

## Common Causes

- Swift toolchain is not installed on the build machine
- Source files reference modules that are not linked
- The Swift version in the toolchain is incompatible with the code
- Module.modulemap files are missing for library dependencies

## How to Fix

1. Verify the Swift compiler is installed:

```bash
swift --version
```

2. Configure the Swift toolchain in `build.gradle`:

```groovy
plugins {
    id 'swift-application'
}

application {
    targetMachines = [machines.macos.x86_64]
}
```

3. Ensure source files are in the correct directory structure:

```
src/main/swift/
  main.swift
  Sources/
    MyModule/
      MyClass.swift
```

4. Install the Swift toolchain:

```bash
# macOS -- already included with Xcode
xcode-select --install

# Linux (Ubuntu)
wget https://download.swift.org/swift-5.9.2-release/ubuntu2204/swift-5.9.2-RELEASE/swift-5.9.2-RELEASE-ubuntu22.04.tar.gz
tar xzf swift-5.9.2-RELEASE-ubuntu22.04.tar.gz
export PATH=$PWD/usr/bin:$PATH
```

## Examples

```bash
# Error output
error: missing required module 'Foundation'
```

```groovy
// Swift library configuration
plugins {
    id 'swift-library'
}

library {
    targetMachines = [machines.macos.x86_64]
}
```

## Related Errors

- [Native Compilation Error]({{< relref "/tools/gradle/gradle-native-compilation-error" >}}) -- general native build issues
- [C++ Compilation Error]({{< relref "/tools/gradle/gradle-cpp-compilation-error" >}}) -- C++ specific failures
