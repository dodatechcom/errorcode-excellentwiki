---
title: "[Solution] Groovy CLI Error"
description: "Picocli/command-line parsing errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy CLI Error

Picocli/command-line parsing errors.

### Common Causes
Wrong annotation; missing description

### How to Fix
```groovy
import picocli.CommandLine
@CommandLine.Command
class MyApp implements Runnable {
    @CommandLine.Option(names = ['-n', '--name'], required = true)
    String name
    void run() { println "Hello, $name" }
}
CommandLine.execute(new MyApp(), args)
```

### Examples
```groovy
@CommandLine.Command(description = 'My app')
class App implements Runnable {
    @CommandLine.Parameters(index = '0', description = 'Input file')
    File inputFile
    void run() { println inputFile.text }
}
```
