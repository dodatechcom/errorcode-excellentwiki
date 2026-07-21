---
title: "[Solution] Spring Security SAML Error"
description: "Fix Spring Security SAML errors when SAML authentication or assertion processing fails."
frameworks: ["spring"]
error-types: ["authentication-error"]
severities: ["error"]
---

SAML errors occur when SAML metadata is not properly configured, assertions cannot be validated, or the IdP is unreachable.

## Common Causes

- SAML metadata XML not loaded
- IdP certificate not configured
- Assertion signature validation fails
- Audience restriction mismatch
- ACS URL not matching IdP configuration

## How to Fix

### Configure SAML Authentication

```java
@Configuration
@EnableWebSecurity
public class SamlConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/saml/**").permitAll()
                .anyRequest().authenticated()
            )
            .saml2Login(saml2 -> saml2
                .loginPage("/saml/login")
                .relyingPartyRegistrationRepository(relayingPartyRegistrationRepository())
            );
        return http.build();
    }

    @Bean
    public RelyingPartyRegistrationRepository relayingPartyRegistrationRepository() {
        RelyingPartyRegistration registration = RelyingPartyRegistration
            .withRegistrationId("idp")
            .assertingPartyDetails(party -> party
                .entityId("https://idp.example.com")
                .singleSignOnServiceLocation("https://idp.example.com/sso")
                .wantAssertionsSigned(true)
                .signatureAlgorithms(algs -> algs.add(SignatureAlgorithm.RSA_SHA256))
            )
            .build();
        return new InMemoryRelyingPartyRegistrationRepository(registration);
    }
}
```

### Validate SAML Assertion

```java
@Component
public class SamlAssertionValidator {
    public boolean validate(Saml2AuthenticatedToken token) {
        Saml2Authentication auth = (Saml2Authentication) token.getPrincipal();
        // Validate assertion attributes
        return auth.getName() != null && !auth.getName().isEmpty();
    }
}
```

## Examples

```java
// Bug -- IdP metadata not loaded
// Fails to authenticate users

// Fix -- configure metadata location
RelyingPartyRegistration registration = RelyingPartyRegistration
    .withRegistrationId("idp")
    .assertingPartyDetails(party -> party
        .entityId("https://idp.example.com")
        .singleSignOnServiceLocation("https://idp.example.com/sso")
    )
    .build();
```
