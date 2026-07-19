---
title: "[Solution] IntelliJ IDEA Generate code error"
description: "Fix IntelliJ IDEA code generation failures. Resolve Alt+Insert generator errors, getter/setter issues, and template problems."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "code-generation", "generators", "getters-setters", "constructors"]
severity: "error"
---

# Generate code error

## Error Message

```
Generate code error
Cannot generate getters and setters: no fields found
Generate Constructor: superclass constructor not accessible
Override Methods: no methods available to override
Generate equals() and hashCode(): Lombok detected but not configured
```

## Common Causes

- Class has no fields to generate getters/setters from
- Superclass constructor is private and cannot be called
- No methods available to override from parent classes
- Lombok or other code generation tools conflict with IDE generators
- Record type classes have different generation rules

## Solutions

### Solution 1: Generate Getters and Setters

Use the code generator to create accessor methods for class fields.

```
# Position cursor inside the class body
# Press Alt+Insert (Windows/Linux) or ⌘N (macOS)
# Select 'Getter and Setter'

# In the dialog:
#   Select fields to generate for:
#     ☑ id
#     ☑ name
#     ☑ email
#   Choose:
#     - Getters and Setters
#     - Getters only
#     - Setters only
#     - Getters and isSetters (for boolean)
# Click 'OK' to generate

# Generated code:
public Long getId() { return id; }
public void setId(Long id) { this.id = id; }
```

### Solution 2: Generate Constructor

Generate constructors for your class with selected fields.

```
# Alt+Insert → Constructor

# Select fields to include:
#   ☑ id
#   ☑ name
#   ☑ email

# Options:
#   - Superclass constructor available: Call 'super()'
#   - Initialize final fields

# For records (Java 14+):
# The constructor is generated automatically
# Use Alt+Insert → 'Canonical Constructor' if needed

# Generated:
public User(Long id, String name, String email) {
    this.id = id;
    this.name = name;
    this.email = email;
}
```

### Solution 3: Override Methods from Superclass

Generate method overrides for all or selected methods from parent classes.

```
# Alt+Insert → Override Methods

# In the dialog:
#   Tree view of available methods from:
#     - java.lang.Object
#     - Parent class methods
#     - Interface methods
#   ☑ Select methods to override
#   Click 'OK'

# Generated with @Override annotation:
@Override
public String toString() {
    return "User{" +
        "id=" + id +
        ", name='" + name + '\'' +
        '}';
}

# For implementing interface methods:
# Alt+Insert → Implement Methods
```

### Solution 4: Generate equals() and hashCode()

Generate equals and hashCode methods based on selected fields.

```
# Alt+Insert → equals() and hashCode()

# Step 1: Select fields for equals()
#   ☑ id
#   ☑ email
# Click 'Next'

# Step 2: Select fields for hashCode()
#   ☑ id
#   ☑ email
# Click 'OK'

# If using Lombok, ensure annotation processing is enabled:
# File → Settings → Build → Compiler → Annotation Processors
# ☑ Enable annotation processing
# Then use @Data, @Getter, @Setter annotations instead

# For records:
# equals() and hashCode() are auto-generated
```

## Prevention Tips

- Use Alt+Insert (Generate) frequently to avoid writing boilerplate code manually
- Customize generation templates in File → Settings → Code Generation
- Use Live Templates alongside code generators for additional patterns
- For Lombok projects, prefer annotations over IDE code generation

## Related Errors

- [Surround Error]({{< relref "/tools/intellij/surround-error" >}})
- [Code Completion Error]({{< relref "/tools/intellij/code-completion-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
