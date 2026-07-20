---
title: "[Solution] Java AuthenticationException — Spring Security authentication failure"
description: "Fix Java AuthenticationException by checking credentials, verifying UserDetailsService, and handling the authentication flow. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 105
---

# AuthenticationException — Spring Security authentication failure

An `AuthenticationException` is thrown by Spring Security when a user cannot be authenticated. This covers invalid credentials, missing tokens, expired sessions, and misconfigured authentication providers.

## Description

Spring Security processes authentication through the `AuthenticationManager`. When authentication fails at any stage, an `AuthenticationException` subclass is thrown. Common message variants include:

- `Bad credentials`
- `User is disabled`
- `User account is locked`
- `User credentials have expired`
- `An Authentication object was not found in the SecurityContext`
- `Full authentication is required to access this resource`

## Common Causes

```java
// Cause 1: Incorrect credentials in login request
@PostMapping("/login")
public ResponseEntity<?> login(@RequestBody LoginRequest req) {
    // req.password is wrong or user doesn't exist
    authenticationManager.authenticate(
        new UsernamePasswordAuthenticationToken(req.username, req.password)
    );
}

// Cause 2: UserDetailsService returns wrong user details
@Service
public class CustomUserDetailsService implements UserDetailsService {
    @Override
    public UserDetails loadUserByUsername(String username) {
        User user = repo.findByUsername(username);
        if (user == null) throw new UsernameNotFoundException(username);
        // Forgot to set enabled=true or authorities
        return User.withUsername(user.getName())
            .password(user.getHash())
            .build();  // No roles assigned
    }
}

// Cause 3: Password encoder mismatch
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
// But passwords stored as plain text in DB

// Cause 4: Missing AuthenticationManager configuration
// No AuthenticationProvider or UserDetailsService bean defined

// Cause 5: Token expired or malformed in JWT flow
```

## Solutions

### Fix 1: Implement a correct UserDetailsService

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) {
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));

        return org.springframework.security.core.userdetails.User
            .withUsername(user.getUsername())
            .password(user.getPasswordHash())
            .roles(user.getRoles().toArray(new String[0]))
            .accountLocked(user.isLocked())
            .disabled(!user.isActive())
            .build();
    }
}
```

### Fix 2: Match password encoding

```java
@Service
public class RegistrationService {

    private final PasswordEncoder passwordEncoder;
    private final UserRepository userRepository;

    public RegistrationService(PasswordEncoder passwordEncoder, UserRepository userRepository) {
        this.passwordEncoder = passwordEncoder;
        this.userRepository = userRepository;
    }

    public void register(RegisterRequest request) {
        User user = new User();
        user.setUsername(request.username());
        user.setPasswordHash(passwordEncoder.encode(request.password()));  // Encode on save
        user.setRoles(Set.of("USER"));
        userRepository.save(user);
    }
}

// Configure encoder
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

### Fix 3: Configure the AuthenticationManager

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }
}
```

### Fix 4: Handle JWT authentication properly

```java
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtService jwtService;
    private final UserDetailsService userDetailsService;

    public JwtAuthenticationFilter(JwtService jwtService, UserDetailsService userDetailsService) {
        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {
        String header = request.getHeader("Authorization");

        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            try {
                String username = jwtService.extractUsername(token);
                UserDetails userDetails = userDetailsService.loadUserByUsername(username);

                if (jwtService.isTokenValid(token, userDetails)) {
                    UsernamePasswordAuthenticationToken auth =
                        new UsernamePasswordAuthenticationToken(userDetails, null,
                            userDetails.getAuthorities());
                    SecurityContextHolder.getContext().setAuthentication(auth);
                }
            } catch (Exception e) {
                SecurityContextHolder.clearContext();
            }
        }
        filterChain.doFilter(request, response);
    }
}
```

### Fix 5: Custom authentication entry point

```java
@Component
public class CustomAuthenticationEntryPoint implements AuthenticationEntryPoint {

    @Override
    public void commence(HttpServletRequest request,
                         HttpServletResponse response,
                         AuthenticationException authException) throws IOException {
        response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        response.setContentType("application/json");
        response.getWriter().write("{\"error\": \"Authentication required\", " +
            "\"message\": \"" + authException.getMessage() + "\"}");
    }
}
```

## Prevention Checklist

- Ensure `UserDetailsService` returns correct authorities and account status
- Always use `PasswordEncoder` — never store or compare plain-text passwords
- Configure `AuthenticationManager` explicitly when using custom providers
- Validate JWT tokens including expiration, issuer, and signature
- Set `AuthenticationEntryPoint` for consistent 401 responses
- Test authentication flow with valid and invalid credentials

## Related Errors

- [AccessDeniedException](/languages/java/spring-security-access-denied/)
- [BadCredentialsException](/languages/java/authenticationexception/)
- [UsernameNotFoundException](/languages/java/spring-nosuchbean/)
