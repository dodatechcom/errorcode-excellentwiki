---
title: "Gradle JavaScript Plugin Error"
description: "Gradle JavaScript plugin fails during build due to missing Node.js, npm configuration errors, or incompatible plugin version."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle JavaScript Plugin Error

The Gradle JavaScript plugin or the Node plugin enables building JavaScript projects from Gradle. An error occurs when the plugin cannot find Node.js, npm, or encounters configuration issues.

## Common Causes

- Node.js is not installed or not found on the system PATH
- The node version specified in the plugin does not match what is available
- npm dependencies fail to install due to network issues
- The `nodeDownloadRoot` URL is incorrect or unreachable

## How to Fix

1. Verify Node.js is installed and accessible:

```bash
node --version
npm --version
```

2. Configure the Node plugin to download a specific version:

```groovy
plugins {
    id 'com.github.node-gradle.node' version '7.0.1'
}

node {
    version = '18.19.0'
    npmVersion = '10.2.3'
    download = true
    workDir = file("${projectDir}/.gradle/nodejs")
}
```

3. Set a custom download mirror if the default is slow:

```groovy
node {
    download = true
    distBaseUrl = 'https://npmmirror.com/mirrors/node'
}
```

4. Clean and retry the Node installation:

```bash
rm -rf .gradle/nodejs/
./gradlew npmInstall
```

## Examples

```bash
# Error output
> Failed to setup node.js:
  Unable to download node.js distribution from https://nodejs.org/dist/v18.19.0/
  Could not GET https://nodejs.org/dist/v18.19.0/shasums256.txt
```

```groovy
// Complete Node plugin configuration
node {
    version = '18.19.0'
    npmVersion = '10.2.3'
    download = true
    distBaseUrl = 'https://npmmirror.com/mirrors/node'
    workDir = file("${projectDir}/.gradle/nodejs")
    npmWorkDir = file("${projectDir}/.gradle/npm")
}

task npmBuild(type: NpmTask) {
    args = ['run', 'build']
}
```

## Related Errors

- [Build Script Error]({{< relref "/tools/gradle/gradle-build-script-error" >}}) -- build script compilation issues
- [Process Forking Error]({{< relref "/tools/gradle/gradle-process-forking-error" >}}) -- process execution failures
