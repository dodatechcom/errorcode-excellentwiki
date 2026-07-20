---
title: "[Solution] Java Thymeleaf TemplateEngine error — template not found or rendering failure"
description: "Fix Java Thymeleaf TemplateEngine error by checking template syntax, verifying variables, and clearing cache. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 116
---

# Thymeleaf TemplateEngine error — template not found or rendering failure

A Thymeleaf `TemplateEngine` error occurs when the template cannot be found, has syntax errors, or references undefined variables. This covers template resolution failures, parsing errors, and expression evaluation problems.

## Description

Thymeleaf resolves templates by name and processes them through its template engine. Errors occur during resolution, parsing, or execution. Common message variants include:

- `TemplateInputException: Error resolving template [X]`
- `org.thymeleaf.exceptions.TemplateProcessingException`
- `Could not resolve view with name 'X' in servlet with name 'thymeleaf'`
- `Template was not found for resource [X]`
- `Attribute value expression does not evaluate`

## Common Causes

```html
<!-- Cause 1: Template not found -->
<!-- Missing: src/main/resources/templates/user/profile.html -->
<!-- Controller returns "user/profile" as view name -->
@GetMapping("/profile")
public String profile(Model model) {
    return "user/profile";  // Thymeleaf cannot find the template
}

<!-- Cause 2: Syntax errors in template -->
<div th:if="${user != null">  <!-- Missing closing bracket -->
    <span th:text="${user.name}">Name</span>
</div>

<!-- Cause 3: Undefined variable in template -->
<div th:text="${userName}">Name</div>
<!-- Model doesn't contain "userName" attribute -->

<!-- Cause 4: Incorrect Thymeleaf namespace -->
<html xmlns:th="http://www.thymeleaf.org">  <!-- Wrong namespace -->
```

## Solutions

### Fix 1: Verify template file location and name

```
src/main/resources/
├── templates/
│   ├── user/
│   │   ├── profile.html
│   │   └── list.html
│   ├── home.html
│   └── error.html
└── static/
    └── css/
```

```java
@Controller
public class UserController {

    @GetMapping("/user/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        model.addAttribute("user", userService.findById(id));
        return "user/profile";  // Resolves to templates/user/profile.html
    }

    @GetMapping("/users")
    public String listUsers(Model model) {
        model.addAttribute("users", userService.findAll());
        return "user/list";  // Resolves to templates/user/list.html
    }
}
```

### Fix 2: Check Thymeleaf template syntax

```html
<!-- CORRECT syntax -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title th:text="${title}">Default Title</title>
</head>
<body>
    <!-- Conditionals -->
    <div th:if="${user != null}">
        <h1 th:text="${user.name}">Name</h1>
    </div>
    <div th:unless="${user != null}">
        <p>User not found</p>
    </div>

    <!-- Loops -->
    <ul>
        <li th:each="item : ${items}" th:text="${item.name}">Item</li>
    </ul>

    <!-- Links -->
    <a th:href="@{/users/{id}(id=${user.id})}">Profile</a>

    <!-- Forms -->
    <form th:action="@{/users}" th:object="${user}" method="post">
        <input type="text" th:field="*{name}"/>
    </form>
</body>
</html>
```

### Fix 3: Provide all required model attributes

```java
@Controller
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/user/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = userService.findById(id);
        model.addAttribute("user", user);
        model.addAttribute("title", "User Profile");  // Provide all needed attributes
        model.addAttribute("pageTitle", user.getName() + " - Profile");
        return "user/profile";
    }

    @GetMapping("/user/{id}/edit")
    public String editForm(@PathVariable Long id, Model model) {
        model.addAttribute("user", userService.findById(id));
        model.addAttribute("departments", departmentService.findAll());
        model.addAttribute("roles", Role.values());
        return "user/edit";
    }
}
```

### Fix 4: Clear template cache during development

```yaml
spring:
  thymeleaf:
    cache: false  # Disable cache in development
    prefix: classpath:/templates/
    suffix: .html
    encoding: UTF-8
    mode: HTML
```

```java
// Or clear cache programmatically
@Autowired
private TemplateEngine templateEngine;

@EventListener
public void handleRefresh(ContextRefreshedEvent event) {
    templateEngine.clearTemplateCache();
}
```

### Fix 5: Use fragments for reusable components

```html
<!-- src/main/resources/templates/fragments/header.html -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<div th:fragment="header(title)">
    <nav>
        <a th:href="@{/}">Home</a>
        <span th:text="${title}">Page Title</span>
    </nav>
</div>
</html>

<!-- Usage in another template -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{fragments/header :: header('User Profile')}"></head>
<body>
    <div th:text="${user.name}">Name</div>
</body>
</html>
```

## Prevention Checklist

- Ensure template files exist in `src/main/resources/templates/` with correct paths
- Use `th:if`, `th:unless`, and `th:text` with correct bracket syntax
- Provide all required model attributes in the controller before returning the view name
- Disable `spring.thymeleaf.cache` during development to see template changes immediately
- Use Thymeleaf fragment syntax (`~{}`) for reusable components
- Test templates independently with `thymeleaf-testing` or browser preview

## Related Errors

- [Thymeleaf ExpressionError](/languages/java/thymeleaf-expression-error/)
- [TemplateInputException](/languages/java/servlet-exception/)
- [NullPointerException in template](/languages/java/npe-method-chain/)
