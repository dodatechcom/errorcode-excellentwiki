---
title: "Gradle Native Compilation Error"
description: "Gradle native compilation using the software model or new native plugins fails due to toolchain or platform configuration issues."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Native Compilation Error

Gradle supports building native C, C++, and Swift projects using native plugins. A compilation error occurs when the native toolchain is not found or configured correctly.

## Common Causes

- The C or C++ compiler is not installed or not on the system PATH
- Required headers or libraries are missing from the platform
- The `targetMachine` does not match the host architecture
- Build type or platform settings conflict with available toolchains

## How to Fix

1. Verify the compiler is available:

```bash
gcc --version
g++ --version
```

2. Configure the native toolchain in `build.gradle`:

```groovy
plugins {
    id 'cpp-application'
}

application {
    targetMachines = [machines.linux.x86_64]
}

model {
    toolchains {
        gcc(GccToolChainSpec) {
            // Optional: specify paths
        }
    }
}
```

3. Set the compiler path explicitly if auto-detection fails:

```groovy
model {
    toolchains {
        clang(ClangToolChainSpec) {
            clangExecutable = '/usr/bin/clang'
        }
    }
}
```

4. Install the required toolchain:

```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# macOS
xcode-select --install
```

## Examples

```bash
# Error output
> Native toolchain not found for target machine Linux AMD64
  Install gcc or clang and ensure they are on the PATH
```

```groovy
// Complete native application configuration
plugins {
    id 'cpp-application'
}

application {
    targetMachines = [machines.linux.x86_64]
}

model {
    components {
        main(NativeExecutableSpec) {
            targetPlatform 'linux_x86_64'
            sources.cpp {
                source {
                    srcDirs 'src/main/cpp'
                    include '**/*.cpp'
                }
            }
        }
    }
}
```

## Related Errors

- [C++ Compilation Error]({{< relref "/tools/gradle/gradle-cpp-compilation-error" >}}) -- C++ specific issues
- [Process Forking Error]({{< relref "/tools/gradle/gradle-process-forking-error" >}}) -- compiler execution failures
