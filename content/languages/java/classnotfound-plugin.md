---
title: "[Solution] Java ClassNotFoundException — custom ClassLoader cannot find plugin classes in plugin-based architectures"
description: "Fix Java ClassNotFoundException when custom classloader cannot find plugin classes in plugin-based architectures with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — custom ClassLoader cannot find plugin classes in plugin-based architectures

A `ClassNotFoundException` occurs when URLClassLoader pluginLoader = new URLClassLoader(new URL[]{jar.toURI().toURL()}, getClass().getClassLoader());
pluginLoader.loadClass("com.plugin.MyPlugin");  // wrong name or path.

## Common Causes

```java
URLClassLoader pluginLoader = new URLClassLoader(new URL[]{jar.toURI().toURL()}, getClass().getClassLoader());
pluginLoader.loadClass("com.plugin.MyPlugin");  // wrong name or path
```

## Solutions

```java
// Fix: child-first ClassLoader
public class PluginClassLoader extends URLClassLoader {
    protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
        try { return findClass(name); }
        catch (ClassNotFoundException e) { return super.loadClass(name, resolve); }
    }
}

// Fix: ServiceLoader with META-INF/services
ServiceLoader<Plugin> loader = ServiceLoader.load(Plugin.class);
```

## Prevention Checklist

- Verify plugin JARs contain expected classes.
- Use child-first ClassLoaders for isolation.
- Include proper META-INF/services files.

## Related Errors

ClassNotFoundException, NoClassDefFoundError
