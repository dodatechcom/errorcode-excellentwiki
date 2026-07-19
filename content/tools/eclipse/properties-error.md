---
title: "[Solution] Eclipse Properties file error"
description: "Properties file error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "properties", "i18n", "resource-bundle"]
severity: "error"
---

# Properties file error

## Error Message

```
Properties file encoding error: The file 'messages.properties' contains non-ASCII characters but is saved with ISO-8859-1 encoding. Use native2ascii or save the file as UTF-8.
```

## Common Causes

- The properties file contains non-ASCII characters but is saved with ISO-8859-1 encoding, which is the Java default.
- Resource bundle file names do not follow the naming convention required by ResourceBundle (e.g., `messages_en.properties`).
- The properties file contains syntax errors such as unescaped special characters or malformed key-value pairs.

## Solutions

### Solution 1: Set Properties File Encoding

Right-click the properties file in the Package Explorer and select **Properties**. Set the **Text file encoding** to UTF-8. For Java resource bundles, you can configure the default encoding via **Window > Preferences > General > Workspace > Text file encoding** and set it to UTF-8.

```java
# Example properties file with UTF-8 encoding
# File: messages.properties
app.title=My Application
app.greeting=Hello, \u0057orld!
error.not.found=Resource not found
user.welcome=Welcome back, {0}!

# Localized version
# File: messages_en.properties
app.title=My Application
app.greeting=Hello, World!

# File: messages_fr.properties
app.title=Mon Application
app.greeting=Bonjour, le monde!
```

### Solution 2: Use Eclipse Properties Editor Plugin

Install the **Properties Editor** plugin from Eclipse Marketplace to get a specialized editor for `.properties` files that handles Unicode encoding automatically. The editor shows native characters directly instead of escaped Unicode sequences.

```bash
# Convert non-ASCII properties to escaped format
native2ascii -encoding UTF-8 messages_utf8.properties messages.properties

# Or use the java.text.MessageFormat for parameterized messages
import java.util.ResourceBundle;
ResourceBundle bundle = ResourceBundle.getBundle("messages");
String greeting = bundle.getString("user.welcome");
```

## Prevention Tips

- Use **Resource Bundle Editor** (from Eclipse Marketplace) to manage multi-language properties files.
- Store all translatable strings in properties files and use `MessageFormat` for parameterized messages.
- Add the @SuppressWarnings('unused') annotation to suppress warnings about unused resource bundle keys.

## Related Errors

- [xml-error]({{< relref "/tools/eclipse/xml-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
- [web-tools-error]({{< relref "/tools/eclipse/web-tools-error" >}})
