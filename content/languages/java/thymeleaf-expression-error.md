---
title: "[Solution] Java Thymeleaf SpEL expression error — template expression evaluation failure"
description: "Fix Java Thymeleaf SpEL expression error by checking expression syntax, verifying context variables, and handling null. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 117
---

# Thymeleaf SpEL expression error — template expression evaluation failure

A Thymeleaf SpEL expression error occurs when a Spring Expression Language (SpEL) expression in a template cannot be evaluated. This includes null pointer access, invalid syntax, missing variables, and type mismatches in expressions.

## Description

Thymeleaf uses SpEL expressions inside `th:text`, `th:if`, `th:each`, and other attributes. When the expression evaluates to an error state, Thymeleaf throws an exception. Common message variants include:

- `TemplateProcessingException: Exception evaluating SpringEL expression`
- `SpelEvaluationException: EL1007E: Property or field 'X' cannot be found on null`
- `SpelEvaluationException: EL1011E: Past limit of indexes`
- `SpelParseException: Expression [X] is not valid`
- `Could not access bean property 'X': Method threw exception`

## Common Causes

```html
<!-- Cause 1: Accessing property on null object -->
<div th:text="${user.name}">Name</div>
<!-- user is null — throws SpelEvaluationException -->

<!-- Cause 2: Invalid SpEL syntax -->
<div th:text="${items[0].name()}">Name</div>
<!-- items is empty — index out of bounds -->

<!-- Cause 3: Wrong property name -->
<div th:text="${user.fullName}">Name</div>
<!-- User has 'name' not 'fullName' -->

<!-- Cause 4: Calling nonexistent method -->
<div th:text="${user.getDisplayName()}">Name</div>
<!-- User has no getDisplayName() method -->

<!-- Cause 5: Wrong collection syntax -->
<div th:each="item : ${items}">
    <span th:text="${item.name}">Name</span>
</div>
<!-- items is not a collection — iteration fails -->
```

## Solutions

### Fix 1: Use null-safe access with Elvis operator

```html
<!-- Elvis operator returns default value when null -->
<div th:text="${user?.name ?: 'Unknown'}">Name</div>

<!-- Null-safe with default -->
<span th:text="${user?.email ?: 'No email'}">Email</span>

<!-- Check null before accessing -->
<div th:if="${user != null}">
    <h1 th:text="${user.name}">Name</h1>
</div>

<!-- Safe navigation on nested objects -->
<div th:text="${user?.address?.city ?: 'No city'}">City</div>
```

### Fix 2: Validate collections before iteration

```html
<!-- Safe iteration with empty check -->
<div th:if="${items != null and items.size() > 0}">
    <ul>
        <li th:each="item, iterStat : ${items}">
            <span th:text="${item.name}">Name</span>
        </li>
    </ul>
</div>

<!-- Handle empty list gracefully -->
<div th:if="${items != null and items.isEmpty()}">
    <p>No items found</p>
</div>

<!-- Safe indexing -->
<li th:each="item, iterStat : ${items}">
    <span th:text="${iterStat.index + 1}">1</span>
    <span th:text="${item.name}">Name</span>
</li>
```

### Fix 3: Use correct property names and methods

```html
<!-- WRONG — property doesn't exist -->
<div th:text="${user.fullName}">Name</div>

<!-- CORRECT — matches Java field name -->
<div th:text="${user.name}">Name</div>

<!-- Use method call if available -->
<div th:text="${user.getDisplayName()}">Display Name</div>

<!-- Use utility methods in model -->
<div th:text="${T(java.lang.String).format('%s %s', user.firstName, user.lastName)}">
    Full Name
</div>
```

### Fix 4: Provide variables with safe defaults in controller

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
        model.addAttribute("orders", user != null ? user.getOrders() : Collections.emptyList());
        model.addAttribute("address", user != null ? user.getAddress() : null);
        model.addAttribute("pageReady", true);
        return "user/profile";
    }
}
```

### Fix 5: Use Thymeleaf utility objects for safe expressions

```html
<!-- Use #strings utility -->
<span th:text="${#strings.isEmpty(user?.name) ? 'Unknown' : user.name}">Name</span>

<!-- Use #lists utility -->
<div th:if="${#lists.size(items) > 0}">
    <span th:each="item : ${items}" th:text="${item.name}">Item</span>
</div>

<!-- Use #dates utility -->
<span th:text="${#dates.format(user.createdAt, 'yyyy-MM-dd')}">Date</span>

<!-- Use #maps utility for maps -->
<div th:each="entry : ${#maps.entrySet(userPreferences)}">
    <span th:text="${entry.key}">Key</span>:
    <span th:text="${entry.value}">Value</span>
</div>

<!-- Use #numbers utility -->
<span th:text="${#numbers.formatDecimal(price, 1, 2)}">0.00</span>
```

## Prevention Checklist

- Always provide null-safe expressions using the Elvis operator (`?:`) or safe navigation (`?.`)
- Check collection emptiness before using `th:each`
- Verify SpEL property names match Java field names exactly
- Provide all required model attributes with safe defaults in the controller
- Use Thymeleaf utility objects (`#strings`, `#lists`, `#dates`) for common operations
- Test templates with realistic data including edge cases (null, empty collections)

## Related Errors

- [Thymeleaf TemplateEngine error](/languages/java/thymeleaf-template-error/)
- [SpelEvaluationException](/languages/java/npe-method-chain/)
- [NullPointerException](/languages/java/nullpointerexception/)
