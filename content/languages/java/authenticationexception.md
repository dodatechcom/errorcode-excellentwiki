---
title: "[Solution] Java AuthenticationException — JNDI Authentication Failed"
description: "Fix Java AuthenticationException by verifying credentials, checking authentication method, handling expired passwords, and using correct security configuration."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1502
---

# AuthenticationException — JNDI Authentication Failed

A `javax.naming.AuthenticationException` is thrown when authentication fails during a JNDI operation against a naming or directory service.

## Description

`AuthenticationException` indicates that the credentials provided to the naming or directory service were rejected. This commonly occurs with LDAP, Kerberos, or other secured JNDI providers when the principal name, password, or authentication method is incorrect.

**Message variants:**
- `javax.naming.AuthenticationException`
- `Authentication failed`
- `Invalid credentials`
- `Simple bind failed: invalid credentials`
- `49 - Invalid Credentials`

## Common Causes

```java
// Cause 1: Wrong password
env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "wrongPassword");
Context ctx = new InitialContext(env); // AuthenticationException

// Cause 2: Incorrect authentication method
env.put(Context.SECURITY_AUTHENTICATION, "none"); // Should be "simple"
env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "password");
Context ctx = new InitialContext(env); // AuthenticationException

// Cause 3: Expired password
// Password was changed on the server but not in the application config
env.put(Context.SECURITY_CREDENTIALS, "oldExpiredPassword");
Context ctx = new InitialContext(env); // AuthenticationException

// Cause 4: Bind DN is malformed
env.put(Context.SECURITY_PRINCIPAL, "admin");  // Should be full DN
env.put(Context.SECURITY_CREDENTIALS, "password");
Context ctx = new InitialContext(env); // AuthenticationException

// Cause 5: SASL mechanism not supported or misconfigured
env.put(Context.SECURITY_AUTHENTICATION, "DIGEST-MD5");
env.put(Context.SECURITY_PRINCIPAL, "user@EXAMPLE.COM");
Context ctx = new InitialContext(env); // AuthenticationException
```

## Solutions

### Fix 1: Verify Credentials and Principal Format

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");

// Use the correct DN format for the principal
env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "correctPassword");
env.put(Context.SECURITY_AUTHENTICATION, "simple");

try {
    Context ctx = new InitialContext(env);
    Object obj = ctx.lookup("cn=users,dc=example,dc=com");
} catch (javax.naming.AuthenticationException e) {
    System.err.println("Authentication failed: " + e.getMessage());
    System.err.println("Verify the bind DN and password are correct.");
}
```

### Fix 2: Externalize Credentials to Configuration

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Hashtable;

public class LdapContextFactory {
    public static Context createSecureContext(String host, int port,
            String bindDn, String password) throws javax.naming.NamingException {
        Hashtable<String, String> env = new Hashtable<>();
        env.put(Context.INITIAL_CONTEXT_FACTORY,
                "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(Context.PROVIDER_URL, "ldap://" + host + ":" + port);
        env.put(Context.SECURITY_AUTHENTICATION, "simple");
        env.put(Context.SECURITY_PRINCIPAL, bindDn);
        env.put(Context.SECURITY_CREDENTIALS, password);
        return new InitialContext(env);
    }
}

// Usage — load credentials from environment variables or vault
String bindDn = System.getenv("LDAP_BIND_DN");
String password = System.getenv("LDAP_PASSWORD");
Context ctx = LdapContextFactory.createSecureContext(
        "ldap.example.com", 389, bindDn, password);
```

### Fix 3: Handle Expired Passwords with Graceful Error Handling

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.AuthenticationException;

public Context authenticateWithRetry(String bindDn, String password,
        String host, int port) throws javax.naming.NamingException {
    try {
        return createLdapContext(bindDn, password, host, port);
    } catch (AuthenticationException e) {
        if (e.getMessage() != null && e.getMessage().contains("49")) {
            // LDAP error code 49 = invalid credentials
            // Could indicate expired password — prompt user or notify admin
            System.err.println("Credentials rejected. If password was recently "
                    + "changed, update the configuration.");
        }
        throw e;
    }
}

private Context createLdapContext(String bindDn, String password,
        String host, int port) throws javax.naming.NamingException {
    Hashtable<String, String> env = new Hashtable<>();
    env.put(Context.INITIAL_CONTEXT_FACTORY,
            "com.sun.jndi.ldap.LdapCtxFactory");
    env.put(Context.PROVIDER_URL, "ldap://" + host + ":" + port);
    env.put(Context.SECURITY_AUTHENTICATION, "simple");
    env.put(Context.SECURITY_PRINCIPAL, bindDn);
    env.put(Context.SECURITY_CREDENTIALS, password);
    return new InitialContext(env);
}
```

### Fix 4: Use StartTLS for Secure Connections

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.directory.DirContext;
import javax.naming.directory.InitialDirContext;
import javax.net.ssl.SSLContext;
import java.util.Hashtable;

Hashtable<String, Object> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "password");

// Use LDAPS for secure authentication
env.put(Context.SECURITY_PROTOCOL, "ssl");

DirContext ctx = new InitialDirContext(env);
```

## Prevention Checklist

- Store credentials in a secrets manager, not in source code
- Use environment variables or configuration files for bind DN and password
- Always use `simple` or a supported SASL mechanism for `SECURITY_AUTHENTICATION`
- Verify the principal DN format matches the directory schema
- Monitor password expiration policies and rotate credentials proactively
- Use LDAPS (`SECURITY_PROTOCOL = ssl`) to protect credentials in transit

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [CommunicationException](/languages/java/communicationexception) — Network communication failure
- [ServiceUnavailableException](/languages/java/serviceunavailableexception) — Naming service unavailable
- [SecurityException](/languages/java/securityexception) — General security violation
