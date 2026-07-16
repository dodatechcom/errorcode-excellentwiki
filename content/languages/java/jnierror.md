---
title: "[Solution] Java JNI Error — UnsatisfiedLinkError Fix"
description: "Fix Java UnsatisfiedLinkError (JNI Error) by ensuring native libraries are on java.library.path, matching architecture, and verifying JNI signatures."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["jnierror", "unsatisfiedlinkerror", "jni", "native", "library"]
weight: 5
---

# JNI Error — UnsatisfiedLinkError Fix

A JNI Error (manifested as `UnsatisfiedLinkError`) is thrown when the JVM cannot find or load a native library required by a `native` method, or cannot find the native method within the loaded library. This occurs when Java Native Interface (JNI) calls fail.

## Description

JNI allows Java code to call and be called by native applications and libraries. When a `native` method is declared but the corresponding native implementation cannot be loaded, the JVM throws `UnsatisfiedLinkError`.

## Common Causes

```java
// Cause 1: Native library not found on java.library.path
public class NativeLib {
    static {
        System.loadLibrary("mylib");  // Searches java.library.path
    }
    public native String processData(String input);
}

// Cause 2: Architecture mismatch (32-bit vs 64-bit)
// libmylib.so compiled for x86, running on x86_64 JVM

// Cause 3: JNI method signature mismatch
public native String process(int[] data);  // Java
// C: JNIEXPORT jstring JNICALL Java_NativeLib_process(...)  // wrong signature

// Cause 4: Missing dependent shared libraries
// libmylib.so depends on libfoo.so which is not on LD_LIBRARY_PATH
```

## Solutions

```java
// Fix 1: Set java.library.path before running
// java -Djava.library.path=/path/to/native/libs -jar myapp.jar

// Fix 2: Load library with absolute path
public class NativeLib {
    static {
        System.load("/opt/libs/libmylib.so");
    }
    public native String processData(String input);
}

// Fix 3: Verify architecture compatibility
// file /path/to/libmylib.so
// Should show: ELF 64-bit LSB shared object for x86-64

// Fix 4: Generate and verify JNI headers
// javac -h . NativeLib.java
// Compare generated header with C implementation
```

## Examples

```java
// This triggers UnsatisfiedLinkError when library is missing
public class NativeProcessor {
    static {
        System.loadLibrary("processor");
    }

    public native byte[] process(byte[] data);

    public static void main(String[] args) {
        NativeProcessor p = new NativeProcessor();
        byte[] result = p.process(new byte[]{1, 2, 3});
        // UnsatisfiedLinkError: no processor in java.library.path
    }
}
```

## Related Exceptions

- [NoClassDefFoundError](../noclassdeffounderror) — Java class missing
- [LinkageError](../linkageerror) — parent class for linkage failures
- [ClassNotFoundException](../classnotfoundexception) — Java class not found on classpath
