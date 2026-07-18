---
title: "[Solution] Julia ProcessFailedException — External Command Failed"
description: "Fix Julia ProcessFailedException when running external commands. Learn about pipeline, success, and proper command error handling."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `ProcessFailedException` is thrown when an external command run with `run`, `success`, or `pipeline` exits with a non-zero status code. The exception contains the process exit status and any output that was captured.

## Why It Happens

The most common cause is running a command that does not exist on the system. For example, `run(pipeline(`nonexistent_command`, stdout=devnull))` fails because the command cannot be found.

Another frequent cause is a command that fails due to invalid arguments. If the command is valid but the arguments are wrong, it exits with a non-zero status code, causing this exception.

File not found errors when the command requires input files are common. For example, running `grep "pattern" nonexistent_file.txt` fails because the input file does not exist.

Permission errors occur when the command is not executable by the current user. This is common with scripts that do not have the execute permission set.

Network commands that fail due to connectivity issues (like `curl` or `wget` with unreachable URLs) also cause this exception.

## How to Fix It

### Use success instead of run for boolean checking

```julia
# Wrong — throws ProcessFailedException
run(pipeline(`ls nonexistent_dir`, stdout=devnull))

# Correct — returns false instead of throwing
if success(pipeline(`ls my_dir`, stdout=devnull))
    println("Directory exists")
else
    println("Directory not found")
end
```

### Capture and inspect the error

```julia
try
    run(pipeline(`my_command`, stdout=devnull))
catch e
    if e isa ProcessFailedException
        println("Command failed with status: $(e.process.exitcode)")
    else
        rethrow()
    end
end
```

### Check if command exists before running

```julia
function safe_run(cmd)
    if success(pipeline(`which $cmd`, stdout=devnull, stderr=devnull))
        run(cmd)
    else
        println("Command not found: $cmd")
    end
end
```

### Use pipeline with error redirection

```julia
# Redirect stderr to suppress error output
run(pipeline(`my_command`, stdout=devnull, stderr=devnull))
```

### Use Cmd objects for complex commands

```julia
cmd = `git status --porcelain`
if success(cmd)
    output = read(cmd, String)
    process_git_status(output)
end
```

## Common Mistakes

- Not checking if a command exists before trying to run it
- Using `run` when `success` would be more appropriate
- Not capturing stderr for debugging failed commands
- Assuming commands available on one OS are available on another
- Not handling the exit code properly when it matters

## Related Pages

- [Julia SystemError](/languages/julia/julia-system-error/)
- [Julia ErrorException](/languages/julia/julia-error-exception/)
- [Julia RemoteException](/languages/julia/julia-remote-error/)
