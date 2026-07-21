---
title: "[Solution] Spring Security Login Error"
description: "Fix Spring Security login errors when authentication fails or login page is not accessible."
frameworks: ["spring"]
error-types: ["authentication-error"]
severities: ["error"]
---

Login errors in Spring Security occur when authentication configuration is incorrect, login page is not properly configured, or credentials are not validated.

## Common Causes

- Login page URL does not match security configuration
- UserDetailsService not properly configured
- Password encoder not matched with stored passwords
- CSRF token not included in login form
- Session fixation protection interferes with login

## How to Fix

### Configure Login Page

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/login", "/register").permitAll()
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard")
                .failureUrl("/login?error=true")
                .permitAll()
            )
            .logout(logout -> logout
                .logoutSuccessUrl("/login?logout=true")
                .permitAll()
            );
        return http.build();
    }
}
```

### Configure UserDetailsService

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {
    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found"));
        return org.springframework.security.core.userdetails.User
            .withUsername(user.getUsername())
            .password(user.getPassword())
            .roles("USER")
            .build();
    }
}
```

### Use Correct Password Encoder

```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

## Examples

```java
// Bug -- no password encoder
@Bean
public UserDetailsService userDetailsService() {
    return username -> {
        User user = userRepository.findByUsername(username);
        return org.springframework.security.core.userdetails.User
            .withUsername(user.getUsername())
            .password(user.getRawPassword())  // Raw password, not encoded
            .roles("USER")
            .build();
    };
}

// Fix -- encode passwords
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```
