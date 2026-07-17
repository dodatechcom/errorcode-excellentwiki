---
title: "[Solution] Azure DevOps — pipeline YAML error"
description: "Fix Azure DevOps pipeline YAML error. Resolve pipeline syntax and configuration issues."
cloud: ["azure"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["azure", "devops", "pipeline", "yaml", "error", "build", "release"]
weight: 5
---

An Azure DevOps pipeline YAML error means the pipeline definition file has syntax or configuration errors that prevent the pipeline from running. The validation fails before any tasks execute.

## What This Error Means

Azure DevOps validates the `azure-pipelines.yml` file before running it. YAML syntax errors, invalid task references, undefined variables, or structural issues cause the pipeline to fail at the validation stage. The error message identifies the specific line and type of error. Common issues include indentation errors, invalid template references, undefined variables, and tasks that require extensions not installed in the organization.

## Common Causes

- YAML indentation errors (tabs vs spaces, inconsistent indentation)
- Undefined pipeline variables used without default values
- Invalid task name or version (e.g., wrong extension installed)
- Template file not found at the specified path
- Circular template references
- Stage/step/job structure violates the pipeline schema
- Missing required parameters for tasks

## How to Fix

### Validate YAML Locally

```bash
# Install Azure DevOps CLI extension
az extension add --name azure-devops

# Validate pipeline
az pipelines validate --file azure-pipelines.yml
```

### Check YAML Syntax

```bash
# Basic YAML validation
python -c "import yaml; yaml.safe_load(open('azure-pipelines.yml'))"
```

### Fix Common Indentation Errors

```yaml
# Correct: 2-space indentation
trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - script: echo "Hello"
    displayName: 'Say Hello'
```

### Define Missing Variables

```yaml
variables:
  buildConfiguration: 'Release'
  dotnetVersion: '8.0.x'

stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - task: DotNetCoreCLI@2
            inputs:
              command: 'build'
              projects: '**/*.csproj'
              arguments: '--configuration $(buildConfiguration)'
```

### Fix Template References

```yaml
# Use correct relative path
resources:
  repositories:
    - repository: templates
      type: github
      name: org/repo

steps:
  - template: templates/build.yml@templates
```

### Check Task Versions

```yaml
# Use explicit version
- task: UseNode@1
  inputs:
    version: '18.x'

# Or use latest
- task: NodeTool@0
  inputs:
    versionSpec: '18.x'
```

### Debug Pipeline

```bash
# Enable system diagnostics
# Add variable: system.debug = true
```

## Related Errors

- [Azure DevOps Error]({{< relref "/cloud/azure/azure-devops-error" >}}) — original DevOps error
- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error-v2" >}}) — host not started
- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error-v2" >}}) — node pool not ready
