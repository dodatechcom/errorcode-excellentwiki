---
title: "Solved JavaScript semantic-release Error — How to Fix"
date: 2026-03-20T17:55:20+00:00
description: "Learn how to resolve JavaScript semantic-release versioning and publishing errors."
categories: ["javascript"]
keywords: ["semantic-release error", "versioning", "npm publish", "release automation", "changelog"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

semantic-release errors occur when commit history doesn't trigger releases, plugin configuration is wrong, or npm authentication fails. The tool automates version publishing.

Common causes include:
- No release-worthy commits
- Invalid plugin configuration
- npm authentication missing
- Branch not configured
- Git permissions issues

## Common Error Messages

```
Error: No release found
```

```
Error: ENOENT: no such file or directory, open 'package.json'
```

```
Error: Cannot publish over previously published version
```

## How to Fix It

### 1. Configure semantic-release

Set up release automation.

```javascript
// release.config.js
export default {
  branches: ["main"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    [
      "@semantic-release/git",
      {
        assets: ["package.json", "CHANGELOG.md"],
        message: "chore(release): ${nextRelease.version} [skip ci]"
      }
    ],
    "@semantic-release/github"
  ]
};
```

### 2. Write Release Commits

Follow conventional commits.

```bash
# Triggers minor release (0.1.0 → 0.2.0)
git commit -m "feat: add user authentication"

# Triggers patch release (0.1.0 → 0.1.1)
git commit -m "fix: resolve login timeout"

# Triggers major release (0.1.0 → 1.0.0)
git commit -m "feat(api)!: change authentication

BREAKING CHANGE: API now requires OAuth2"

# No release triggered
git commit -m "chore: update dependencies"
git commit -m "docs: update README"
```

### 3. CI Integration

Automate releases in CI:

```yaml
# .github/workflows/release.yml
name: Release
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build
      - run: npx semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

## Common Scenarios

### Scenario 1: Dry Run

Test release without publishing:

```bash
npx semantic-release --dry-run
```

### Scenario 2: Skip Release

Skip specific commits:

```bash
git commit -m "docs: update README [skip release]"
```

## Prevent It

- Use conventional commits for automatic versioning
- Configure `branches` to control release triggers
- Set up `GITHUB_TOKEN` and `NPM_TOKEN` in CI
- Use `--dry-run` to test before production
- Add `[skip ci]` to release commit messages