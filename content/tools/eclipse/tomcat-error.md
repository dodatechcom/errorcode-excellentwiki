---
title: "[Solution] Eclipse Tomcat server error"
description: "Tomcat server error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "tomcat", "server", "web", "servlet"]
severity: "error"
---

# Tomcat server error

## Error Message

```
Several ports (8005, 8080, 8443) required by Tomcat v9.0 Server at localhost are already in use. The server may already be running in another process, or a system process may be using one of the requested ports.
```

## Common Causes

- Another Tomcat instance or application is already using the configured ports.
- Eclipse did not properly shut down the Tomcat server from a previous launch.
- The server port configuration in Eclipse's server definition conflicts with the `server.xml` ports.

## Solutions

### Solution 1: Kill the Existing Process

Find and kill the process occupying the port using the command line. Then go to the **Servers** view in Eclipse, right-click the Tomcat server, and select **Start** to relaunch it.

```java
# Find process using port 8080
lsof -i :8005
lsof -i :8080
lsof -i :8443

# Kill the process by PID
kill -9 <PID>

# Alternative: use fuser
fuser -k 8080/tcp
```

### Solution 2: Configure Eclipse Server Ports

Double-click the Tomcat server entry in the **Servers** view to open the server configuration editor. In the **Ports** section, change the HTTP, HTTPS, and Shutdown ports to available values. Make sure the changes match the `server.xml` in the Tomcat installation directory.

```bash
<!-- server.xml - Port configuration -->
<Server port="8005" shutdown="SHUTDOWN">
  <Service name="Catalina">
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
  </Service>
</Server>
```

## Prevention Tips

- Always use the **Servers** view to stop Tomcat rather than killing the process directly.
- Enable **Publish before starting** in the server configuration to auto-deploy changes.
- Set the Tomcat server timeout in **Servers > double-click server > Timeout** to prevent long startup hangs.

## Related Errors

- [web-tools-error]({{< relref "/tools/eclipse/web-tools-error" >}})
- [console-error]({{< relref "/tools/eclipse/console-error" >}})
- [run-configuration-error]({{< relref "/tools/eclipse/run-configuration-error" >}})
