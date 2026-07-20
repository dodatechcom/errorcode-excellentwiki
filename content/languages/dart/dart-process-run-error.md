---
title: "[Solution] Dart Process.run Error — exit code, stderr, environment variables"
description: "Fix Dart Process.run and Process.start errors from exit codes, stderr handling, and environment variable issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 135
---

Process errors occur when external processes fail, return non-zero exit codes, or produce unexpected stderr output.

## Common Causes

1. Process not found on the system PATH.
2. Non-zero exit code not being checked.
3. stderr output being ignored.
4. Environment variables not being passed correctly.
5. `Process.start` failing due to permissions.

## How to Fix It

**Solution 1: Run a process and check exit code**

```dart
import 'dart:io';

void main() async {
  ProcessResult result = await Process.run('ls', ['-la']);
  
  print('Exit code: ${result.exitCode}');
  print('stdout: ${result.stdout}');
  
  if (result.exitCode != 0) {
    print('stderr: ${result.stderr}');
  }
}
```

**Solution 2: Handle process not found**

```dart
import 'dart:io';

void main() async {
  try {
    ProcessResult result = await Process.run('nonexistent_command', []);
    print(result.stdout);
  } on ProcessException catch (e) {
    print('Process error: ${e.message}');
    print('Working directory: ${e.directory}');
  }
}
```

**Solution 3: Use Process.start for streaming output**

```dart
import 'dart:io';

void main() async {
  Process process = await Process.start('ping', ['-c', '3', 'localhost']);
  
  process.stdout.transform(SystemEncoding().decoder).listen(
    (data) => print('OUT: $data'),
  );
  
  process.stderr.transform(SystemEncoding().decoder).listen(
    (data) => print('ERR: $data'),
  );
  
  int exitCode = await process.exitCode;
  print('Exit code: $exitCode');
}
```

**Solution 4: Pass environment variables**

```dart
import 'dart:io';

void main() async {
  Map<String, String> env = {
    'MY_VAR': 'hello',
    'PATH': Platform.environment['PATH'],
  };
  
  ProcessResult result = await Process.run(
    'env',
    [],
    environment: env,
  );
  
  print(result.stdout);
}
```

**Solution 5: Set working directory**

```dart
import 'dart:io';

void main() async {
  ProcessResult result = await Process.run(
    'pwd',
    [],
    workingDirectory: '/tmp',
  );
  
  print('Working directory: ${result.stdout.toString().trim()}');
}
```

## Examples

`Process.run` captures all output and waits for the process to complete. `Process.start` gives you streams for real-time output. Always check `exitCode` — a zero exit code indicates success.

## Related Errors

- [Dart IO Socket Error](/languages/dart/dart-io-socket-error/)
- [Dart File Open Error](/languages/dart/dart-file-open-error/)
- [Dart IO Encoding Error](/languages/dart/dart-io-encoding-error/)
