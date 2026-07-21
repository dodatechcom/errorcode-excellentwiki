---
title: "[Solution] Spring Security Configuration Error -- How to Fix"
description: "Fix Spring Security configuration errors. Resolve authentication, authorization, and security filter issues."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring Security configuration error occurs when the security filter chain is misconfigured, authentication fails, or authorization rules block legitimate requests. Security misconfiguration is a critical vulnerability.

## Why It Happens

Spring Security uses a filter chain to process requests. Errors occur when the security configuration is too restrictive or too permissive, when password encoders don't match, when CSRF protection interferes with API calls, when CORS configuration conflicts with security headers, or when authentication providers are not properly registered.

## Common Error Messages

```
AccessDeniedException: Access is denied
```

```
BadCredentialsException: Bad credentials
```

```
AuthenticationServiceException: Failed to authenticate
```

```
InvalidCsrfTokenException: Invalid CSRF Token
```

## How to Fix It

### 1. Configure Security Filter Chain

Set up the security configuration properly:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())  // For REST APIs
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/**").authenticated()
                .anyRequest().permitAll()
            )
            .httpBasic(Customizer.withDefaults())
            .sessionManagement(session ->
                session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            );
        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### 2. Fix Password Encoder Mismatches

Ensure password encoding is consistent:

```java
@Service
public class UserDetailsService implements org.springframework.security.core.userdetails.UserDetailsService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserDetailsService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public UserDetails loadUserByUsername(String email) {
        User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new UsernameNotFoundException("User not found: " + email));
        return org.springframework.security.core.userdetails.User
            .withUsername(user.getEmail())
            .password(user.getPassword())
            .roles(user.getRole())
            .build();
    }
}

// When creating users
public User createUser(String email, String rawPassword) {
    User user = new User();
    user.setEmail(email);
    user.setPassword(passwordEncoder.encode(rawPassword));  // Always encode
    return userRepository.save(user);
}
```

### 3. Configure CORS with Security

Allow cross-origin requests through security:

```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .cors(cors -> cors.configurationSource(corsConfigurationSource()))
        .csrf(csrf -> csrf.disable())
        .authorizeHttpRequests(auth -> auth
            .anyRequest().authenticated()
        );
    return http.build();
}

@Bean
public CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();
    config.setAllowedOrigins(List.of("http://localhost:3000"));
    config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE"));
    config.setAllowedHeaders(List.of("*"));
    config.setAllowCredentials(true);

    UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/api/**", config);
    return source;
}
```

### 4. Custom Authentication Provider

Implement custom authentication:

```java
@Component
public class CustomAuthenticationProvider implements AuthenticationProvider {

    @Override
    public Authentication authenticate(Authentication authentication) {
        String email = authentication.getName();
        String password = authentication.getCredentials().toString();

        User user = userService.findByEmail(email);
        if (user != null && passwordEncoder.matches(password, user.getPassword())) {
            return new UsernamePasswordAuthenticationToken(
                user, null, List.of(new SimpleGrantedAuthority("ROLE_" + user.getRole()))
            );
        }
        throw new BadCredentialsException("Invalid credentials");
    }

    @Override
    public boolean supports(Class<?> authentication) {
        return UsernamePasswordAuthenticationToken.class.isAssignableFrom(authentication);
    }
}
```

## Common Scenarios

**Scenario 1: All endpoints return 403 Forbidden.**
Check that the security configuration permits the required paths. Use `.permitAll()` for public endpoints.

**Scenario 2: CSRF token error in API.**
REST APIs should disable CSRF as they use token-based authentication. Keep CSRF enabled for form-based web applications.

**Scenario 3: Login fails with "Bad credentials".**
Verify that the password encoder in login matches the one used during registration. BCrypt, SCrypt, and other encoders are not interchangeable.

## Prevent It

1. **Never use `.permitAll()` on sensitive endpoints.** Follow the principle of least privilege.

2. **Disable CSRF only for stateless APIs.** Keep CSRF protection for server-rendered applications.

3. **Test security configuration with `@WithMockUser`** for unit tests and `@WithSecurityContext` for integration tests.
