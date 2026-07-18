---
title: "[Solution] GitLab CI Include Error"
description: "Fix GitLab CI include errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Include Error

Include errors occur when the include directive fails to load external files or templates.

## Why This Happens

- File path incorrect
- Template has invalid YAML
- Remote URL not accessible
- Circular include references

## Common Error Messages

- `include_file_not_found`
- `include_template_error`
- `include_remote_failed`
- `include_circular`

## How to Fix It

### Solution 1: Verify file paths

Relative paths are from repository root. Use `/` prefix for absolute paths.

### Solution 2: Use local includes

For frequently used templates, include from the same repository:

```yaml
include:
  - local: '/templates/deploy.yml'
```

### Solution 3: Validate included files

Each included file must be valid YAML independently.


## Common Scenarios

- **File not found:** Check if the file exists at the specified path.
- **Template has errors:** Validate the included file separately with yamllint.

## Prevent It

- Use relative paths
- Validate files independently
- Document dependencies
