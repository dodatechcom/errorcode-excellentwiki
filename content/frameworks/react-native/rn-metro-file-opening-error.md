---
title: "[Solution] React Native Metro File Opening Error"
description: "react-native Metro bundler throws EMFILE or too many open files error on macOS or Linux during React Native development"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Metro file opening error occurs when the operating system's per-process file descriptor limit is reached. Metro opens many files for module resolution, source maps, and caching. When combined with other tools like ESLint and TypeScript server, the system runs out of file handles.

## Common Causes

- macOS default ulimit is set to 256 per process, which is insufficient for large projects
- ESLint running alongside Metro and Watchman, all consuming file descriptors
- Node.js process file descriptor limit is too low (default 1024)
- Antivirus or cloud sync software holding file handles open
- A file watcher or hot module replacement leaking open file handles

## How to Fix

1. Increase file descriptor limit temporarily:

```bash
ulimit -n 4096
```

2. Make it permanent in shell config:

```bash
# ~/.zshrc or ~/.bashrc
ulimit -n 10000
```

3. Configure the system limit on macOS:

```bash
# /etc/sysctl.conf
kern.maxfiles=50000
kern.maxfilesperproc=45000
```

4. Reduce Metro workers processing:

```bash
npx react-native start --max-workers 2
```

## Examples

```bash
# Error: EMFILE: too many open files
# Fix: increase limit before starting metro
ulimit -n 4096
npx react-native start
```

## Related Errors

- [Metro Bundler Failed]({{< relref "/frameworks/react-native/rn-metro-bundler-failed" >}})
- [Bundler Error]({{< relref "/frameworks/react-native/rn-bundler-error" >}})
