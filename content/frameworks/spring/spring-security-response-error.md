---
title: "[Solution] Spring Security Response Error"
description: "Fix Spring Security response errors when security-related HTTP responses are incorrect or missing headers."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

Security response errors occur when security headers are not included, CSRF tokens are missing, or authentication responses are malformed.

## Common Causes

- Security headers not configured
- CSRF token not included in response
- WWW-Authenticate header missing
- Cache-Control headers interfere with security
- Content-Security-Policy not configured

## How to Fix

### Configure Security Headers

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .headers(headers -> headers
                .contentSecurityPolicy(csp -> csp.policyDirectives("default-src 'self'"))
                .frameOptions(frame -> frame.deny())
                .contentTypeOptions(Customizer.withDefaults())
                .httpStrictTransportSecurity(hsts -> hsts
                    .includeSubDomains(true)
                    .maxAgeInSeconds(31536000)
                )
            );
        return http.build();
    }
}
```

### Add Custom Security Headers

```java
@Component
public class SecurityHeadersFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) {
        HttpServletResponse response = (HttpServletResponse) res;
        response.setHeader("X-Content-Type-Options", "nosniff");
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("X-XSS-Protection", "1; mode=block");
        chain.doFilter(req, res);
    }
}
```

### Handle Authentication Challenge

```java
http
    .httpBasic(basic -> basic
        .authenticationEntryPoint((request, response, authException) -> {
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            response.setHeader("WWW-Authenticate", "Basic realm="MyApp"");
            response.getWriter().write("{"error": "unauthorized"}");
        })
    );
```

## Examples

```java
// Bug -- no security headers
http.authorizeHttpRequests(auth -> auth.anyRequest().authenticated());
// Missing X-Frame-Options, CSP, etc.

// Fix -- add headers
http.headers(headers -> headers.frameOptions(frame -> frame.deny()));
```
