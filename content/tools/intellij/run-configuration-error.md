---
title: "[Solution] IntelliJ IDEA Run configuration error"
description: "Fix IntelliJ IDEA run configuration errors. Resolve application launch failures, class not found errors, and configuration issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "run-configuration", "launch", "debug", "execution"]
severity: "error"
---

# Run configuration error

## Error Message

```
Run configuration error
Error: Main class 'com.example.Application' not found.
Cannot start process, working directory is not a directory.
ClassNotFoundException: com.example.Application
Error: Module 'my-module' not specified in run configuration.
```

## Common Causes

- Main class has been renamed or moved to a different package
- Module is missing from the run configuration
- Working directory path is invalid or contains spaces
- Classpath does not include required dependencies
- Run configuration template is outdated after project restructuring

## Solutions

### Solution 1: Update Main Class Configuration

Reconfigure the main class in the run configuration. Use the class browser to select the correct class.

```
Run → Edit Configurations
# Select your run configuration
# Click on 'Main class' field
# Click the '...' button to browse for the class
# Select the correct main class from the list
# Click 'Apply' then 'OK'

# For Spring Boot:
# Main class: com.example.Application
# Ensure @SpringBootApplication annotation is present
```

### Solution 2: Fix Module Assignment

Ensure the correct module is assigned to the run configuration.

```
Run → Edit Configurations
# Select your configuration
# Under 'Module' dropdown:
#   Select the correct module for your application
#   This should match the module containing your main class

# If module is missing:
# File → Project Structure → Modules
# Ensure all modules are properly configured
# Click '+' → Import Module if needed
```

### Solution 3: Set Correct Working Directory

Configure the working directory for the run configuration.

```
Run → Edit Configurations
# Under 'Working directory':
#   Click folder icon to browse
#   Select your project root directory
#   Or use module file path: $MODULE_DIR$

# For web applications, ensure working directory
# is set to where static resources are located

# For Maven/Gradle projects:
# Working directory: $MODULE_DIR$
```

### Solution 4: Reset Run Configuration from Template

Delete the problematic run configuration and create a fresh one from the default template.

```
Run → Edit Configurations
# Delete the problematic configuration
# Click '+' → Application (or Spring Boot)
# Name: My Application
# Main class: Browse and select correct class
# Module: Select correct module
# JVM options: -Xmx2048m
# Working directory: $MODULE_DIR$
# Click 'Apply' then 'OK'

# To reset all templates:
# Run → Edit Configurations → Click gear icon
# → Restore Defaults
```

## Prevention Tips

- Use 'Store as project file' to share run configurations with the team via version control
- Configure environment variables in the run configuration dialog instead of shell profiles
- Use 'Shorten command line' option when the classpath exceeds OS limits
- Create run configuration templates for consistent team configurations

## Related Errors

- [Debug Error]({{< relref "/tools/intellij/debug-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Test Error]({{< relref "/tools/intellij/test-error" >}})
