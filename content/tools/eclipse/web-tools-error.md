---
title: "[Solution] Eclipse Web tools error"
description: "Web tools error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "web", "html", "css", "javascript", "wtp"]
severity: "error"
---

# Web tools error

## Error Message

```
Server startup failed. The web application could not be deployed. Check the server logs for the root cause. Context '/mywebapp' failed to start.
```

## Common Causes

- The web application has deployment descriptor errors in `web.xml` or `application.properties`.
- Required libraries are missing from the `WEB-INF/lib` directory.
- The server configuration (e.g., context path, port) conflicts with another running application.

## Solutions

### Solution 1: Verify Web Application Deployment

Open the **web.xml** file (in `src/main/webapp/WEB-INF/`) and validate it using the XML editor. Check for missing required elements such as `<display-name>`, `<welcome-file-list>`, or servlet mappings. Use **Project > Properties > Web Project Settings** to set the correct context root.

```java
<!-- web.xml - Valid deployment descriptor -->
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         version="4.0">
    <display-name>My Web Application</display-name>
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
    </welcome-file-list>
    <servlet>
        <servlet-name>MyServlet</servlet-name>
        <servlet-class>com.example.MyServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>MyServlet</servlet-name>
        <url-pattern>/api/*</url-pattern>
    </servlet-mapping>
</web-app>
```

### Solution 2: Configure WTP Server Runtime

Go to **Window > Preferences > Server > Runtime Environments** and ensure the correct server runtime is configured (e.g., Apache Tomcat). Then go to **Window > Preferences > Server > Adapter** and verify the server adapter is enabled. In the **Servers** view, double-click the server to check the module configuration.

```bash
# Eclipse server runtime configuration
# Window > Preferences > Server > Runtime Environments
#   Add > Apache Tomcat v9.0
#   Name: Apache Tomcat v9.0
#   Installation directory: /opt/tomcat-9.0
#   JRE: JavaSE-11 (or appropriate version)

# Project > Properties > Project Facets
#   ☑ Dynamic Web Module 4.0
#   ☑ Java 11
#   ☑ JavaScript 1.0
```

## Prevention Tips

- Use the **Servers** view to manage server lifecycle (start, stop, restart, publish).
- Enable **Publish before starting** in the server configuration to auto-deploy changes.
- Check **Window > Preferences > Web > File Types** to configure how different file types are served.

## Related Errors

- [tomcat-error]({{< relref "/tools/eclipse/tomcat-error" >}})
- [xml-error]({{< relref "/tools/eclipse/xml-error" >}})
- [console-error]({{< relref "/tools/eclipse/console-error" >}})
