---
title: "[Solution] Java UnsatisfiedLinkError — Native Library Fix"
description: "Fix Java UnsatisfiedLinkError by placing native libraries on java.library.path, ensuring correct architecture, and verifying JNI method signatures."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsatisfiedLinkError — Native Library Fix

An `UnsatisfiedLinkError` is thrown when the JVM cannot find or load a native library required by a `native` method, or cannot find the native method within the loaded library. This is a subclass of `LinkageError`.

## Description

This error occurs in two scenarios:

1. **Library not found**: The `System.loadLibrary()` or `System.load()` call cannot find the native library file (`.so` on Linux, `.dll` on Windows, `.dylib` on macOS).
2. **Method not found**: The native library is loaded but the JNI method signature does not match the Java declaration.

Common message variants:

- `java.lang.UnsatisfiedLinkError: no mylib in java.library.path`
- `java.lang.UnsatisfiedLinkError: /path/to/libmylib.so: wrong ELF class: ELFCLASS32`
- `java.lang.UnsatisfiedLinkError: com.example.MyClass.myNativeMethod()Ljava.lang.String;`
- `java.lang.UnsatisfiedLinkError: Can't load dependent library`

## Common Causes

```java
// Cause 1: Native library not on java.library.path
public class NativeHelper {
    static {
        System.loadLibrary("mylib");  // Searches java.library.path
    }
    public native String process(String input);
}

// Cause 2: Architecture mismatch (32-bit library on 64-bit JVM)
// libmylib.so compiled for x86, running on x86_64 JVM

// Cause 3: JNI method signature mismatch
public native String process(int[] data);  // Java declaration
// C implementation: JNIEXPORT jstring JNICALL Java_NativeHelper_process(
//     JNIEnv *env, jobject obj, jintArray data);  // May mismatch if Java signature changed

// Cause 4: Missing dependent native libraries
// libmylib.so depends on libfoo.so which is not on LD_LIBRARY_PATH
```

## Solutions

### Fix 1: Add the library path to java.library.path

```bash
# Set before running the JVM
java -Djava.library.path=/path/to/native/libs -jar myapp.jar

# Or set LD_LIBRARY_PATH (Linux/macOS)
export LD_LIBRARY_PATH=/path/to/native/libs:$LD_LIBRARY_PATH
java -jar myapp.jar

# Windows
set PATH=C:\path\to\libs;%PATH%
java -jar myapp.jar
```

### Fix 2: Use absolute path with `System.load()`

```java
public class NativeHelper {
    static {
        // Load with absolute path — no java.library.path needed
        String path = "/opt/libs/libmylib.so";
        System.load(path);
    }
    public native String process(String input);
}
```

### Fix 3: Verify architecture compatibility

```bash
# Check library architecture
file /path/to/libmylib.so
# Should show: ELF 64-bit LSB shared object for x86-64

# Check JVM architecture
java -version  # Should show 64-Bit Server VM

# Cross-compile if needed (on Linux)
gcc -m64 -shared -o libmylib.so -I$JAVA_HOME/include mylib.c  # 64-bit
```

### Fix 4: Verify JNI method signatures

```bash
# Generate JNI header to verify signatures
javac -h . NativeHelper.java
# Compare generated header with your C implementation

# Use javap to check the Java native method signature
javap -s NativeHelper
```

## Prevention Checklist

- Always verify `java.library.path` includes the directory containing your native library.
- Match native library architecture (32/64-bit) to the JVM architecture.
- Use `javap -s` to verify JNI method signatures match the native implementation.
- Bundle native libraries in the correct platform-specific directory for your deployment target.

## Related Errors

- [NoClassDefFoundError](../noclassdeffounderror) — Java class missing, not native library.
- [LinkageError](../linkageerror) — parent class for linkage failures.
- [ClassNotFoundException](../classnotfoundexception) — Java class not found on classpath.
