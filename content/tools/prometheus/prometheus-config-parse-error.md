---
title: "[Solution] Prometheus Config Parse Error"
description: "How to fix Prometheus configuration file parse errors in prometheus.yml"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid YAML syntax in prometheus.yml
- Indentation errors in configuration
- Missing colons after keys
- Tab characters mixed with spaces
- Unterminated quotes in string values

## How to Fix

Validate the configuration file:

```bash
promtool check config prometheus.yml
```

Check YAML syntax manually:

```bash
python3 -c "import yaml; yaml.safe_load(open('prometheus.yml'))"
```

Use a YAML linter:

```bash
yamllint prometheus.yml
```

Common YAML syntax fixes:

```yaml
# Wrong (tab character)
->global:
->  scrape_interval: 15s

# Correct (spaces only)
global:
  scrape_interval: 15s
```

Fix unterminated strings:

```yaml
# Wrong
job_name: 'my-job

# Correct
job_name: 'my-job'
```

## Examples

```bash
# Validate config
promtool check config prometheus.yml

# Check with verbose output
promtool check config --verbose prometheus.yml

# View parsed config
prometheus --config.file=prometheus.yml --dry-run
```
