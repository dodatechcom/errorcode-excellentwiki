---
title: "[Solution] Spring Security OAuth2 Error Fix"
description: "Fix Spring Security OAuth2 errors. Resolve token validation, redirect URI mismatch, and authorization server connectivity issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-security", "oauth2", "jwt", "token", "authorization"]
weight: 5
---

# Spring Security OAuth2 Error Fix

A Spring Security OAuth2 error occurs when the application fails to validate tokens, redirect to the authorization server, or process OAuth2 responses.

## What This Error Means

Common messages:

- `InvalidOAuth2AuthenticationException: Invalid token`
- `RedirectUriMismatchException: The redirect URI does not match`
- `OAuth2AuthorizationException: An error occurred while attempting to fetch the OAuth 2.0 Access Token`
- `JwtValidationException: JWT expired`

The OAuth2 flow fails at some point — token validation, authorization request, or token exchange. This typically involves misconfigured client registrations or expired credentials.

## Common Causes

```java
// Cause 1: Redirect URI mismatch
// Application configured with /login/oauth2/code/google
// But Google OAuth console has https://myapp.com/callback

// Cause 2: JWT token expired
// Access token lifetime exceeded before refresh

// Cause 3: Client secret incorrect
// application.yml has wrong client-secret

// Cause 4: Authorization server unreachable
// Keycloak or Auth0 endpoint down or changed
```

## How to Fix

### Fix 1: Match redirect URIs exactly

```yaml
# application.yml
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: ${GOOGLE_CLIENT_ID}
            client-secret: ${GOOGLE_CLIENT_SECRET}
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
            scope:
              - openid
              - profile
              - email
```

### Fix 2: Configure JWT validation properly

```java
@Bean
public JwtDecoder jwtDecoder() {
    NimbusJwtDecoder decoder = NimbusJwtDecoder.withJwkSetUri(jwkSetUri)
        .build();
    decoder.setJwtValidator(JwtValidators.createDefaultWithIssuer(issuerUri));
    return decoder;
}
```

### Fix 3: Add token refresh support

```java
@Bean
public OAuth2AuthorizedClientProvider authorizedClientProvider() {
    return OAuth2AuthorizedClientProviderBuilder.builder()
        .authorizationCode()
        .refreshToken()
        .clientCredentials()
        .build();
}
```

### Fix 4: Configure custom token exchange

```java
@Bean
public OAuth2TokenClient<OAuth2TokenExchangeRequest, OAuth2Token> tokenClient() {
    NimbusOAuth2TokenClient<OAuth2TokenExchangeRequest, OAuth2Token> client = new NimbusOAuth2TokenClient<>();
    client.setRequestUri(tokenUri);
    return client;
}
```

### Fix 5: Handle OAuth2 errors gracefully

```java
@ControllerAdvice
public class OAuth2ExceptionHandler {
    @ExceptionHandler(OAuth2AuthenticationException.class)
    public String handleOAuth2Error(OAuth2AuthenticationException ex, Model model) {
        model.addAttribute("error", ex.getError().getDescription());
        return "error/oauth2";
    }
}
```

## Related Errors

- {{< relref "spring-security" >}} — Spring Security general error.
- {{< relref "jwt-validation" >}} — JWT token validation failed.
