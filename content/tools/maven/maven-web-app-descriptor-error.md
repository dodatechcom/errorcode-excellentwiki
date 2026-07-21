---
title: "Maven Web App Descriptor Error"
description: "Maven WAR build fails because the web.xml descriptor is malformed, missing required elements, or uses an unsupported schema version."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Web App Descriptor Error

The web.xml file defines the configuration of a Java web application. A descriptor error occurs when the file is not well-formed XML or contains configuration that the servlet container cannot parse.

## Common Causes

- The web.xml file contains XML syntax errors such as unclosed tags
- The schema declaration is incorrect or uses an unsupported version
- Required elements like `<servlet>` or `<web-app>` are malformed
- The namespace URL is incorrect for the declared schema version

## How to Fix

1. Validate the web.xml XML syntax:

```bash
xmllint --noout src/main/webapp/WEB-INF/web.xml
```

2. Use the correct schema for Servlet 4.0:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
         http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <display-name>My Web Application</display-name>

  <servlet>
    <servlet-name>main</servlet-name>
    <servlet-class>com.example.MainServlet</servlet-class>
  </servlet>

  <servlet-mapping>
    <servlet-name>main</servlet-name>
    <url-pattern>/api/*</url-pattern>
  </servlet-mapping>
</web-app>
```

3. Use annotation-based configuration instead of web.xml:

```java
@WebServlet(urlPatterns = "/api/*")
public class MainServlet extends HttpServlet {
    // ...
}
```

4. Configure the WAR plugin to handle missing web.xml:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-war-plugin</artifactId>
  <configuration>
    <failOnMissingWebXml>false</failOnMissingWebXml>
  </configuration>
</plugin>
```

## Examples

```bash
# Error output
[ERROR] Error parsing XML at line 12:
  The element "servlet" must be followed by "servlet-mapping"
```

```xml
<!-- Minimal valid web.xml for Servlet 4.0 -->
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         version="4.0">
  <display-name>My App</display-name>
</web-app>
```

## Related Errors

- [Web XML Missing]({{< relref "/tools/maven/maven-web-xml-missing" >}}) -- missing web.xml
- [WAR Plugin Error]({{< relref "/tools/maven/maven-war-plugin-error" >}}) -- WAR packaging issues
