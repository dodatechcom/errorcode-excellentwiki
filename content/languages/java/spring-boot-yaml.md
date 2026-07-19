---
title: "[Solution] YAMLException — Spring Boot YAML Parsing Fix"
description: "Fix YAMLException and MalformedInputException in Spring Boot YAML configuration. Resolve encoding and syntax issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# YAMLException — Spring Boot YAML Parsing Fix

A `YAMLException` with `MalformedInputException` means Spring Boot's YAML parser encountered invalid characters or encoding issues in your configuration files. This is often caused by non-UTF-8 encoded files or YAML syntax errors.

## What This Error Means

Common messages:

- `org.yaml.snakeyaml.error.YAMLException: java.nio.charset.MalformedInputException`
- `YAMLException: while parsing a block mapping`
- `YAMLException: unexpected character found`

## Common Causes

```yaml
# Cause 1: Non-UTF-8 encoding with special characters
app:
  greeting: Hello café  # accented chars in non-UTF-8 file

# Cause 2: Tab characters (YAML only allows spaces)
app:
	name: myapp  # Tab character causes parse error

# Cause 3: Unquoted colons in values
app:
  url: http://example.com:8080  # Unquoted colon can confuse parser
```

## How to Fix

### Fix 1: Convert files to UTF-8 encoding

Ensure all YAML files are saved with UTF-8 encoding to prevent character encoding issues.

```java
# Check file encoding
file --mime-encoding application.yml

# Convert to UTF-8
iconv -f ISO-8859-1 -t UTF-8 application.yml > application_utf8.yml

# Or use a batch conversion
find . -name "*.yml" -exec sh -c '
    for f; do
        encoding=$(file --mime-encoding "$f" | awk -F: "{print $2}")
        if [ "$encoding" != "utf-8" ]; then
            iconv -f "$encoding" -t UTF-8 "$f" > "$f.utf8"
            mv "$f.utf8" "$f"
            echo "Converted: $f"
        fi
    done
' _ {} +
```

### Fix 2: Validate YAML syntax before deployment

Add YAML validation to your build process using SnakeYAML or a CI check to catch syntax errors early.

```java
// Add to your test suite
@Test
void applicationYamlShouldBeValid() throws Exception {
    Yaml yaml = new Yaml();
    try (InputStream is = getClass().getClassLoader()
            .getResourceAsStream("application.yml")) {
        assertNotNull(is, "application.yml not found on classpath");

        // Parse without errors
        Map<String, Object> config = yaml.load(is);
        assertNotNull(config);
        assertTrue(config.containsKey("spring"));
    }
}

// Or validate YAML structure with Jackson
@Test
void yamlShouldParseWithObjectMapper() throws Exception {
    ObjectMapper yamlMapper = new ObjectMapper(
        new YAMLFactory());
    Map<String, Object> config = yamlMapper.readValue(
        new File("src/main/resources/application.yml"),
        Map.class);
    assertNotNull(config.get("spring"));
}
```

### Fix 3: Use multi-document YAML with proper separators

When using profile-specific YAML, ensure document separators (---) are placed correctly with no extra whitespace.

```java
# application.yml
spring:
  application:
    name: myapp

---
# Profile-specific configuration
spring:
  config:
    activate:
      on-profile: development
  datasource:
    url: jdbc:h2:mem:devdb

---
spring:
  config:
    activate:
      on-profile: production
  datasource:
    url: jdbc:postgresql://prod-host:5432/mydb
```

## Related Errors

- {{< relref "spring-boot-properties" >}} — ConfigurationProperties Bind Error
- {{< relref "spring-boot-profile" >}} — Profile Activation Error
