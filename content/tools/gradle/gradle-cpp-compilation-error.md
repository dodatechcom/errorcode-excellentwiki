---
title: "C++ Compilation Error in Gradle"
description: "Gradle C++ compilation fails due to missing compiler, incorrect flags, or unresolved include paths in the native build configuration."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# C++ Compilation Error in Gradle

Gradle compiles C++ code using platform-native toolchains. A compilation error occurs when the compiler cannot process the source files due to toolchain misconfiguration or code issues.

## Common Causes

- The C++ compiler does not support the specified C++ standard level
- Include directories are missing or contain wrong paths
- Compiler flags reference unsupported options
- Linker cannot find required shared or static libraries

## How to Fix

1. Verify the C++ compiler supports your target standard:

```bash
g++ --version
g++ -std=c++17 -E /dev/null  # test C++17 support
```

2. Configure include directories in `build.gradle`:

```groovy
model {
    components {
        main(NativeExecutableSpec) {
            sources.cpp {
                source {
                    srcDirs 'src/main/cpp'
                }
                exportedHeaders {
                    srcDirs 'src/main/headers'
                }
            }
        }
    }
}
```

3. Set compiler arguments explicitly:

```groovy
model {
    toolchains {
        gcc(GccToolChainSpec) {
            eachPlatform {
                cppCompiler.withArguments { args ->
                    args.addAll(['-std=c++17', '-Wall', '-Wextra'])
                }
            }
        }
    }
}
```

4. Link required libraries:

```groovy
model {
    components {
        main(NativeExecutableSpec) {
            nativeComponent.linkLibrary('pthread')
            nativeComponent.linkLibrary('stdc++fs')
        }
    }
}
```

## Examples

```bash
# Error output
src/main/cpp/main.cpp:12:10: fatal error: 'optional' file not found
 #include <optional>
```

```groovy
// C++ executable with correct configuration
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

- [Native Compilation Error]({{< relref "/tools/gradle/gradle-native-compilation-error" >}}) -- general native build issues
- [Process Forking Error]({{< relref "/tools/gradle/gradle-process-forking-error" >}}) -- compiler execution failures
