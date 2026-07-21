---
title: "JNI Interface Error"
description: "Fix JNI interface errors when calling native methods from Java or Kotlin"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes when calling native method because JNI registration fails

## Common Causes

- Native method name does not match JNI convention
- System.loadLibrary call missing for native lib
- JNI function signature incorrect
- Package name in JNI function does not match Java class

## Fixes

- Ensure native function name follows Java_package_Method convention
- Call System.loadLibrary in static initializer
- Use javah or javac -h to generate correct headers
- Verify package path matches JNI function name exactly

## Code Example

```kotlin
// Kotlin declaration
external fun nativeAdd(a: Int, b: Int): Int

companion object {
    init {
        System.loadLibrary("native-lib")
    }
}

// C++ implementation
extern "C" JNIEXPORT jint JNICALL
Java_com_example_app_MyClass_nativeAdd(
    JNIEnv *env, jobject thiz, jint a, jint b) {
    return a + b;
}
```

# Generate JNI headers
javac -h app/src/main/cpp/ app/src/main/java/com/example/app/MyClass.java
