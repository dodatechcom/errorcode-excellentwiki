---
title: "Can't Find Action"
description: "GitHub Actions cannot find the referenced action, either by name or in the specified repository."
tools: ["github-actions"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means the `uses` directive in a workflow step cannot resolve the specified action. The action name, version, or repository path is incorrect or unavailable.

## Common Causes

- The action reference is misspelled (wrong owner, repo, or action name)
- The specified version tag or commit SHA does not exist
- A private action requires authentication that is not configured
- The action was removed or renamed by its maintainer

## How to Fix

Verify the action exists on GitHub and check the correct reference format:

```yaml
- uses: actions/checkout@v4
```

The correct format is `owner/repo@ref`. Check available versions:

```bash
# Browse https://github.com/actions/checkout/tags
```

If using a local action, ensure the path is correct:

```yaml
- uses: ./.github/actions/my-action
```

For private actions, configure a `GITHUB_TOKEN` with appropriate permissions:

```yaml
- uses: private-org/private-action@v1
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
```

## Examples

```
Error: Can't find action 'actions/chekout@v4'. Unable to resolve action
`actions/chekout@v4`, unable to find version `v4`
```

## Related Errors

- [Workflow Failed]({{< relref "/tools/github-actions/workflow-failed" >}})
