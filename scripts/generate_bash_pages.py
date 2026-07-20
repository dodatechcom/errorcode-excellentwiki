#!/usr/bin/env python3
"""Generate 100+ Bash/Shell scripting error pages."""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "tools", "bash")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CATEGORIES = [
    # ── 1. Syntax errors ──────────────────────────────────────────────
    {
        "category": "Syntax Errors",
        "pages": [
            {
                "slug": "unexpected-eof",
                "title": "Unexpected End of File (EOF)",
                "desc": "Bash script ends unexpectedly with an unexpected EOF error.",
                "body": """\
This error occurs when Bash reaches the end of a file while still expecting more input, typically due to unclosed constructs.

### Common Causes
- Missing closing keyword (`done`, `fi`, `esac`, `}`) for a compound command.
- Unclosed `case` statement or `select` loop.
- Script truncated during transfer or editing.

### How to Fix
```bash
# Verify matching pairs of control structures
grep -n 'if\\|then\\|else\\|fi' script.sh
grep -n 'for\\|while\\|until\\|do\\|done' script.sh

# Use shellcheck to detect unclosed blocks
shellcheck script.sh

# Count opening vs closing keywords
opens=$(grep -cE '^(if|for|while|until|case) ' script.sh)
closes=$(grep -cE '^(done|fi|esac)' script.sh)
echo "Opens: $opens, Closes: $closes"
```

### Example
```bash
# Broken script
#!/bin/bash
for i in 1 2 3; do
    echo "$i"
# missing: done

# Fixed script
#!/bin/bash
for i in 1 2 3; do
    echo "$i"
done
```""",
            },
            {
                "slug": "syntax-error-near-unexpected-token",
                "title": "Syntax Error Near Unexpected Token",
                "desc": "Fix 'syntax error near unexpected token' in Bash scripts.",
                "body": """\
Bash encounters a token it does not expect at the current position in the script.

### Common Causes
- Windows-style line endings (CRLF `\r\n`) in a Unix script.
- Missing semicolons or newlines between statements on the same line.
- Typo in a keyword or use of a reserved word incorrectly.

### How to Fix
```bash
# Convert CRLF to LF
dos2unix script.sh
# Or with sed
sed -i 's/\\r$//' script.sh

# Check for stray characters
cat -A script.sh | head -20

# Run shellcheck for diagnostics
shellcheck script.sh
```

### Example
```bash
# Broken (CRLF)
echo "hello"$'\r'

# Fixed
echo "hello"
```""",
            },
            {
                "slug": "missing-closing-bracket",
                "title": "Missing Closing Bracket `]`",
                "desc": "Resolve 'missing ]' error in Bash test expressions.",
                "body": """\
The `test` or `[` command requires a matching `]` to close the expression.

### Common Causes
- Forgetting the closing `]` in a test expression.
- Spaces around `[` but not around `]`.
- Nested conditions with missing brackets.

### How to Fix
```bash
# Use [[ ]] instead of [ ] (bash-specific, more forgiving)
[[ -f "$file" ]]

# Always ensure spaces around test operators
[ -z "$var" ]

# shellcheck will flag missing brackets
shellcheck script.sh
```

### Example
```bash
# Broken
if [ -f "$file"
then
    echo "exists"
fi

# Fixed
if [ -f "$file" ]; then
    echo "exists"
fi
```""",
            },
            {
                "slug": "missing-done",
                "title": "Missing `done` Keyword",
                "desc": "Bash script error: missing done keyword for loop.",
                "body": """\
Every `for`, `while`, `until`, or `select` loop must end with `done`.

### Common Causes
- Typo in `done` (e.g., `don`).
- `done` placed inside a subshell accidentally.
- Early `return` or `exit` skipping the `done`.

### How to Fix
```bash
# Validate loop structure
grep -c 'do$' script.sh   # should match loop count
grep -c '^done' script.sh  # should match loop count

# Use indent-based linting
shellcheck script.sh
```

### Example
```bash
# Broken
for f in *.txt; do
    cat "$f"

# Fixed
for f in *.txt; do
    cat "$f"
done
```""",
            },
            {
                "slug": "missing-fi",
                "title": "Missing `fi` Keyword",
                "desc": "Resolve missing fi error in Bash if/else statements.",
                "body": """\
Every `if` statement must be closed with `fi`.

### Common Causes
- Unclosed `if` block.
- Mismatched `if`/`then`/`else`/`fi` structure.
- `fi` misspelled or omitted.

### How to Fix
```bash
# Count if/fi pairs
grep -cE '^\s*if ' script.sh
grep -cE '^\s*fi' script.sh

# Use shellcheck
shellcheck script.sh
```

### Example
```bash
# Broken
if [ "$a" = "1" ]; then
    echo "one"

# Fixed
if [ "$a" = "1" ]; then
    echo "one"
fi
```""",
            },
            {
                "slug": "missing-esac",
                "title": "Missing `esac` Keyword",
                "desc": "Fix missing esac in Bash case statements.",
                "body": """\
A `case` statement must end with `esac` (case spelled backwards).

### Common Causes
- Forgetting to close the `case` block.
- Misspelling `esac`.

### How to Fix
```bash
# Validate case/esac pairs
grep -c '^case ' script.sh
grep -c '^esac' script.sh

shellcheck script.sh
```

### Example
```bash
# Broken
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;

# Fixed
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
esac
```""",
            },
            {
                "slug": "missing-double-semicolon",
                "title": "Missing `;;` in Case Statement",
                "desc": "Bash case statement missing double semicolon separator.",
                "body": """\
Each pattern in a `case` statement must end with `;;`.

### Common Causes
- Forgetting `;;` between case patterns.
- Using `;` instead of `;;`.

### How to Fix
```bash
# Ensure every case branch ends with ;;
sed -n '/case/,/esac/p' script.sh

shellcheck script.sh
```

### Example
```bash
# Broken
case "$1" in
    start) echo "starting"
    stop) echo "stopping" ;;

# Fixed
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
esac
```""",
            },
            {
                "slug": "bad-substitution",
                "title": "Bad Substitution Error",
                "desc": "Resolve 'bad substitution' error in Bash variable expansion.",
                "body": """\
The shell cannot parse the variable substitution syntax used.

### Common Causes
- Using `${var/pattern/replacement}` in `sh` instead of `bash`.
- Incorrect brace placement or unbalanced braces.
- Using Bash-specific syntax in a POSIX shell.

### How to Fix
```bash
# Ensure script uses bash shebang
#!/bin/bash

# Use ${var%pattern} not ${var(pattern)}
echo "${filename%.log}"

# Validate syntax
bash -n script.sh
```

### Example
```bash
# Broken (sh mode)
#!/bin/sh
echo "${PATH//:/:\\n}"

# Fixed (bash mode)
#!/bin/bash
echo "${PATH//:/$'\\n'}"
```""",
            },
            {
                "slug": "unterminated-quote",
                "title": "Unterminated Quote Error",
                "desc": "Fix unterminated single or double quote errors in Bash.",
                "body": """\
A quoted string was opened but never closed before the end of the line or file.

### Common Causes
- Missing closing single or double quote.
- Quote spanning multiple lines unintentionally.
- Escaped quotes confusing the parser.

### How to Fix
```bash
# Highlight quotes in editor
grep -n '"' script.sh | head -20
grep -n "'" script.sh | head -20

# Use shellcheck
shellcheck script.sh

# Count quotes (should be even)
grep -o '"' script.sh | wc -l
```

### Example
```bash
# Broken
echo "hello world

# Fixed
echo "hello world"
```""",
            },
            {
                "slug": "unterminated-here-doc",
                "title": "Unterminated Here-Document",
                "desc": "Resolve unterminated here-doc (<<) errors in Bash scripts.",
                "body": """\
A heredoc was opened with `<<` but the closing delimiter was never found.

### Common Causes
- Closing delimiter has leading whitespace when it should not (or vice versa).
- Delimiter is quoted in the opening but not in the closing.
- Missing newline before the closing delimiter.

### How to Fix
```bash
# Ensure closing delimiter is on its own line with no indentation
cat <<EOF
content
EOF

# If using tab-indented heredoc, use <<-
cat <<-EOF
	content
	EOF

shellcheck script.sh
```

### Example
```bash
# Broken
cat <<EOF
hello world
  EOF    # leading whitespace causes error

# Fixed
cat <<EOF
hello world
EOF
```""",
            },
            {
                "slug": "invalid-arithmetic-operator",
                "title": "Invalid Arithmetic Operator",
                "desc": "Fix invalid arithmetic operator in Bash arithmetic expansion.",
                "body": """\
The arithmetic expression contains a token that is not a valid operator.

### Common Causes
- Non-numeric characters in an arithmetic context.
- Octal numbers with `8` or `9`.
- Using Bash arithmetic in a non-arithmetic context.

### How to Fix
```bash
# Validate the expression independently
echo $(( 1 + 2 ))    # valid
echo $(( 08 + 1 ))   # invalid octal

# Use decimal prefix for clarity
echo $(( 010 + 1 ))  # octal 10 + 1 = 9
```

### Example
```bash
# Broken
result=$(( "abc" + 1 ))

# Fixed
result=$(( 0 + 1 ))
```""",
            },
            {
                "slug": "double-parenthesis-error",
                "title": "Double Parenthesis `(( ))` Error",
                "desc": "Resolve errors with Bash double parenthesis arithmetic.",
                "body": """\
The `(( ))` arithmetic command received an invalid expression.

### Common Causes
- Comparison operators `==` used instead of arithmetic `==` inside `(())`.
- Missing operands for an operator.
- Using string operations inside arithmetic context.

### How to Fix
```bash
# Inside (( )), use arithmetic comparison
(( a == b ))    # valid
(( a = b ))     # assignment, not comparison!

# For strings, use [[ ]]
[[ "$a" == "$b" ]]
```

### Example
```bash
# Broken
(( x == ))     # missing right operand

# Fixed
(( x == 0 ))
```""",
            },
            {
                "slug": "invalid-variable-name",
                "title": "Invalid Variable Name",
                "desc": "Fix invalid variable name errors in Bash assignments.",
                "body": """\
Variable names must start with a letter or underscore and contain only alphanumerics and underscores.

### Common Causes
- Variable name starts with a digit.
- Variable name contains hyphens or special characters.
- Spaces around `=` in assignment.

### How to Fix
```bash
# Variable names: [a-zA-Z_][a-zA-Z0-9_]*
my_var=1       # correct
my-var=1       # incorrect
1var=1         # incorrect

# No spaces around =
var="hello"    # correct
var = "hello"  # incorrect (runs command 'var' with args '=' '"hello"')
```

### Example
```bash
# Broken
my-var="test"
123abc="bad"

# Fixed
my_var="test"
_123abc="ok"
```""",
            },
            {
                "slug": "readonly-variable",
                "title": "Assigning to Readonly Variable",
                "desc": "Resolve 'readonly variable' error in Bash scripts.",
                "body": """\
A variable marked `readonly` or with `-r` cannot be reassigned.

### Common Causes
- Reassigning a variable after `readonly` or `declare -r`.
- Modifying a read-only positional parameter.
- Attempting to unset a readonly variable.

### How to Fix
```bash
# Check if variable is readonly
readonly -p varname

# Use a different variable name
readonly CONST="value"
CONST="new"       # error
NEW_CONST="value" # works

# Temporarily disable (not recommended)
unset CONST 2>/dev/null || true
```

### Example
```bash
# Broken
readonly PI=3.14
PI=3.14159  # error: readonly variable

# Fixed
readonly PI=3.14
# Use a new variable for the adjusted value
PI_ADJUSTED=3.14159
```""",
            },
            {
                "slug": "invalid-alias-syntax",
                "title": "Invalid Alias Syntax",
                "desc": "Fix invalid alias syntax errors in Bash.",
                "body": """\
The alias definition has incorrect syntax.

### Common Causes
- Missing `=` or spaces around it.
- Quoting issues in the replacement string.
- Using aliases in non-interactive shells.

### How to Fix
```bash
# Correct syntax: alias name='command'
alias ll='ls -la'

# For complex commands, use a function instead
mycommand() {
    echo "complex command"
}

# Disable alias expansion in scripts
unalias mycommand 2>/dev/null
set +o alias
```

### Example
```bash
# Broken
alias ll = 'ls -la'

# Fixed
alias ll='ls -la'
```""",
            },
        ],
    },
    # ── 2. Permission/Execution errors ────────────────────────────────
    {
        "category": "Permission and Execution Errors",
        "pages": [
            {
                "slug": "permission-denied",
                "title": "Permission Denied Error",
                "desc": "Resolve 'Permission denied' errors when running Bash commands.",
                "body": """\
The current user lacks execute or read permissions for the target file or directory.

### Common Causes
- Script file lacks execute permission.
- Trying to write to a read-only directory or file.
- Insufficient user/group permissions.

### How to Fix
```bash
# Add execute permission to a script
chmod +x script.sh

# Check current permissions
ls -la script.sh

# Change ownership
sudo chown user:group file

# Use sudo if needed (carefully)
sudo command
```

### Example
```bash
# Broken
./deploy.sh    # -rw-r--r-- permissions

# Fixed
chmod +x deploy.sh
./deploy.sh
```""",
            },
            {
                "slug": "command-not-found",
                "title": "Command Not Found Error",
                "desc": "Fix 'command not found' error in Bash shell.",
                "body": """\
Bash cannot locate the command in `PATH` or as a builtin.

### Common Causes
- Command is not installed.
- Program directory not in `PATH`.
- Typo in the command name.
- Script uses a non-standard shell.

### How to Fix
```bash
# Check if command exists
which command_name
type command_name

# Search for package
apt search command_name    # Debian/Ubuntu
yum search command_name    # RHEL/CentOS

# Add directory to PATH
export PATH="/new/path:$PATH"

# Verify PATH
echo "$PATH" | tr ':' '\\n'
```

### Example
```bash
# Broken
myapp --version    # myapp not in PATH

# Fixed
export PATH="$HOME/.local/bin:$PATH"
myapp --version
```""",
            },
            {
                "slug": "no-such-file-or-directory",
                "title": "No Such File or Directory",
                "desc": "Resolve 'No such file or directory' errors in Bash.",
                "body": """\
The file or directory referenced does not exist at the given path.

### Common Causes
- Typo in the file or directory path.
- File has been moved or deleted.
- Symlink target is missing.
- Working directory changed unexpectedly.

### How to Fix
```bash
# Check if file exists before using it
if [[ -f "$filepath" ]]; then
    cat "$filepath"
fi

# Use absolute paths for reliability
source /full/path/to/config.sh

# Check for broken symlinks
ls -la link_name
file link_name
```

### Example
```bash
# Broken
source ./config.sh  # file doesn't exist in cwd

# Fixed
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.sh"
```""",
            },
            {
                "slug": "cannot-execute-binary-file",
                "title": "Cannot Execute Binary File",
                "desc": "Fix 'cannot execute binary file' error in Bash.",
                "body": """\
The file is not a valid executable for the current architecture or is not a script.

### Common Causes
- Trying to run a binary compiled for a different architecture (e.g., ARM on x86).
- File lacks execute permission.
- Script has wrong or missing shebang.

### How to Fix
```bash
# Check file type
file ./mybinary

# Check architecture
uname -m
file ./mybinary | grep -o 'ELF.*'

# Fix shebang
#!/bin/bash    # for scripts
#!/usr/bin/env bash  # portable

# Check for wrong line endings
file -i script.sh
dos2unix script.sh
```

### Example
```bash
# Broken
./myapp  # compiled for ARM, running on x86

# Fixed: recompile for correct architecture
gcc -o myapp myapp.c  # on the correct machine
```""",
            },
            {
                "slug": "exec-format-error",
                "title": "Exec Format Error",
                "desc": "Resolve 'exec format error' when executing scripts or binaries.",
                "body": """\
The kernel cannot determine how to execute the file, usually due to architecture mismatch or missing shebang.

### Common Causes
- Binary compiled for different CPU architecture.
- Script missing `#!` shebang line.
- File is a data file, not executable.

### How to Fix
```bash
# Add shebang to script
#!/bin/bash
# or
#!/usr/bin/env bash

# Check binary architecture
readelf -h ./mybinary | grep Machine

# For cross-architecture binaries, use QEMU
qemu-arm ./arm-binary
```

### Example
```bash
# Broken (missing shebang)
echo "hello"

# Fixed
#!/bin/bash
echo "hello"
```""",
            },
            {
                "slug": "not-a-valid-identifier",
                "title": "Not a Valid Identifier",
                "desc": "Fix 'not a valid identifier' error in Bash variable assignment.",
                "body": """\
The identifier used for a variable, function, or environment variable is not valid.

### Common Causes
- Variable name starts with a number or contains invalid characters.
- Exporting a variable with invalid syntax.
- Sourcing a file with malformed `export` statements.

### How to Fix
```bash
# Valid identifiers: start with letter/underscore
valid_var="ok"
_valid_var="ok"
123var="bad"    # invalid

# Check export syntax
export VAR=value    # correct
export VAR=value    # no spaces around =

# Debug the source file
bash -n sourced_file.sh
```

### Example
```bash
# Broken
export my-var="test"
my-var="test"

# Fixed
export my_var="test"
```""",
            },
            {
                "slug": "fork-failed-retry",
                "title": "Fork Failed / Retry Error",
                "desc": "Resolve 'fork failed, retry' errors in Bash.",
                "body": """\
The system cannot create a new process due to resource exhaustion.

### Common Causes
- Too many processes running.
- Insufficient memory (RAM or swap).
- Process limit hit (`ulimit -u`).

### How to Fix
```bash
# Check process count
ps aux | wc -l

# Check memory
free -h

# Increase process limit
ulimit -u 4096

# Kill zombie/defunct processes
ps aux | awk '$8=="Z" {print $2}' | xargs kill -9

# Check system limits
cat /proc/sys/kernel/pid_max
sysctl kernel.pid_max
```

### Example
```bash
# Broken: spawns too many processes
for i in $(seq 1 10000); do
    sleep 1 &
done

# Fixed: limit concurrency
for i in $(seq 1 10000); do
    sleep 1 &
    (( $(jobs -r | wc -l) >= 50 )) && wait -n
done
```""",
            },
            {
                "slug": "resource-temporarily-unavailable",
                "title": "Resource Temporarily Unavailable",
                "desc": "Fix 'resource temporarily unavailable' (EAGAIN) in Bash.",
                "body": """\
A system resource is temporarily exhausted and the operation would block.

### Common Causes
- Too many open file descriptors.
- Process table full.
- Memory pressure causing OOM conditions.

### How to Fix
```bash
# Check open file descriptors
ls /proc/$$/fd | wc -l

# Increase file descriptor limit
ulimit -n 65536

# Check system-wide limits
cat /proc/sys/fs/file-nr

# Monitor memory
free -h
vmstat 1 5
```

### Example
```bash
# Broken: opens too many files
for f in /tmp/*.log; do
    exec 3< "$f"
done

# Fixed: close file descriptors
for f in /tmp/*.log; do
    exec 3< "$f"
    # process file...
    exec 3<&-
done
```""",
            },
            {
                "slug": "too-many-arguments",
                "title": "Too Many Arguments Error",
                "desc": "Resolve 'too many arguments' error in Bash commands.",
                "body": """\
A command or builtin received more arguments than it can handle.

### Common Causes
- Glob expansion returning too many files.
- Passing unquoted variable with many words.
- Command argument limit reached.

### How to Fix
```bash
# Quote variables to prevent word splitting
echo "$var"      # one argument
echo $var        # may split into many

# Use xargs for large argument lists
find . -name "*.log" -print0 | xargs -0 rm

# Use glob with null delimiter
find . -maxdepth 1 -name "*.txt" -print0 | xargs -0 grep pattern
```

### Example
```bash
# Broken
rm $(find . -name "*.log")    # too many arguments

# Fixed
find . -name "*.log" -print0 | xargs -0 rm
```""",
            },
            {
                "slug": "argument-list-too-long",
                "title": "Argument List Too Long Error",
                "desc": "Fix 'argument list too long' (E2BIG) error in Bash.",
                "body": """\
The total size of arguments and environment exceeds the OS limit (ARG_MAX).

### Common Causes
- Glob `*` expanding to thousands of files.
- Very long string passed as argument.

### How to Fix
```bash
# Use find + xargs instead of glob
find /dir -name "*.txt" | xargs rm

# Use find -exec for safety with special characters
find /dir -name "*.txt" -exec rm {} +

# Check ARG_MAX
getconf ARG_MAX

# Use while loop for batch processing
find /dir -name "*.txt" -print0 | while IFS= read -r -d '' f; do
    rm "$f"
done
```

### Example
```bash
# Broken
rm *.log    # if too many .log files

# Fixed
find . -name "*.log" -exec rm {} +
```""",
            },
        ],
    },
    # ── 3. Variable expansion errors ──────────────────────────────────
    {
        "category": "Variable Expansion Errors",
        "pages": [
            {
                "slug": "unbound-variable",
                "title": "Unbound Variable Error",
                "desc": "Resolve 'unbound variable' errors in Bash with nounset.",
                "body": """\
With `set -u` (nounset), referencing an unset variable causes an error.

### Common Causes
- `set -u` enabled and a variable is not initialized.
- Positional parameter `$1` not provided.
- Environment variable not exported.

### How to Fix
```bash
# Provide default value
echo "${MY_VAR:-default}"

# Check if variable is set
if [[ -v MY_VAR ]]; then
    echo "$MY_VAR"
fi

# For positional parameters
file="${1:?Usage: script.sh <file>}"

# Disable nounset temporarily
set +u
# ... code ...
set -u
```

### Example
```bash
# Broken
set -u
echo "$UNDECLARED_VAR"

# Fixed
set -u
echo "${UNDECLARED_VAR:-fallback}"
```""",
            },
            {
                "slug": "parameter-null-or-not-set",
                "title": "Parameter Null or Not Set",
                "desc": "Fix 'parameter null or not set' error in Bash scripts.",
                "body": """\
The variable is either unset or set to an empty string, and `set -u` is active.

### Common Causes
- Environment variable not set by calling script.
- Missing configuration file.
- `set -u` combined with empty optional variables.

### How to Fix
```bash
# Use default value syntax
echo "${CONFIG_FILE:-/etc/myapp.conf}"

# Use error message syntax
: "${DB_HOST:?DB_HOST must be set}"

# Check before use
if [[ -n "${DB_HOST:-}" ]]; then
    connect "$DB_HOST"
else
    echo "DB_HOST is not set" >&2
    exit 1
fi
```

### Example
```bash
# Broken
set -u
echo "$HOME"  # works
echo "$MISSING"  # error

# Fixed
echo "${MISSING:-/tmp}"
```""",
            },
            {
                "slug": "bad-array-subscript",
                "title": "Bad Array Subscript Error",
                "desc": "Resolve 'bad array subscript' error in Bash arrays.",
                "body": """\
An invalid index was used to access a Bash array element.

### Common Causes
- Array index is negative.
- Index is not an integer.
- Associative array used with numeric index.

### How to Fix
```bash
# Array indices must be >= 0
arr=(a b c)
echo "${arr[0]}"    # valid
echo "${arr[-1]}"   # error in older bash

# Bash 4.3+ supports negative indices
echo "${arr[-1]}"   # 'c' in bash 4.3+

# Validate index
idx=5
if (( idx >= 0 && idx < ${#arr[@]} )); then
    echo "${arr[$idx]}"
fi
```

### Example
```bash
# Broken
arr=(a b c)
echo "${arr[abc]}"

# Fixed
echo "${arr[1]}"
```""",
            },
            {
                "slug": "invalid-subscript",
                "title": "Invalid Subscript Error",
                "desc": "Fix invalid subscript errors when accessing Bash arrays.",
                "body": """\
The subscript used to index an array is syntactically invalid.

### Common Causes
- Using a string where an integer is expected.
- Bash version does not support the subscript syntax.
- Incorrect associative array syntax.

### How to Fix
```bash
# Declare associative arrays properly
declare -A mymap
mymap[key]="value"

# Use integer indices for indexed arrays
declare -a arr
arr[0]="first"

# Check bash version
bash --version
```

### Example
```bash
# Broken
declare -A arr
arr[0]="value"     # wrong for associative

# Fixed
declare -A arr
arr[key]="value"
```""",
            },
            {
                "slug": "indirect-expansion-error",
                "title": "Indirect Expansion Error",
                "desc": "Fix Bash indirect variable expansion (!) errors.",
                "body": """\
Indirect expansion `${!var}` fails when the variable does not contain a valid variable name.

### Common Causes
- `var` contains a value that is not a valid variable name.
- Using `${!var}` on an unset variable.
- Bash version too old for indirect expansion.

### How to Fix
```bash
# Indirect expansion
var=" greeting"
greeting="hello"
echo "${!var}"    # prints 'hello'

# Validate before using
if [[ -n "${!ref:-}" ]]; then
    echo "${!ref}"
fi

# Use eval carefully (security risk)
eval "echo \$$ref"
```

### Example
```bash
# Broken
ref=""
echo "${!ref}"    # empty variable name error

# Fixed
ref="HOME"
echo "${!ref}"    # prints /home/user
```""",
            },
            {
                "slug": "substring-expansion-failed",
                "title": "Substring Expansion Failed",
                "desc": "Resolve substring expansion errors in Bash ${var:offset:length}.",
                "body": """\
The `${var:offset:length}` expansion received invalid parameters.

### Common Causes
- Offset or length is not a valid integer.
- Offset exceeds string length.
- Negative offset in older Bash versions.

### How to Fix
```bash
str="hello world"

# Valid substring extraction
echo "${str:0:5}"     # hello
echo "${str:6}"       # world

# Use arithmetic for variables
offset=6
echo "${str:$offset}"

# Bash 4.2+ supports negative offset
echo "${str: -5}"     # world (note the space)
echo "${str:(-5)}"    # world
```

### Example
```bash
# Broken
str="hello"
echo "${str:abc:3}"   # offset is not a number

# Fixed
echo "${str:0:3}"     # hel
```""",
            },
            {
                "slug": "pattern-matching-error",
                "title": "Pattern Matching Error in Variable Expansion",
                "desc": "Fix pattern matching errors in Bash ${var/pattern/replacement}.",
                "body": """\
The pattern in `${var/pattern/replacement}` has invalid syntax.

### Common Causes
- Unescaped special regex characters in the pattern.
- Using extended regex where basic glob is expected.
- Unbalanced brackets in the pattern.

### How to Fix
```bash
str="hello.world"

# Escape dots and special characters
echo "${str/./_}"       # hello_world

# Use glob patterns, not regex
echo "${str/*.*/match}" # match

# For complex patterns, use sed
echo "$str" | sed 's/\\./-/g'
```

### Example
```bash
# Broken
echo "${str/[a-z]/X}"   # brackets interpreted as glob

# Fixed
echo "${str//./-}"      # hello-world
```""",
            },
            {
                "slug": "nameref-not-found",
                "title": "Nameref Not Found Error",
                "desc": "Resolve 'nameref not found' error in Bash nameref variables.",
                "body": """\
A `nameref` (namered) variable references a variable that does not exist.

### Common Causes
- `declare -n ref=target` where `target` is undefined.
- `target` variable name itself is invalid.
- Using nameref in a subshell where target was local.

### How to Fix
```bash
# Ensure target variable exists
target="hello"
declare -n ref=target
echo "$ref"    # hello

# Check variable existence
if declare -p target &>/dev/null; then
    declare -n ref=target
fi

# Avoid namerefs in subshells
```

### Example
```bash
# Broken
declare -n ref=nonexistent
echo "$ref"    # error

# Fixed
nonexistent="value"
declare -n ref=nonexistent
echo "$ref"    # value
```""",
            },
            {
                "slug": "variable-length-error",
                "title": "Variable Length Expansion Error",
                "desc": "Fix ${#var} string length errors in Bash.",
                "body": """\
The `${#var}` syntax for string length failed.

### Common Causes
- Using `${#array[@]}` incorrectly (should be `${#array[@]}` for count, `${#array[0]}` for first element length).
- Variable name contains invalid characters.
- Bash version incompatibility.

### How to Fix
```bash
str="hello"

# Get string length
echo "${#str}"    # 5

# Get array element count
arr=(a b c)
echo "${#arr[@]}" # 3

# Get specific element length
echo "${#arr[0]}" # 1
```

### Example
```bash
# Broken
echo "${#}"    # no variable specified

# Fixed
var="test"
echo "${#var}" # 4
```""",
            },
            {
                "slug": "uppercase-lowercase-error",
                "title": "Uppercase/Lowercase Transformation Error",
                "desc": "Fix ${var^^} ${var,,} case transformation errors in Bash.",
                "body": """\
Case transformation operators `${var^^}`, `${var,,}`, `${var^}`, `${var,}` failed.

### Common Causes
- Using case transformation in Bash < 4.0.
- Applying to an unset variable.
- Incorrect syntax with count parameter.

### How to Fix
```bash
# Bash 4.0+ required
str="hello"

echo "${str^^}"    # HELLO (all upper)
echo "${str,,}"    # hello (all lower)
echo "${str^}"     # Hello (first upper)
echo "${str,}"     # hello (first lower)

# With count parameter (Bash 4.4+)
echo "${str^^1}"   # Hello (first 1 char upper)

# Fallback for older Bash
echo "$str" | tr '[:lower:]' '[:upper:]'
```

### Example
```bash
# Broken (Bash 3.x)
echo "${str^^}"

# Fixed
echo "$str" | tr '[:lower:]' '[:upper:]'
```""",
            },
        ],
    },
    # ── 4. Globbing/Pathname errors ───────────────────────────────────
    {
        "category": "Globbing and Pathname Errors",
        "pages": [
            {
                "slug": "no-match-for-glob",
                "title": "No Match for Glob Pattern",
                "desc": "Resolve 'no matches found' glob errors in Bash.",
                "body": """\
A glob pattern did not match any files and `failglob` is enabled.

### Common Causes
- `shopt -s failglob` is active.
- Files matching the pattern do not exist.
- Directory context changed unexpectedly.

### How to Fix
```bash
# Check if files exist before globbing
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -gt 0 ]]; then
    process "${files[@]}"
fi

# Disable failglob temporarily
shopt -u failglob

# Use find for complex matching
find . -maxdepth 1 -name "*.txt" -print0 | while IFS= read -r -d '' f; do
    echo "$f"
done
```

### Example
```bash
# Broken
shopt -s failglob
echo *.txt    # error if no .txt files

# Fixed
shopt -s nullglob
for f in *.txt; do
    echo "$f"
done
```""",
            },
            {
                "slug": "ambiguous-redirect",
                "title": "Ambiguous Redirect Error",
                "desc": "Fix 'ambiguous redirect' errors in Bash I/O redirection.",
                "body": """\
A redirection has an ambiguous target, usually due to an empty or multi-word variable.

### Common Causes
- Unquoted variable in redirection target.
- Variable is empty or unset.
- Multiple `>` on the same line.

### How to Fix
```bash
# Quote the redirect target
output="/path/to/file"
cat file > "$output"

# Check variable before redirecting
if [[ -n "${output:-}" ]]; then
    echo "data" > "$output"
fi

# Use a single redirect per line
echo "a" > file1
echo "b" > file2
```

### Example
```bash
# Broken
output=""
echo "hello" > $output   # ambiguous redirect

# Fixed
output="/tmp/out.txt"
echo "hello" > "$output"
```""",
            },
            {
                "slug": "cannot-stat-file",
                "title": "Cannot Stat File Error",
                "desc": "Resolve 'cannot stat' errors for files in Bash.",
                "body": """\
The `stat()` system call failed on the given file path.

### Common Causes
- File does not exist.
- Too many levels of symbolic links (loop).
- Permission denied on a parent directory.

### How to Fix
```bash
# Check existence before stat
if [[ -e "$filepath" ]]; then
    stat "$filepath"
fi

# Resolve symlinks
realpath "$filepath"

# Check for symlink loops
readlink -f "$filepath"
```

### Example
```bash
# Broken
stat "$nonexistent_file"

# Fixed
if [[ -f "$file" ]]; then
    stat "$file"
else
    echo "File not found: $file"
fi
```""",
            },
            {
                "slug": "glob-pattern-too-large",
                "title": "Glob Pattern Too Large",
                "desc": "Fix 'argument list too long' from large glob expansions.",
                "body": """\
The glob pattern expands to more files than the argument list limit allows.

### Common Causes
- Too many files matching the pattern.
- Deep directory recursion.
- No `nullglob` or batching.

### How to Fix
```bash
# Use find + xargs instead of direct glob
find . -name "*.txt" -print0 | xargs -0 -n 100 process

# Batch processing with while loop
find . -name "*.log" -print0 | while IFS= read -r -d '' f; do
    process "$f"
done

# Limit glob with extglob
shopt -s extglob
rm -f !(keep_me|and_this).txt
```

### Example
```bash
# Broken
rm *.tmp    # if millions of .tmp files

# Fixed
find . -name "*.tmp" -print0 | xargs -0 rm
```""",
            },
            {
                "slug": "extglob-not-enabled",
                "title": "Extended Globbing Not Enabled",
                "desc": "Enable and fix extended globbing (extglob) errors in Bash.",
                "body": """\
Extended globbing patterns like `+(pattern)` require `extglob` to be enabled.

### Common Causes
- `shopt -s extglob` not called.
- Using extended glob syntax in a non-interactive shell.

### How to Fix
```bash
# Enable extglob
shopt -s extglob

# Use extended patterns
shopt -s extglob
echo *.+(gz|bz2)    # match .gz and .bz2 files

# Disable extglob
shopt -u extglob

# Check status
shopt extglob
```

### Example
```bash
# Broken
echo *.+(log)    # extglob not enabled

# Fixed
shopt -s extglob
echo *.+(log)
```""",
            },
            {
                "slug": "globstar-not-set",
                "title": "Globstar Not Set Error",
                "desc": "Fix globstar (**) recursive glob errors in Bash.",
                "body": """\
The `**` recursive glob requires `shopt -s globstar` to be enabled.

### Common Causes
- `shopt -s globstar` not set.
- Using `**` in a POSIX `sh` shell.
- Bash version < 4.0.

### How to Fix
```bash
# Enable globstar
shopt -s globstar

# Now ** matches all files recursively
for f in **/*.txt; do
    echo "$f"
done

# Alternative: use find
find . -name "*.txt" -type f

# Check status
shopt globstar
```

### Example
```bash
# Broken
for f in **/*.sh; do echo "$f"; done    # no match

# Fixed
shopt -s globstar
for f in **/*.sh; do echo "$f"; done
```""",
            },
            {
                "slug": "nullglob-fail",
                "title": "Nullglob Configuration Error",
                "desc": "Fix nullglob behavior when no files match a glob pattern.",
                "body": """\
With `nullglob` enabled, an unmatched glob expands to nothing instead of the literal pattern.

### Common Causes
- `nullglob` not set when relying on empty expansion.
- Script behavior differs between environments.

### How to Fix
```bash
# Enable nullglob for safe glob handling
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -eq 0 ]]; then
    echo "No .txt files found"
fi

# Use nullglob in loops
shopt -s nullglob
for f in *.log; do
    process "$f"
done

# Disable if you want literal pattern
shopt -u nullglob
```

### Example
```bash
# Broken (no nullglob)
echo *.txt    # prints "*.txt" even if no match

# Fixed
shopt -s nullglob
for f in *.txt; do
    echo "$f"
done
```""",
            },
            {
                "slug": "failglob-enabled",
                "title": "Failglob Enabled Error",
                "desc": "Resolve errors caused by failglob being enabled in Bash.",
                "body": """\
With `shopt -s failglob`, an unmatched glob causes a shell error.

### Common Causes
- `failglob` enabled in scripts where no-match is expected.
- Globbing in a directory without matching files.

### How to Fix
```bash
# Disable failglob
shopt -u failglob

# Or handle the case explicitly
shopt -s failglob
if ! echo *.txt >/dev/null 2>&1; then
    echo "No files matched"
fi

# Check current setting
shopt failglob
```

### Example
```bash
# Broken
shopt -s failglob
echo *.nonexistent    # error

# Fixed
shopt -u failglob
echo *.nonexistent    # prints literal "*.nonexistent"
```""",
            },
            {
                "slug": "dotglob-mismatch",
                "title": "Dotglob Globbing Mismatch",
                "desc": "Fix dotglob behavior when globbing hidden files in Bash.",
                "body": """\
With `dotglob`, the `*` pattern matches files starting with `.` which may cause unexpected behavior.

### Common Causes
- `shopt -s dotglob` causes `.` and `..` to be included.
- Scripts relying on default behavior break when dotglob is enabled.

### How to Fix
```bash
# Enable dotglob to match hidden files
shopt -s dotglob
for f in *; do
    [[ "$f" == "." || "$f" == ".." ]] && continue
    echo "$f"
done

# Disable if you want default behavior
shopt -u dotglob

# Check setting
shopt dotglob
```

### Example
```bash
# Broken (dotglob enabled, includes . and ..)
shopt -s dotglob
rm *    # tries to remove . and ..

# Fixed
shopt -s dotglob
for f in *; do
    [[ "$f" == "." || "$f" == ".." ]] && continue
    rm "$f"
done
```""",
            },
            {
                "slug": "nocaseglob-error",
                "title": "Nocaseglob Pattern Error",
                "desc": "Fix nocaseglob case-insensitive globbing errors in Bash.",
                "body": """\
With `nocaseglob`, pattern matching in globs is case-insensitive.

### Common Causes
- `shopt -s nocaseglob` makes `*.TXT` match `file.txt`.
- Unexpected file matches due to case-insensitive behavior.

### How to Fix
```bash
# Enable case-insensitive globbing
shopt -s nocaseglob
echo *.txt    # matches .TXT, .Txt, .txt

# Disable for case-sensitive matching
shopt -u nocaseglob
echo *.txt    # only matches .txt

# Check status
shopt nocaseglob
```

### Example
```bash
# Broken (nocaseglob on, matches unexpected files)
shopt -s nocaseglob
rm *.txt    # removes .TXT files too

# Fixed
shopt -u nocaseglob
rm *.txt    # only removes .txt
```""",
            },
        ],
    },
    # ── 5. I/O redirection errors ─────────────────────────────────────
    {
        "category": "I/O Redirection Errors",
        "pages": [
            {
                "slug": "cannot-redirect",
                "title": "Cannot Redirect Error",
                "desc": "Fix 'cannot redirect' errors in Bash I/O redirection.",
                "body": """\
A redirection operation failed due to permission or file system issues.

### Common Causes
- Target directory does not exist.
- Permission denied on the target file or directory.
- Read-only file system.

### How to Fix
```bash
# Create directory if needed
mkdir -p /path/to/output

# Check permissions
ls -la /path/to/

# Use tee for debugging
command 2>&1 | tee output.log

# Redirect to /dev/null to suppress
command >/dev/null 2>&1
```

### Example
```bash
# Broken
echo "log" > /nonexistent/dir/log.txt

# Fixed
mkdir -p /nonexistent/dir
echo "log" > /nonexistent/dir/log.txt
```""",
            },
            {
                "slug": "cannot-open-file-for-read",
                "title": "Cannot Open File for Reading",
                "desc": "Resolve 'cannot open file for reading' errors in Bash.",
                "body": """\
The file specified for input redirection or command argument cannot be opened.

### Common Causes
- File does not exist.
- Insufficient read permissions.
- File is actually a directory.
- Too many open files.

### How to Fix
```bash
# Check file existence and type
[[ -f "$file" ]] && [[ -r "$file" ]] && cat "$file"

# Check if it's a directory
[[ -d "$file" ]] && echo "It's a directory"

# Use descriptive error messages
if [[ ! -r "$file" ]]; then
    echo "Cannot read: $file" >&2
    exit 1
fi
```

### Example
```bash
# Broken
while IFS= read -r line; do
    echo "$line"
done < "$missing_file"

# Fixed
if [[ -r "$file" ]]; then
    while IFS= read -r line; do
        echo "$line"
    done < "$file"
fi
```""",
            },
            {
                "slug": "cannot-open-file-for-write",
                "title": "Cannot Open File for Writing",
                "desc": "Fix 'cannot open file for writing' errors in Bash.",
                "body": """\
The output target file cannot be opened for writing.

### Common Causes
- Directory does not exist.
- File permissions are read-only.
- Disk is full.
- File descriptor limit reached.

### How to Fix
```bash
# Check disk space
df -h .

# Ensure directory exists
mkdir -p "$(dirname "$outfile")"

# Use umask for file creation permissions
umask 022

# Check writable
[[ -w "$(dirname "$outfile")" ]] || { echo "Cannot write to directory" >&2; exit 1; }
```

### Example
```bash
# Broken
echo "data" > /readonly/dir/file.txt

# Fixed
mkdir -p /tmp/output
echo "data" > /tmp/output/file.txt
```""",
            },
            {
                "slug": "descriptor-not-found",
                "title": "File Descriptor Not Found",
                "desc": "Resolve 'Bad file descriptor' errors in Bash redirection.",
                "body": """\
A file descriptor referenced in redirection does not exist or was already closed.

### Common Causes
- Using `>&3` without first opening fd 3.
- Closing a file descriptor and then trying to use it.
- Invalid file descriptor number.

### How to Fix
```bash
# Open a file descriptor before using it
exec 3> output.txt
echo "data" >&3
exec 3>&-

# Use valid fd numbers (0-9, or higher with caution)
exec 4< input.txt
read -r line <&4
exec 4<&-

# Check open descriptors
ls -la /proc/$$/fd/
```

### Example
```bash
# Broken
echo "data" >&3    # fd 3 not opened

# Fixed
exec 3> /tmp/output.txt
echo "data" >&3
exec 3>&-
```""",
            },
            {
                "slug": "process-substitution-error",
                "title": "Process Substitution Error",
                "desc": "Fix process substitution <() >() errors in Bash.",
                "body": """\
Process substitution `<()` or `>()` failed or is not supported.

### Common Causes
- Using process substitution in `sh` instead of `bash`.
- `/dev/fd` not available on the system.
- Too many open file descriptors.

### How to Fix
```bash
# Ensure bash shebang
#!/bin/bash

# Check /dev/fd availability
ls /dev/fd

# Use process substitution for diff
diff <(sort file1) <(sort file2)

# Fallback: use temp files
sort file1 > /tmp/sorted1
sort file2 > /tmp/sorted2
diff /tmp/sorted1 /tmp/sorted2
```

### Example
```bash
# Broken (in sh)
diff <(ls) <(ls -a)    # sh doesn't support <()

# Fixed
#!/bin/bash
diff <(ls) <(ls -a)
```""",
            },
            {
                "slug": "heredoc-delimiter-error",
                "title": "Heredoc Delimiter Error",
                "desc": "Fix heredoc delimiter mismatch errors in Bash.",
                "body": """\
The heredoc closing delimiter does not match the opening delimiter.

### Common Causes
- Quoted vs unquoted delimiter mismatch.
- Closing delimiter has extra whitespace.
- Indented heredoc with wrong syntax.

### How to Fix
```bash
# Simple heredoc
cat <<EOF
hello world
EOF

# Quoted delimiter (no variable expansion)
cat <<'EOF'
$HOME is not expanded
EOF

# Indented heredoc (use <<-)
cat <<-EOF
	indented content
	EOF

# Tab-indented closing delimiter must use tabs, not spaces
```

### Example
```bash
# Broken
cat <<EOF
hello
eoF    # wrong case

# Fixed
cat <<EOF
hello
EOF
```""",
            },
            {
                "slug": "here-string-error",
                "title": "Here-String `<<<` Error",
                "desc": "Fix here-string (<<<) errors in Bash.",
                "body": """\
The here-string operator `<<<` is Bash-specific and has syntax requirements.

### Common Causes
- Using `<<<` in `sh` instead of `bash`.
- Missing the string to pass.
- Unquoted string with spaces.

### How to Fix
```bash
# Ensure bash mode
#!/bin/bash

# Pass string to command via here-string
read -r first rest <<< "hello world"
echo "$first"    # hello

# Quote strings with spaces
read -r a b <<< "one two"
echo "$a $b"    # one two

# Use pipe as fallback
echo "hello world" | read -r first rest
```

### Example
```bash
# Broken (in sh)
read -r var <<< "test"

# Fixed
#!/bin/bash
read -r var <<< "test"
```""",
            },
            {
                "slug": "redirection-operator-syntax",
                "title": "Redirection Operator Syntax Error",
                "desc": "Fix redirection operator syntax errors in Bash.",
                "body": """\
A redirection operator is used incorrectly or has malformed syntax.

### Common Causes
- `>>` vs `>` confusion (append vs overwrite).
- Invalid fd combination (e.g., `2>&1>`).
- Missing space around operators.

### How to Fix
```bash
# Append stderr and stdout
command &> file          # bash: both to file
command > file 2>&1      # POSIX: both to file
command >> file 2>&1     # append both

# Redirect specific fd
command 2>/dev/null      # suppress stderr
command 1>/dev/null      # suppress stdout

# Duplicate fd
exec 3>&1               # save stdout to fd 3
```

### Example
```bash
# Broken
command > file &>       # syntax error

# Fixed
command > file 2>&1
```""",
            },
            {
                "slug": "dev-null-usage-error",
                "title": "/dev/null Usage Error",
                "desc": "Fix /dev/null redirection and usage errors in Bash.",
                "body": """\
Incorrect usage of `/dev/null` for output suppression.

### Common Causes
- Missing `2>&1` when suppressing all output.
- Typo in `/dev/null` path.
- Trying to read from `/dev/null` unexpectedly.

### How to Fix
```bash
# Suppress stdout only
command >/dev/null

# Suppress stderr only
command 2>/dev/null

# Suppress both stdout and stderr
command >/dev/null 2>&1
# Or bash shorthand
command &>/dev/null

# Test if /dev/null exists
[[ -c /dev/null ]] || { echo "/dev/null missing!" >&2; exit 1; }
```

### Example
```bash
# Broken
command > /dev/nul 2>&1    # typo

# Fixed
command &>/dev/null
```""",
            },
            {
                "slug": "tee-permission-error",
                "title": "Tee Permission or Usage Error",
                "desc": "Fix tee command errors when writing to files in Bash.",
                "body": """\
The `tee` command fails to write to the specified output file.

### Common Causes
- Output file location is read-only.
- Permission denied on the directory.
- Too many open file descriptors.

### How to Fix
```bash
# Basic tee usage
command | tee output.txt

# Append mode
command | tee -a output.txt

# Suppress tee output to terminal
command | tee output.txt >/dev/null

# Multiple outputs
command | tee file1.txt file2.txt

# Check directory permissions
ls -ld "$(dirname output.txt)"
```

### Example
```bash
# Broken
command | tee /root/output.txt    # permission denied

# Fixed
command | tee "$HOME/output.txt"
```""",
            },
        ],
    },
    # ── 6. Job control errors ─────────────────────────────────────────
    {
        "category": "Job Control Errors",
        "pages": [
            {
                "slug": "job-not-found",
                "title": "Job Not Found Error",
                "desc": "Resolve 'job not found' errors with fg, bg, and jobs in Bash.",
                "body": """\
The job ID or process referenced does not exist in the current session.

### Common Causes
- Job has already completed.
- Job was started in a different subshell.
- Using job ID after the shell session was restarted.

### How to Fix
```bash
# List current jobs
jobs -l

# Bring specific job to foreground
%1        # job number 1
%+        # current job
%-        # previous job

# Check if process is running
ps aux | grep process_name

# Use PID instead of job ID
kill %1    # by job number
kill 1234  # by PID
```

### Example
```bash
# Broken
sleep 100 &
jobs
# job finishes before next command
fg %1     # job not found

# Fixed
sleep 100 &
jobs -l   # see PID
fg %1     # works while job is running
```""",
            },
            {
                "slug": "stopped-job",
                "title": "Stopped Job Warning",
                "desc": "Handle stopped jobs and SIGTSTP in Bash.",
                "body": """\
A background job has been stopped (usually via Ctrl+Z sending SIGTSTP).

### Common Causes
- Interactive program sent to background tried to read stdin.
- SIGTSTP signal sent manually.
- Terminal flow control.

### How to Fix
```bash
# List stopped jobs
jobs -l

# Resume in foreground
fg %1

# Resume in background
bg %1

# Send SIGCONT to specific PID
kill -CONT 1234

# Prevent stopping with nohup
nohup command &
```

### Example
```bash
# Broken
vim &    # stopped: needs terminal

# Fixed
vim      # run in foreground
# Or use nohup for long-running processes
nohup long_task &
```""",
            },
            {
                "slug": "background-process-error",
                "title": "Background Process Error",
                "desc": "Fix background process errors in Bash scripts.",
                "body": """\
A background process failed or reported an error.

### Common Causes
- Process tries to read from terminal in background.
- Process depends on a terminal it cannot access.
- SIGHUP sent when parent shell exits.

### How to Fix
```bash
# Use nohup to prevent hangup
nohup command &

# Redirect all I/O for background processes
command </dev/null >output.log 2>&1 &

# Disown to remove from job table
command &
disown

# Use setsid for completely independent process
setsid command </dev/null >output.log 2>&1
```

### Example
```bash
# Broken
sleep 5 &    # may receive SIGHUP when shell exits

# Fixed
nohup sleep 5 >/dev/null 2>&1 &
disown
```""",
            },
            {
                "slug": "fg-bg-error",
                "title": "fg/bg Job Control Error",
                "desc": "Fix foreground and background job control errors in Bash.",
                "body": """\
The `fg` or `bg` command cannot operate on the specified job.

### Common Causes
- No current job to send to foreground/background.
- Job ID syntax is wrong.
- Job control is disabled in non-interactive shell.

### How to Fix
```bash
# Check job control is enabled
set -m    # enable job control
set +m    # disable job control

# List available jobs
jobs -l

# fg sends job to foreground
fg %1

# bg resumes job in background
bg %1

# Check if interactive
[[ $- == *i* ]] && echo "interactive" || echo "non-interactive"
```

### Example
```bash
# Broken (non-interactive shell)
command &
fg %1    # fg: no job control

# Fixed: ensure interactive shell or use different approach
#!/bin/bash
set -m    # enable job control
command &
fg %1
```""",
            },
            {
                "slug": "disown-error",
                "title": "Disown Error in Bash",
                "desc": "Fix 'disown' job control errors in Bash.",
                "body": """\
The `disown` command failed to remove the job from the job table.

### Common Causes
- Job ID does not exist.
- Job has already completed.
- Using `disown` on a job from a different subshell.

### How to Fix
```bash
# List current jobs
jobs -l

# Disown specific job
command &
disown %1

# Disown all jobs
disown -a

# Disown without sending SIGHUP
disown -h %1

# Use nohup as alternative
nohup command &
```

### Example
```bash
# Broken
command &
# ... time passes, job finishes ...
disown %1    # error: no such job

# Fixed
command &
disown %1    # immediately after backgrounding
```""",
            },
            {
                "slug": "no-job-control",
                "title": "No Job Control in Non-Interactive Shell",
                "desc": "Resolve 'no job control' errors in Bash scripts.",
                "body": """\
Job control features (fg, bg, Ctrl+Z) are disabled in non-interactive shells.

### Common Causes
- Script runs non-interactively (piped or crontab).
- `set +m` was called.
- Running in a subshell.

### How to Fix
```bash
# Enable job control in scripts (may not work everywhere)
set -m

# Check if interactive
if [[ $- == *i* ]]; then
    echo "Interactive: job control available"
else
    echo "Non-interactive: no job control"
fi

# Use process management without job control
command &
PID=$!
wait "$PID"
```

### Example
```bash
# Broken
#!/bin/bash
command &
fg %1    # no job control in script

# Fixed
#!/bin/bash
command &
PID=$!
wait "$PID"
```""",
            },
            {
                "slug": "sigtstp-sent-error",
                "title": "SIGTSTP Signal Sent Error",
                "desc": "Handle SIGTSTP (terminal stop) signal errors in Bash.",
                "body": """\
A process received SIGTSTP (signal 20), typically from Ctrl+Z or `kill -TSTP`.

### Common Causes
- Interactive program run in background.
- Terminal flow control (Ctrl+Z).
- Explicit `kill -TSTP` sent to process.

### How to Fix
```bash
# Send SIGTSTP to a process
kill -TSTP 1234

# Resume the process
kill -CONT 1234

# Prevent SIGTSTP with nohup
nohup command &

# Trap SIGTSTP in a script
trap 'echo "Received SIGTSTP"; sleep 1; kill -CONT $$' TSTP
```

### Example
```bash
# Broken
long_running_process &
kill -TSTP $!    # process stopped, need to resume

# Fixed
long_running_process &
kill -TSTP $!
# later
kill -CONT $!
```""",
            },
            {
                "slug": "wait-pid-not-found",
                "title": "Wait PID Not Found Error",
                "desc": "Resolve 'wait: pid not a child' errors in Bash.",
                "body": """\
The `wait` command is given a PID that is not a child of the current shell.

### Common Causes
- Waiting on a PID from a different shell.
- Process already exited.
- PID was reassigned to a different process.

### How to Fix
```bash
# Wait for specific child process
command &
PID=$!
wait "$PID"
echo "Exit code: $?"

# Wait for all background jobs
wait

# Wait with timeout (Bash 4.3+)
wait -n    # wait for next child to finish
wait -t 10 $PID    # wait up to 10 seconds

# Check if PID is a child
jobs -l
```

### Example
```bash
# Broken
PID=1234    # from different shell
wait "$PID" # error: not a child

# Fixed
command &
PID=$!
wait "$PID" # correct
```""",
            },
            {
                "slug": "kill-signal-invalid",
                "title": "Invalid Kill Signal Error",
                "desc": "Fix 'invalid signal specification' errors with kill in Bash.",
                "body": """\
The signal name or number given to `kill` is not valid.

### Common Causes
- Typo in signal name (e.g., `SIGKIL`).
- Signal number out of range.
- Using signal name in non-interactive context.

### How to Fix
```bash
# List available signals
kill -l

# Common signals
kill -TERM 1234    # graceful shutdown
kill -KILL 1234    # force kill (cannot be trapped)
kill -HUP 1234     # hangup / reload
kill -INT 1234     # interrupt

# Use signal number
kill -15 1234      # SIGTERM
kill -9 1234       # SIGKILL

# Send to process group
kill -- -1234      # all processes in group
```

### Example
```bash
# Broken
kill -SIGKIL 1234    # typo

# Fixed
kill -9 1234         # or
kill -KILL 1234
```""",
            },
            {
                "slug": "sigcont-failed",
                "title": "SIGCONT Signal Failed",
                "desc": "Fix SIGCONT (continue) signal errors in Bash.",
                "body": """\
The SIGCONT signal could not be delivered to the target process.

### Common Causes
- Process does not exist or has exited.
- Process is not stopped.
- Insufficient permissions.

### How to Fix
```bash
# Check if process exists
ps -p 1234

# Check process state
cat /proc/1234/status | grep State

# Send SIGCONT
kill -CONT 1234
# or
kill -SIGCONT 1234

# Resume and wait
kill -CONT 1234 && wait 1234
```

### Example
```bash
# Broken
kill -CONT 99999    # PID doesn't exist

# Fixed
if ps -p 1234 >/dev/null 2>&1; then
    kill -CONT 1234
fi
```""",
            },
        ],
    },
    # ── 7. Function errors ────────────────────────────────────────────
    {
        "category": "Function Errors",
        "pages": [
            {
                "slug": "function-not-found",
                "title": "Function Not Found Error",
                "desc": "Resolve 'function not found' or 'command not found' for functions.",
                "body": """\
Bash cannot locate the function or command being invoked.

### Common Causes
- Function not defined before being called.
- Function defined in a different scope (subshell, sourced file).
- Typo in function name.

### How to Fix
```bash
# Define function before calling it
my_func() {
    echo "hello"
}
my_func

# Check if function exists
declare -f my_func    # prints function definition
type my_func          # shows where it's defined

# Source files containing functions
source ./my_functions.sh

# List all functions
declare -F
```

### Example
```bash
# Broken
my_func
my_func() { echo "hi"; }

# Fixed
my_func() { echo "hi"; }
my_func
```""",
            },
            {
                "slug": "recursive-function-call",
                "title": "Infinite Recursive Function Call",
                "desc": "Fix infinite recursion and stack overflow in Bash functions.",
                "body": """\
A function calls itself without a proper base case, causing stack overflow.

### Common Causes
- Missing or incorrect base/termination condition.
- Function calls itself with same arguments.
- Stack depth exceeded (typically 1000-10000 levels).

### How to Fix
```bash
# Add a base case
fib() {
    local n=$1
    if (( n <= 1 )); then
        echo "$n"
        return
    fi
    echo $(( $(fib $((n-1))) + $(fib $((n-2))) ))
}

# Track recursion depth
recurse() {
    local depth=${2:-0}
    if (( depth > 100 )); then
        echo "Max recursion depth reached" >&2
        return 1
    fi
    recurse "$1" $((depth + 1))
}
```

### Example
```bash
# Broken
countdown() {
    echo $1
    countdown $(( $1 - 1 ))    # never stops
}

# Fixed
countdown() {
    (( $1 <= 0 )) && return
    echo $1
    countdown $(( $1 - 1 ))
}
countdown 5
```""",
            },
            {
                "slug": "readonly-function",
                "title": "Cannot Reassign Readonly Function",
                "desc": "Fix 'readonly function' error in Bash.",
                "body": """\
A function marked as `readonly` cannot be redefined or unset.

### Common Causes
- Function declared with `readonly -f`.
- Attempting to redefine a readonly function.
- Trying to `unset` a readonly function.

### How to Fix
```bash
# Check if function is readonly
readonly -f my_func

# Define readonly function
my_func() { echo "original"; }
readonly -f my_func

# Cannot redefine:
# my_func() { echo "new"; }    # error

# Use a wrapper or variable instead
my_func_wrapper() {
    if [[ -n "${OVERRIDE:-}" ]]; then
        echo "overridden"
    else
        my_func
    fi
}
```

### Example
```bash
# Broken
readonly -f my_func
my_func() { echo "new"; }    # error

# Fixed: use a different name or variable-based dispatch
func_name="original_func"
dispatch() { "$func_name" "$@"; }
```""",
            },
            {
                "slug": "export-function-error",
                "title": "Export Function Error",
                "desc": "Fix 'export -f' function export errors in Bash.",
                "body": """\
The `export -f` command failed to export a function to child processes.

### Common Causes
- Function not defined before export.
- Using `export -f` in non-bash shell.
- Function name contains invalid characters.

### How to Fix
```bash
# Define then export
my_func() {
    echo "hello from child"
}
export -f my_func

# Verify export
export -p | grep my_func

# Run child process
bash -c 'my_func'

# Fallback: source the function file
bash -c 'source functions.sh; my_func'
```

### Example
```bash
# Broken
export -f undefined_func

# Fixed
defined_func() { echo "ok"; }
export -f defined_func
```""",
            },
            {
                "slug": "trap-error",
                "title": "Trap Command Error",
                "desc": "Fix trap signal handler errors in Bash scripts.",
                "body": """\
The `trap` command has invalid syntax or references an invalid signal.

### Common Causes
- Invalid signal name in trap.
- Trap handler has syntax errors.
- Using trap in non-bash shell.

### How to Fix
```bash
# Correct trap syntax
trap 'echo "Caught signal"' INT TERM

# Clean up temp files on exit
cleanup() {
    rm -f /tmp/mytempfile_$$
}
trap cleanup EXIT

# Reset a trap
trap - INT TERM    # remove handlers

# Ignore signal
trap '' INT TERM    # signals are ignored

# List active traps
trap -p
```

### Example
```bash
# Broken
trap 'echo error' INVALID_SIGNAL

# Fixed
trap 'echo "cleaning up"; rm -f "$tmpfile"' EXIT INT TERM
```""",
            },
            {
                "slug": "return-outside-function",
                "title": "Return Outside Function Error",
                "desc": "Fix 'return: can only `return' from a function' error.",
                "body": """\
The `return` statement is used outside of a function definition.

### Common Causes
- `return` used in main script body.
- `return` in a sourced file that runs code outside functions.
- Mixing `return` and `exit`.

### How to Fix
```bash
# Use return inside functions
my_func() {
    if [[ ! -f "$1" ]]; then
        echo "File not found" >&2
        return 1
    fi
    echo "File found"
    return 0
}

# Use exit in main script body
if [[ ! -f "$config" ]]; then
    echo "Missing config" >&2
    exit 1
fi

# Use source for sourced files
# In sourced file, use return
# In main script, use exit
```

### Example
```bash
# Broken
return 1    # at script top level

# Fixed
exit 1      # at script top level
```""",
            },
            {
                "slug": "exit-outside-function",
                "title": "Exit in Subshell Error",
                "desc": "Understand exit vs return in Bash subshells and functions.",
                "body": """\
`exit` in a subshell only exits the subshell, not the parent script.

### Common Causes
- Using `exit` inside `()` expecting to stop the script.
- `exit` in a piped subshell.
- Unexpected subshell creation.

### How to Fix
```bash
# exit in () only exits the subshell
(echo "inside"; exit 1)    # parent continues
echo "parent continues"

# To exit the parent, use a temp file or exit code check
( exit 1 )
if [[ $? -ne 0 ]]; then
    echo "subshell failed"
    exit 1
fi

# For functions, use return (not exit) unless you want to stop everything
my_func() {
    return 1    # returns to caller
}
```

### Example
```bash
# Broken
(exit 1)    # parent doesn't see the exit

# Fixed
if ! (exit 1); then
    echo "subshell failed"
fi
```""",
            },
            {
                "slug": "local-variable-error",
                "title": "Local Variable Scope Error",
                "desc": "Fix 'local: can only be used in a function' error.",
                "body": """\
The `local` keyword is used outside of a function definition.

### Common Causes
- `local` used in main script body.
- `local` in a sourced file that is not inside a function.
- Missing function wrapper.

### How to Fix
```bash
# local only works inside functions
my_func() {
    local var="value"    # scoped to function
    echo "$var"
}

# At script level, don't use local
global_var="value"    # global scope

# Use subshell for local scope at script level
(
    local_var="scoped_to_subshell"
    echo "$local_var"
)
echo "$local_var"    # empty
```

### Example
```bash
# Broken
local myvar="test"    # outside function

# Fixed
my_func() {
    local myvar="test"
    echo "$myvar"
}
my_func
```""",
            },
            {
                "slug": "typeset-error",
                "title": "Typeset Command Error",
                "desc": "Fix typeset declaration errors in Bash scripts.",
                "body": """\
The `typeset` command is used incorrectly or with invalid options.

### Common Causes
- Using `typeset` in `sh` instead of `bash`.
- Invalid option combination.
- `typeset` in a non-function context with `-l` or `-u`.

### How to Fix
```bash
# typeset is equivalent to declare in Bash
typeset -i num=42         # integer
typeset -r CONST="val"    # readonly
typeset -a arr=(1 2 3)    # array
typeset -A map             # associative array

# Use declare for portability
declare -i num=42

# Check typeset availability
type typeset

# Convert typeset to declare if needed
sed -i 's/typeset/declare/g' script.sh
```

### Example
```bash
# Broken
typeset -l upper="HELLO"    # lowercase flag, bash 4.0+

# Fixed
declare -l lower="HELLO"
echo "$lower"    # hello
```""",
            },
            {
                "slug": "unset-function-error",
                "title": "Cannot Unset Function Error",
                "desc": "Fix 'unset: my_func: cannot unset readonly function' error.",
                "body": """\
The function is marked readonly and cannot be unset.

### Common Causes
- Function declared with `readonly -f`.
- Attempting `unset -f` on a readonly function.
- Function defined with `declare -rf`.

### How to Fix
```bash
# Check if function is readonly
readonly -f my_func

# Cannot unset readonly functions
unset -f my_func    # error if readonly

# Alternative: redefine with a wrapper pattern
my_func() {
    if [[ -n "${MY_FUNC_OVERRIDE:-}" ]]; then
        eval "$MY_FUNC_OVERRIDE"
        return
    fi
    echo "original"
}

# Or use a variable-based dispatch
FUNC_TO_CALL="original_impl"
my_func() { "$FUNC_TO_CALL" "$@"; }
```

### Example
```bash
# Broken
readonly -f my_func
unset -f my_func    # error

# Fixed: use override variable pattern
MY_FUNC_OVERRIDE='echo "overridden"'
my_func
```""",
            },
        ],
    },
    # ── 8. Arithmetic errors ──────────────────────────────────────────
    {
        "category": "Arithmetic Errors",
        "pages": [
            {
                "slug": "integer-expression-expected",
                "title": "Integer Expression Expected",
                "desc": "Fix 'integer expression expected' errors in Bash arithmetic.",
                "body": """\
A command expecting an integer received a non-numeric value.

### Common Causes
- Variable contains non-numeric data.
- Missing quotes around variables with possible spaces.
- Comparison operator used on strings.

### How to Fix
```bash
# Validate before arithmetic
if [[ "$var" =~ ^[0-9]+$ ]]; then
    echo $(( var + 1 ))
fi

# Use default value
val=$(( ${var:-0} + 1 ))

# Use [[ ]] for integer comparison
[[ "$a" =~ ^[0-9]+$ ]] && [[ "$b" =~ ^[0-9]+$ ]] && echo $(( a + b ))
```

### Example
```bash
# Broken
var="abc"
echo $(( var + 1 ))    # integer expression expected

# Fixed
var="123"
echo $(( var + 1 ))    # 124
```""",
            },
            {
                "slug": "division-by-zero",
                "title": "Division by Zero Error",
                "desc": "Fix 'division by 0' errors in Bash arithmetic.",
                "body": """\
Arithmetic division or modulo by zero is undefined.

### Common Causes
- Denominator variable is 0 or unset.
- No guard against zero divisor.
- Dynamic calculations producing zero.

### How to Fix
```bash
divisor=0

# Guard against division by zero
if (( divisor != 0 )); then
    result=$(( 100 / divisor ))
else
    echo "Error: division by zero" >&2
    result=0
fi

# Use default value
divisor=${divisor:-1}

# Bash 4.4+ error message: "division by 0"
```

### Example
```bash
# Broken
a=10
b=0
echo $(( a / b ))    # division by 0

# Fixed
if (( b != 0 )); then
    echo $(( a / b ))
fi
```""",
            },
            {
                "slug": "exponent-too-large",
                "title": "Exponent Too Large Error",
                "desc": "Resolve 'exponent too large' errors in Bash arithmetic.",
                "body": """\
The exponent in an arithmetic expression exceeds the supported range.

### Common Causes
- Very large power calculation (e.g., `2**100`).
- Negative exponents (not supported in `(( ))`).

### How to Fix
```bash
# Use bc for large number arithmetic
echo "2^100" | bc

# Use awk for floating point
awk 'BEGIN { print 2^100 }'

# Check bash arithmetic limits
echo $(( 2**62 ))    # ok
echo $(( 2**63 ))    # may overflow on 32-bit

# Use Python for arbitrary precision
python3 -c "print(2**1000)"
```

### Example
```bash
# Broken
echo $(( 2**1000 ))    # too large

# Fixed
echo "2^1000" | bc
```""",
            },
            {
                "slug": "base-out-of-range",
                "title": "Base Out of Range Error",
                "desc": "Fix 'base out of range' errors with Bash arithmetic base conversion.",
                "body": """\
The numeric base used in `16#hex` or `2#bin` syntax is invalid or a digit exceeds the base.

### Common Causes
- Base outside range 2-64.
- Digit exceeds the specified base (e.g., `8#9`).
- Non-numeric characters in the number.

### How to Fix
```bash
# Valid bases: 2-64
echo $(( 16#FF ))    # 255
echo $(( 2#1010 ))   # 10
echo $(( 8#77 ))     # 63

# Invalid: digit exceeds base
# echo $(( 8#99 ))   # error: 9 not valid in octal

# Convert hex to decimal
echo $(( 0x1F ))     # 31

# Convert binary
echo $(( 2#1101 ))   # 13
```

### Example
```bash
# Broken
echo $(( 8#18 ))    # 8 is not valid in octal

# Fixed
echo $(( 8#17 ))    # 15
```""",
            },
            {
                "slug": "numeric-constant-out-of-range",
                "title": "Numeric Constant Out of Range",
                "desc": "Fix numeric overflow errors in Bash arithmetic.",
                "body": """\
A numeric constant exceeds the representable range of Bash integer arithmetic.

### Common Causes
- Number exceeds 64-bit signed integer range.
- Negative numbers used where unsigned expected.

### How to Fix
```bash
# Bash uses 64-bit signed integers on most systems
max_int=$(( 2**63 - 1 ))
echo "$max_int"    # 9223372036854775807

# For larger numbers, use bc
echo "2^100" | bc

# For unsigned behavior, use bit masking
echo $(( -1 & 0xFFFFFFFFFFFFFFFF ))

# Check overflow
result=$(( 9999999999999999999 + 1 ))
# May wrap around to negative
```

### Example
```bash
# Broken
echo $(( 2**63 ))    # overflow on signed 64-bit

# Fixed
echo "2^63" | bc
```""",
            },
            {
                "slug": "let-error",
                "title": "Let Command Arithmetic Error",
                "desc": "Fix let command arithmetic expression errors in Bash.",
                "body": """\
The `let` command received an invalid arithmetic expression.

### Common Causes
- Using `let` with string comparison.
- Missing operands.
- Shell keyword conflicts.

### How to Fix
```bash
# let for arithmetic
let "x = 5 + 3"
echo "$x"    # 8

# Use (( )) instead (preferred)
(( x = 5 + 3 ))

# let returns 1 if result is 0 (false)
let "x = 0"
echo $?    # 1

# Multiple expressions
let "a=1" "b=2" "c=a+b"
echo "$c"    # 3
```

### Example
```bash
# Broken
let "x = "    # missing right side

# Fixed
let "x = 42"
```""",
            },
            {
                "slug": "arithmetic-expression-error",
                "title": "Arithmetic Expression Error",
                "desc": "Fix (( expression )) arithmetic evaluation errors in Bash.",
                "body": """\
The `(( ))` command has an invalid arithmetic expression.

### Common Causes
- Missing operands for operators.
- Using `==` where `=` is needed for assignment.
- Division by zero or invalid operations.

### How to Fix
```bash
# Correct (( )) usage
(( x = 5 + 3 ))    # assignment
(( x == 5 ))        # comparison (returns 0=true, 1=false)

# Use for conditionals
if (( x > 0 )); then
    echo "positive"
fi

# Increment
(( x++ ))
(( ++x ))
```

### Example
```bash
# Broken
(( x = 5 + ))    # incomplete expression

# Fixed
(( x = 5 + 3 ))
```""",
            },
            {
                "slug": "increment-decrement-error",
                "title": "Increment/Decrement Operator Error",
                "desc": "Fix ++ and -- operator errors in Bash arithmetic.",
                "body": """\
The `++` or `--` operators are used incorrectly in Bash arithmetic.

### Common Causes
- Using `++`/`--` outside of `(( ))` or `let`.
- Applying to non-numeric variable.
- Syntax like `$var++` instead of `(( var++ ))`.

### How to Fix
```bash
x=5

# Correct usage inside (( ))
(( x++ ))    # post-increment (x becomes 6)
(( x-- ))    # post-decrement (x becomes 5)
(( ++x ))    # pre-increment
(( --x ))    # pre-decrement

# Store result
(( y = x++ ))
echo "y=$y x=$x"    # y=5 x=6

# Cannot use outside arithmetic context
# x++    # syntax error
```

### Example
```bash
# Broken
x++    # syntax error outside (( ))

# Fixed
(( x++ ))
```""",
            },
            {
                "slug": "bitwise-shift-error",
                "title": "Bitwise Shift Error",
                "desc": "Fix bitwise shift operator errors in Bash arithmetic.",
                "body": """\
The bitwise shift operator `<<` or `>>` has invalid operands or syntax.

### Common Causes
- Shift amount is negative or too large.
- Non-integer operand.
- Confusion with redirection `<<`.

### How to Fix
```bash
# Correct bitwise operations
echo $(( 1 << 3 ))    # 8 (shift left by 3)
echo $(( 16 >> 2 ))   # 4 (shift right by 2)

# Shift amount must be 0-63 for 64-bit
echo $(( 1 << 63 ))   # min int64

# Use with bitmasks
mask=$(( 1 << 5 ))
echo $(( 42 & mask )) # test bit 5

# Parentheses to avoid confusion with heredoc
(( result = 1 << 3 ))
```

### Example
```bash
# Broken
echo $(( 1 << -1 ))    # negative shift

# Fixed
echo $(( 1 << 3 ))     # 8
```""",
            },
            {
                "slug": "arithmetic-overflow",
                "title": "Arithmetic Overflow Error",
                "desc": "Handle integer overflow errors in Bash arithmetic.",
                "body": """\
An arithmetic operation produces a result outside the 64-bit signed integer range.

### Common Causes
- Large number multiplication or exponentiation.
- Unsigned interpretation of negative numbers.
- Incrementing past `2^63 - 1`.

### How to Fix
```bash
# Check for overflow
max=9223372036854775807
echo $(( max + 1 ))    # overflow: wraps to negative

# Use bc for arbitrary precision
echo "9223372036854775807 + 1" | bc

# Use awk
awk 'BEGIN { print 9223372036854775807 + 1 }'

# Use Python for truly large numbers
python3 -c "print(2**63 + 1)"
```

### Example
```bash
# Broken
big=$(( 9223372036854775807 + 1 ))    # wraps to negative

# Fixed
result=$(echo "9223372036854775807 + 1" | bc)
```""",
            },
        ],
    },
    # ── 9. Test/conditional errors ────────────────────────────────────
    {
        "category": "Test and Conditional Errors",
        "pages": [
            {
                "slug": "too-many-arguments",
                "title": "Test Command: Too Many Arguments",
                "desc": "Fix '[: too many arguments' error in Bash test expressions.",
                "body": """\
The `[` or `test` command received more arguments than expected for the operator.

### Common Causes
- Unquoted variable containing spaces.
- Using `[` with `&&` or `||` instead of `-a`/`-o`.
- Empty variable causing argument splitting.

### How to Fix
```bash
# Quote all variables
[[ -f "$file" ]]          # [[ ]] handles spaces automatically
[ -f "$file" ]            # [ ] needs quoting

# Use [[ ]] instead of [ ]
[[ "$a" == "$b" ]]        # [[ ]] is safer

# Use -a and -o inside [ ]
[ -f "$file" -a -r "$file" ]

# Use && and || outside [ ]
[ -f "$file" ] && [ -r "$file" ]
```

### Example
```bash
# Broken
file="my file.txt"
[ -f $file ]    # too many arguments

# Fixed
[ -f "$file" ]
```""",
            },
            {
                "slug": "test-missing-bracket",
                "title": "Test Command: Missing `]`",
                "desc": "Fix '[: missing `]' errors in Bash test expressions.",
                "body": """\
The `[` command requires a matching `]` as the last argument.

### Common Causes
- Forgetting closing `]`.
- Using `]` with wrong spacing.
- Nested test expressions without proper syntax.

### How to Fix
```bash
# Correct [ ] syntax (spaces required)
[ -f "$file" ] && echo "exists"

# Use [[ ]] instead (no closing bracket needed in if-then)
if [[ -f "$file" ]]; then
    echo "exists"
fi

# Correct brace placement
[ -n "$var" ]    # -n tests non-empty string
```

### Example
```bash
# Broken
if [ -f "$file"    # missing ]

# Fixed
if [ -f "$file" ]; then
    echo "exists"
fi
```""",
            },
            {
                "slug": "test-unknown-operator",
                "title": "Test Command: Unknown Operator",
                "desc": "Fix 'test: unknown operator' errors in Bash conditionals.",
                "body": """\
The test command received an operator it does not recognize.

### Common Causes
- Using `==` inside `[ ]` (only valid in `[[ ]]`).
- Typo in operator (e.g., `-efile` instead of `-f`).
- Using Bash-specific operators in POSIX `[ ]`.

### How to Fix
```bash
# Use = for string comparison in [ ]
[ "$a" = "$b" ]

# Use == for string comparison in [[ ]]
[[ "$a" == "$b" ]]

# Valid [ ] operators: -f, -d, -e, -r, -w, -x, -s, -z, -n, =, !=, -eq, -ne, etc.

# Use [[ ]] for regex and pattern matching
[[ "$file" == *.txt ]]
[[ "$var" =~ ^[0-9]+$ ]]
```

### Example
```bash
# Broken
[ "$a" == "$b" ]    # == not valid in [ ]

# Fixed
[ "$a" = "$b" ]
# or
[[ "$a" == "$b" ]]
```""",
            },
            {
                "slug": "equals-vs-double-equals",
                "title": "= vs == in Bash Test Expressions",
                "desc": "Understand the difference between = and == in Bash tests.",
                "body": """\
Using the wrong equality operator in the wrong context causes errors.

### Common Causes
- `==` in `[ ]` (only works in Bash, not POSIX sh).
- `=` in `[[ ]]` (works but `==` is conventional).
- Confusion about string vs regex matching.

### How to Fix
```bash
# POSIX: use = in [ ]
[ "$a" = "$b" ]

# Bash: use == in [[ ]] for string comparison
[[ "$a" == "$b" ]]

# Bash: use == for regex in [[ ]]
[[ "$a" =~ ^[0-9]+$ ]]

# For pattern matching in [[ ]]
[[ "$file" == *.log ]]

# Shorthand
[[ "$a" == "$b" ]] && echo "equal"
```

### Example
```bash
# Portable (POSIX)
[ "$a" = "$b" ]

# Bash-specific
[[ "$a" == "$b" ]]
```""",
            },
            {
                "slug": "integer-vs-string-comparison",
                "title": "Integer vs String Comparison Error",
                "desc": "Fix integer (-eq) vs string (=) comparison errors in Bash.",
                "body": """\
Using the wrong comparison operator for the data type.

### Common Causes
- Using `-eq` on strings containing non-numeric data.
- Using `=` on integers (works but less efficient).
- Mixing numeric and string comparison operators.

### How to Fix
```bash
# Integer comparison
[[ 5 -eq 5 ]]    # true (integer equal)
[[ 5 -gt 3 ]]    # true (greater than)
[[ 5 -lt 10 ]]   # true (less than)

# String comparison
[[ "abc" == "abc" ]]    # true (string equal)
[[ "abc" != "xyz" ]]    # true (string not equal)

# Never do:
# [ "abc" -eq "abc" ]    # error: not an integer
```

### Example
```bash
# Broken
a="hello"
[ "$a" -eq "hello" ]    # error: not an integer

# Fixed
[[ "$a" == "hello" ]]
```""",
            },
            {
                "slug": "file-test-operator-error",
                "title": "File Test Operator Error",
                "desc": "Fix file test operator errors (-f, -d, -e) in Bash.",
                "body": """\
A file test operator received an invalid or missing argument.

### Common Causes
- Variable is empty or unset.
- Path contains special characters.
- File does not exist.

### How to Fix
```bash
# Quote variable in file tests
[[ -f "$file" ]]    # file exists and is regular
[[ -d "$dir" ]]     # directory exists
[[ -e "$path" ]]    # path exists (any type)
[[ -r "$file" ]]    # readable
[[ -w "$file" ]]    # writable
[[ -x "$file" ]]    # executable
[[ -s "$file" ]]    # non-empty file
[[ -L "$file" ]]    # symbolic link

# Always check for empty variable
[[ -n "${file:-}" ]] && [[ -f "$file" ]]
```

### Example
```bash
# Broken
[[ -f $undefined_var ]]    # unbound variable

# Fixed
file="${1:-/etc/hostname}"
[[ -f "$file" ]] && cat "$file"
```""",
            },
            {
                "slug": "deprecated-a-o-operators",
                "title": "Deprecated -a and -o Test Operators",
                "desc": "Replace deprecated -a/-o operators in Bash test expressions.",
                "body": """\
The `-a` (AND) and `-o` (OR) operators inside `[ ]` are deprecated and ambiguous.

### Common Causes
- Using `[ -f file -a -r file ]` instead of modern syntax.
- `-a` and `-o` conflict with file test `-a` (access time).
- POSIX standard discourages their use.

### How to Fix
```bash
# Use && and || outside [ ] or [[ ]]
[[ -f "$file" ]] && [[ -r "$file" ]]    # AND
[[ -f "$file" ]] || [[ -d "$file" ]]    # OR

# Use separate [ ] commands with && and ||
[ -f "$file" ] && [ -r "$file" ]

# For complex conditions, use if/then
if [[ -f "$file" ]] && [[ -r "$file" ]]; then
    echo "readable file"
fi
```

### Example
```bash
# Deprecated
[ -f "$file" -a -r "$file" ]

# Fixed
[[ -f "$file" ]] && [[ -r "$file" ]]
```""",
            },
            {
                "slug": "regex-matching-error",
                "title": "Regex Matching Error in [[ ]]",
                "desc": "Fix regex matching errors with =~ in Bash [[ ]].",
                "body": """\
The `=~` regex operator in `[[ ]]` has an invalid pattern.

### Common Causes
- Unquoted regex pattern (subject to word splitting).
- Invalid regex syntax.
- Using `=~` in `[ ]` instead of `[[ ]]`.

### How to Fix
```bash
# Use =~ inside [[ ]] only
[[ "$var" =~ ^[0-9]+$ ]]    # check if numeric

# Store regex in variable (Bash 3.2+)
re='^[0-9]+$'
[[ "$var" =~ $re ]]

# Capture groups (Bash 3.0+)
if [[ "$var" =~ ([0-9]+)-([0-9]+) ]]; then
    echo "Start: ${BASH_REMATCH[1]}"
    echo "End: ${BASH_REMATCH[2]}"
fi

# Quote the regex pattern in variable
pattern="^[a-z]{3}$"
[[ "$var" =~ $pattern ]]
```

### Example
```bash
# Broken
[[ "$var" =~ "^[0-9]+$" ]]    # quoted pattern treated as literal

# Fixed
[[ "$var" =~ ^[0-9]+$ ]]
```""",
            },
            {
                "slug": "string-null-check-error",
                "title": "String Null/Empty Check Error",
                "desc": "Fix string null and empty check errors in Bash.",
                "body": """\
Incorrect syntax for checking if a string is null or empty.

### Common Causes
- Using `[ -z $var ]` without quotes.
- Mixing `-z` and `-n` logic.
- Confusing unset with empty.

### How to Fix
```bash
# Check if empty string
[[ -z "$var" ]]      # true if empty or unset
[[ -n "$var" ]]      # true if non-empty

# Use parameter expansion
[[ -z "${var:-}" ]]  # true if unset or empty
[[ -n "${var:-}" ]]  # true if set and non-empty

# Quote variables always
[[ -z "$var" ]]      # correct
[[ -z $var ]]        # may fail if var contains spaces
```

### Example
```bash
# Broken
var=""
[ -z $var ]    # error: too many arguments

# Fixed
[ -z "$var" ]
```""",
            },
        ],
    },
    # ── 10. Subshell/exec errors ──────────────────────────────────────
    {
        "category": "Subshell and Exec Errors",
        "pages": [
            {
                "slug": "subshell-not-supported",
                "title": "Subshell Not Supported Error",
                "desc": "Fix subshell ( ) not supported errors in Bash.",
                "body": """\
The subshell syntax `( )` is not supported or behaving unexpectedly.

### Common Causes
- Using `sh` instead of `bash` for advanced subshell features.
- Process substitution vs subshell confusion.
- Nested subshell depth issues.

### How to Fix
```bash
# Ensure bash is being used
#!/bin/bash

# Subshell syntax
( command1; command2 )
echo $?    # exit code of last command in subshell

# Variables set in subshell don't affect parent
(x=1; echo "inside: $x")    # inside: 1
echo "outside: $x"          # outside: (empty)

# Use for isolation
( cd /tmp && ls )
echo "$PWD"    # unchanged
```

### Example
```bash
# Broken (in sh)
#!/bin/sh
(command; exit 1)

# Fixed
#!/bin/bash
(command; exit 1)
```""",
            },
            {
                "slug": "exec-failed",
                "title": "Exec Command Failed",
                "desc": "Fix 'exec failed' errors when replacing shell process.",
                "body": """\
The `exec` command could not replace the current shell process.

### Common Causes
- Binary file does not exist or is not executable.
- Insufficient permissions.
- `exec` fails and shell continues unexpectedly.

### How to Fix
```bash
# Check if command exists before exec
if [[ -x "/path/to/command" ]]; then
    exec /path/to/command "$@"
else
    echo "Command not found" >&2
    exit 1
fi

# exec for fd redirection (no replacement)
exec 3> output.txt
echo "data" >&3
exec 3>&-

# exec to change shell settings
exec bash    # start new bash
exec zsh     # switch to zsh
```

### Example
```bash
# Broken
exec /nonexistent/command    # fails silently

# Fixed
command -v mytool >/dev/null 2>&1 || { echo "mytool not found" >&2; exit 1; }
exec mytool "$@"
```""",
            },
            {
                "slug": "coprocess-error",
                "title": "Coprocess Error in Bash",
                "desc": "Fix coprocess (|&) errors in Bash.",
                "body": """\
The coprocess syntax `|&` or `coproc` failed.

### Common Causes
- Using `|&` in Bash < 4.0.
- `coproc` syntax errors.
- Process not running in background properly.

### How to Fix
```bash
# |& pipes both stdout and stderr (Bash 4.0+)
command1 |& command2
# equivalent to
command1 2>&1 | command2

# Coprocess (Bash 4.0+)
coproc myproc { command; }
echo "data" >&${myproc[1]}
read -r output <&${myproc[0]}

# Fallback for older Bash
command1 2>&1 | command2
```

### Example
```bash
# Broken (Bash 3.x)
ls |& grep error

# Fixed (Bash 3.x)
ls 2>&1 | grep error
```""",
            },
            {
                "slug": "ulimit-error",
                "title": "Ulimit Command Error",
                "desc": "Fix ulimit resource limit errors in Bash.",
                "body": """\
The `ulimit` command failed to set or query resource limits.

### Common Causes
- Trying to set limit higher than allowed maximum.
- Insufficient privileges (non-root).
- Using soft limit higher than hard limit.

### How to Fix
```bash
# Query current limits
ulimit -a

# Check specific limits
ulimit -n    # open files
ulimit -u    # max user processes

# Set limits (within allowed range)
ulimit -n 4096    # increase open files

# Check hard limit (maximum allowed)
ulimit -Hn

# Set in /etc/security/limits.conf (permanent)
# <domain> <type> <item> <value>
# * soft nofile 65536
# * hard nofile 65536
```

### Example
```bash
# Broken
ulimit -n 1000000    # may exceed hard limit

# Fixed
ulimit -Hn           # check hard limit first
ulimit -n 4096       # set within allowed range
```""",
            },
            {
                "slug": "umask-error",
                "title": "Umask Command Error",
                "desc": "Fix umask file creation mask errors in Bash.",
                "body": """\
The `umask` command has an invalid value or fails to set the mask.

### Common Causes
- Octal value is invalid (e.g., `umask 888`).
- Trying to set umask in restricted shell.
- Negative or non-octal values.

### How to Fix
```bash
# Set umask (octal, 0-777)
umask 022     # default: rwxr-xr-x
umask 077     # private: rwx------
umask 002     # group-writable: rwxrwxr-x

# Check current umask
umask
umask -S      # symbolic output

# Calculate permissions
# Files: 666 - umask = final permissions
# Dirs: 777 - umask = final permissions
umask 022
# file: 666 - 022 = 644 (rw-r--r--)
# dir:  777 - 022 = 755 (rwxr-xr-x)
```

### Example
```bash
# Broken
umask 088    # invalid octal digit

# Fixed
umask 022
```""",
            },
            {
                "slug": "source-file-not-found",
                "title": "Source File Not Found Error",
                "desc": "Fix 'source: file not found' errors in Bash.",
                "body": """\
The `source` or `.` command cannot find the file to execute.

### Common Causes
- File path is incorrect.
- File does not exist.
- Working directory changed.
- File is not executable/readable.

### How to Fix
```bash
# Use absolute path
source /full/path/to/config.sh

# Use SCRIPT_DIR for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"

# Check file exists before sourcing
if [[ -f "$file" ]]; then
    source "$file"
else
    echo "Warning: $file not found" >&2
fi

# Use . instead of source for POSIX compatibility
. /path/to/config.sh
```

### Example
```bash
# Broken
source config.sh    # file not in $PWD

# Fixed
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"
```""",
            },
            {
                "slug": "dot-source-error",
                "title": "Dot (.) Source Command Error",
                "desc": "Fix errors when using the dot (.) command to source files.",
                "body": """\
The `.` (dot) command to source a file in the current shell context fails.

### Common Causes
- File not found or not readable.
- Syntax error in the sourced file.
- Sourcing a binary file instead of a shell script.

### How to Fix
```bash
# Correct syntax
. ./config.sh
source ./config.sh    # equivalent in bash

# Check before sourcing
[[ -r "$file" ]] && . "$file"

# Debug the sourced file
bash -n config.sh    # syntax check only

# Source with error handling
if ! . "$file"; then
    echo "Failed to source $file" >&2
fi
```

### Example
```bash
# Broken
. nonexistent.sh    # file not found

# Fixed
if [[ -f "config.sh" ]]; then
    . config.sh
fi
```""",
            },
            {
                "slug": "shopt-not-set",
                "title": "Shell Option (shopt) Not Set Error",
                "desc": "Fix shell option errors with shopt in Bash.",
                "body": """\
A shell option is not available or cannot be set.

### Common Causes
- Option name is incorrect.
- Option is not available in the Bash version.
- Trying to set a read-only option.

### How to Fix
```bash
# Check if option exists
shopt extglob    # prints current value

# Enable option
shopt -s extglob

# Disable option
shopt -u extglob

# List all options
shopt -s    # enabled options
shopt -u    # disabled options
shopt       # all options with status

# Common options
shopt -s nullglob     # empty glob = nothing
shopt -s globstar     # ** = recursive glob
shopt -s nocasematch  # case-insensitive [[ ]]
```

### Example
```bash
# Broken
shopt -s nonexistent_option    # not a valid option

# Fixed
shopt -s nullglob    # valid option
```""",
            },
            {
                "slug": "hash-table-error",
                "title": "Hash Table Error in Bash",
                "desc": "Fix hash table errors with hashed commands in Bash.",
                "body": """\
The Bash command hash table has stale or invalid entries.

### Common Causes
- `hash -r` needed after installing new commands.
- PATH changed but hash table not refreshed.
- Cached command no longer exists.

### How to Fix
```bash
# Check hash table
hash

# Reset hash table
hash -r

# Remove specific entry
hash -d command_name

# Force rehash after installing
hash -r && command_name

# Check if command is found
type command_name
command -v command_name
```

### Example
```bash
# Broken
# Install new command, then try to use it
pip install mytool
mytool --version    # command not found (cached in hash)

# Fixed
pip install mytool
hash -r
mytool --version
```""",
            },
            {
                "slug": "builtin-not-found",
                "title": "Builtin Command Not Found",
                "desc": "Fix 'builtin not found' errors in Bash.",
                "body": """\
A shell builtin command is not recognized, possibly due to shell version or type.

### Common Causes
- Using a Bash builtin in `sh` or `dash`.
- Builtin was removed or renamed in newer Bash versions.
- PATH manipulation hiding builtins.

### How to Fix
```bash
# Check if command is a builtin
type echo
type cd

# Force builtin usage
builtin echo "hello"
builtin cd /path

# Builtin vs external command
command -v echo    # /bin/echo or builtin
enable echo        # ensure builtin is active

# Disable a builtin (then use external)
enable -n echo
echo "hello"    # now uses /bin/echo
```

### Example
```bash
# Broken (in dash/sh)
#!/bin/sh
mapfile -t arr < <(echo "a\\nb")    # mapfile not in sh

# Fixed
#!/bin/bash
mapfile -t arr < <(echo -e "a\\nb")
```""",
            },
        ],
    },
    # ── 11. Pipeline errors ───────────────────────────────────────────
    {
        "category": "Pipeline Errors",
        "pages": [
            {
                "slug": "broken-pipe",
                "title": "Broken Pipe Error (SIGPIPE)",
                "desc": "Fix broken pipe and SIGPIPE errors in Bash.",
                "body": """\
A process in a pipe closed its input before the upstream process finished writing.

### Common Causes
- `head` or `grep` closing pipe early.
- Network pipe disconnection.
- Large data piped to a fast consumer.

### How to Fix
```bash
# Broken pipe is usually harmless
# but causes SIGPIPE in the writing process

# Suppress SIGPIPE
trap '' PIPE
command | head -1

# Use process substitution to avoid pipe
head -1 < <(command)

# Check pipe status
set -o pipefail    # propagate pipeline errors
command | head -1
echo ${PIPESTATUS[@]}    # all pipeline exit codes
```

### Example
```bash
# Broken (writes SIGPIPE)
yes | head -1000000    # yes gets SIGPIPE

# Fixed (normal behavior)
set -o pipefail
yes | head -5
```""",
            },
            {
                "slug": "sigpipe-received",
                "title": "SIGPIPE Signal Received",
                "desc": "Handle SIGPIPE (signal 13) errors in Bash scripts.",
                "body": """\
The process received SIGPIPE, meaning it wrote to a pipe with no reader.

### Common Causes
- Downstream command exited early.
- Piped command failed before upstream finished.
- Script receives SIGPIPE unexpectedly.

### How to Fix
```bash
# Ignore SIGPIPE
trap '' PIPE

# Check for broken pipe in pipeline
set -o pipefail
command1 | command2
echo "command2 exit: ${PIPESTATUS[1]}"

# Use pipefail to detect pipeline failures
set -o pipefail
if command1 | command2; then
    echo "pipeline succeeded"
else
    echo "pipeline failed"
fi
```

### Example
```bash
# Broken (SIGPIPE causes script to exit)
#!/bin/bash
set -e
head -1 < <(yes)    # may get SIGPIPE

# Fixed
trap '' PIPE
head -1 < <(yes)
```""",
            },
            {
                "slug": "lastpipe-not-enabled",
                "title": "Lastpipe Not Enabled",
                "desc": "Enable and fix lastpipe ($pipestatus) errors in Bash.",
                "body": """\
The `lastpipe` option allows the last command in a pipeline to run in the current shell.

### Common Causes
- `shopt -s lastpipe` not enabled.
- Using `$PIPESTATUS` without `pipefail`.
- Last command in pipe runs in subshell by default.

### How to Fix
```bash
# Enable lastpipe
shopt -s lastpipe

# Now the last command runs in current shell
echo "hello" | read -r var
echo "$var"    # hello (with lastpipe)

# Check lastpipe status
shopt lastpipe

# Use process substitution as alternative
read -r var < <(echo "hello")
echo "$var"
```

### Example
```bash
# Broken (var is empty in parent)
echo "hello" | read -r var
echo "$var"    # empty

# Fixed
shopt -s lastpipe
echo "hello" | read -r var
echo "$var"    # hello
```""",
            },
            {
                "slug": "pipefail-not-set",
                "title": "Pipefail Not Set Error",
                "desc": "Enable set -o pipefail to catch pipeline errors.",
                "body": """\
Without `pipefail`, only the exit code of the last command in a pipeline is checked.

### Common Causes
- Early pipeline failures go undetected.
- `set -e` doesn't catch failures in non-final pipeline stages.
- Unexpected behavior with `&&` and pipelines.

### How to Fix
```bash
# Enable pipefail (recommended in all scripts)
set -o pipefail

# Now any pipeline stage failure is caught
false | true
echo $?    # 1 (with pipefail)

# Combine with set -e
set -eo pipefail

# Check all pipeline exit codes
command1 | command2 | command3
echo "${PIPESTATUS[@]}"    # exit codes of all 3 commands
```

### Example
```bash
# Broken (exit code is 0, hiding failure)
false | true | echo "ok"
echo $?    # 0

# Fixed
set -o pipefail
false | true | echo "ok"
echo $?    # 0 (last command succeeded, but check PIPESTATUS)
```""",
            },
            {
                "slug": "process-substitution-posix",
                "title": "Process Substitution Not Available in POSIX",
                "desc": "Fix process substitution errors when using POSIX sh.",
                "body": """\
Process substitution `<()` and `>()` are Bash-specific, not POSIX compliant.

### Common Causes
- Using `#!/bin/sh` which may be `dash` or `ash`.
- Script needs to be portable to other shells.

### How to Fix
```bash
# Use bash shebang
#!/bin/bash

# Or use temp files for POSIX portability
tmpfile=$(mktemp)
command1 > "$tmpfile"
command2 < "$tmpfile"
rm -f "$tmpfile"

# Use named pipes (FIFO)
mkfifo /tmp/mypipe
command1 > /tmp/mypipe &
command2 < /tmp/mypipe
rm -f /tmp/mypipe

# Use eval + here-string for simple cases
eval 'command2 <<< "$(command1)"'
```

### Example
```bash
# Broken (POSIX sh)
#!/bin/sh
diff <(ls dir1) <(ls dir2)

# Fixed
#!/bin/bash
diff <(ls dir1) <(ls dir2)
```""",
            },
            {
                "slug": "named-pipe-error",
                "title": "Named Pipe (FIFO) Error",
                "desc": "Fix named pipe (FIFO) creation and usage errors in Bash.",
                "body": """\
Named pipes (FIFOs) failed to create or communicate properly.

### Common Causes
- FIFO already exists at the path.
- Permission denied on the FIFO path.
- Deadlock when both ends block on open.

### How to Fix
```bash
# Create a named pipe
mkfifo /tmp/mypipe

# Remove existing FIFO before creating
rm -f /tmp/mypipe
mkfifo /tmp/mypipe

# Non-blocking read/write to avoid deadlock
exec 3<>/tmp/mypipe    # open for both read and write
echo "data" >&3
read -r line <&3
exec 3>&-

# Clean up
rm -f /tmp/mypipe
```

### Example
```bash
# Broken (FIFO exists)
mkfifo /tmp/mypipe    # error: File exists

# Fixed
rm -f /tmp/mypipe
mkfifo /tmp/mypipe
```""",
            },
            {
                "slug": "xargs-delimiting-error",
                "title": "Xargs Delimiting and Argument Error",
                "desc": "Fix xargs delimiter and argument handling errors in Bash.",
                "body": """\
The `xargs` command fails to parse input correctly due to whitespace or special characters.

### Common Causes
- Filenames contain spaces, quotes, or newlines.
- Default whitespace delimiter splits filenames incorrectly.
- Maximum argument length exceeded.

### How to Fix
```bash
# Use null delimiter for safe handling
find . -name "*.log" -print0 | xargs -0 rm

# Limit arguments per invocation
find . -name "*.txt" -print0 | xargs -0 -n 10 wc -l

# Use -I for placeholder
find . -name "*.log" -print0 | xargs -0 -I {} mv {} /archive/

# Check xargs behavior
echo "a b c" | xargs -n 1    # one per line
echo "a b c" | xargs -n 2    # two per invocation
```

### Example
```bash
# Broken
find . -name "*.log" | xargs rm    # fails on filenames with spaces

# Fixed
find . -name "*.log" -print0 | xargs -0 rm
```""",
            },
            {
                "slug": "parallel-execution-error",
                "title": "Parallel Execution Error in Bash",
                "desc": "Fix parallel command execution errors in Bash pipelines.",
                "body": """\
Commands run in parallel have race conditions or resource conflicts.

### Common Causes
- Multiple background jobs writing to the same file.
- Shared resource access without locking.
- Too many parallel processes consuming memory.

### How to Fix
```bash
# Use file locking
(
    flock -n 200 || { echo "Locked" >&2; exit 1; }
    echo "data" >> shared_file
) 200>"$lockfile"

# Limit parallelism
for i in $(seq 1 100); do
    process "$i" &
    (( $(jobs -r | wc -l) >= $(nproc) )) && wait -n
done
wait

# Use GNU parallel for robust parallelism
parallel -j 4 process ::: {1..100}
```

### Example
```bash
# Broken (race condition)
for i in {1..100}; do
    echo "$i" >> output.txt &
done

# Fixed
for i in {1..100}; do
    echo "$i" >> output.txt &
done
wait
```""",
            },
        ],
    },
    # ── 12. Debugging/Tracing errors ──────────────────────────────────
    {
        "category": "Debugging and Tracing Errors",
        "pages": [
            {
                "slug": "xtrace-too-verbose",
                "title": "Xtrace (set -x) Too Verbose Output",
                "desc": "Control and reduce verbose xtrace output in Bash.",
                "body": """\
`set -x` produces excessive trace output that is hard to read.

### Common Causes
- `set -x` enabled globally in a complex script.
- No PS4 customization for context.
- Loops generating many trace lines.

### How to Fix
```bash
# Customize PS4 for better trace output
export PS4='+${BASH_SOURCE}:${LINENO}: '

# Enable xtrace only around specific commands
set -x
critical_command
set +x

# Use a function to toggle xtrace
trace_on() { set -x; }
trace_off() { set +x; }

# Log xtrace to a file
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
```

### Example
```bash
# Broken (verbose output)
set -x
for i in $(seq 1 100); do
    echo "$i"
done
set +x

# Fixed (targeted xtrace)
for i in $(seq 1 100); do
    [[ $i -eq 50 ]] && set -x
    echo "$i"
    [[ $i -eq 50 ]] && set +x
done
```""",
            },
            {
                "slug": "verbose-mode-error",
                "title": "Verbose Mode (set -v) Error",
                "desc": "Fix verbose mode output issues in Bash scripts.",
                "body": """\
`set -v` prints each line as it is read, which can be very noisy.

### Common Causes
- `set -v` enabled globally.
- Verbose output interfering with script logic.
- Mixing verbose and xtrace modes.

### How to Fix
```bash
# Enable verbose only for specific sections
set -v
source problem_file.sh
set +v

# Use PS4 to control xtrace instead of verbose
set -x    # shows execution, not reading

# Check current settings
set -o | grep -E 'verbose|xtrace'

# Disable both
set +v +x
```

### Example
```bash
# Broken
set -v
source large_config.sh    # massive output

# Fixed
bash -v large_config.sh > /tmp/verbose.log 2>&1
```""",
            },
            {
                "slug": "noexec-mode-error",
                "title": "Noexec Mode (set -n) Error",
                "desc": "Fix noexec mode and syntax check errors in Bash.",
                "body": """\
`set -n` reads commands without executing them, which can cause unexpected behavior.

### Common Causes
- `set -n` left enabled from debugging.
- Script reads but does not execute commands.
- Subshells inherit noexec mode.

### How to Fix
```bash
# Use for syntax checking only
bash -n script.sh    # check syntax without running

# Enable/disable in script
set -n    # read only
set +n    # resume execution

# Check if noexec is active
set -o | grep noexec

# Use in combination with other options
set -n -v    # read and print each line, no execution
```

### Example
```bash
# Broken (left in script)
set -n    # everything after this is not executed
echo "This never runs"

# Fixed: use bash -n externally
bash -n myscript.sh    # check syntax
```""",
            },
            {
                "slug": "nounset-conflict",
                "title": "Nounset (set -u) Conflict Error",
                "desc": "Fix conflicts with nounset (set -u) in Bash scripts.",
                "body": """\
`set -u` causes errors when accessing unset variables, which can conflict with common patterns.

### Common Causes
- `${var:-default}` not used for optional variables.
- Positional parameters not checked before access.
- Array expansion `"${arr[@]}"` on empty array (Bash < 4.4).

### How to Fix
```bash
# Use default values for optional variables
echo "${MY_VAR:-default_value}"

# Check positional parameters
[[ $# -ge 1 ]] || { echo "Usage: script.sh <arg>" >&2; exit 1; }
file="$1"

# Handle empty arrays safely (Bash 4.4+)
arr=()
if (( ${#arr[@]} > 0 )); then
    echo "${arr[@]}"
fi

# Temporarily disable for known-safe code
set +u
# ... access potentially unset vars ...
set -u
```

### Example
```bash
# Broken
set -u
arr=()
echo "${arr[@]}"    # error: unbound variable

# Fixed
set -u
arr=()
[[ ${#arr[@]} -gt 0 ]] && echo "${arr[@]}"
```""",
            },
            {
                "slug": "functrace-error",
                "title": "Functrace (set -T) Error",
                "desc": "Fix functrace (set -T) and function tracing errors in Bash.",
                "body": """\
`set -T` inherits ERR and DEBUG traps in functions, causing unexpected behavior.

### Common Causes
- `set -T` causes traps to fire in nested functions.
- Performance degradation from trap inheritance.
- Unexpected debug output from library functions.

### How to Fix
```bash
# Enable function tracing
set -T

# Inherit DEBUG trap (see function calls)
trap 'echo "DEBUG: $BASH_COMMAND" >&2' DEBUG

# Disable function tracing
set +T

# Check functrace status
set -o | grep functrace

# Use errtrace for ERR trap inheritance
set -E    # or set -o errtrace
```

### Example
```bash
# Broken (triggers in every function call)
set -T
trap 'echo "debug: $BASH_COMMAND"' DEBUG
func() { :; }    # prints debug for every command in func

# Fixed (targeted tracing)
set -T
trap 'echo "debug: $BASH_COMMAND" >&2' DEBUG
# Only trace specific function
my_debug_func
set +T
```""",
            },
            {
                "slug": "errtrace-error",
                "title": "Errtrace (set -E) Error",
                "desc": "Fix errtrace (set -E) ERR trap inheritance errors.",
                "body": """\
`set -E` (errtrace) causes ERR traps to fire in functions and subshells.

### Common Causes
- ERR trap fires unexpectedly in called functions.
- Subshells inherit ERR trap causing cascading errors.
- Performance impact from trap propagation.

### How to Fix
```bash
# Enable errtrace (ERR trap in functions)
set -E

# ERR trap fires on any command failure
trap 'echo "Error on line $LINENO" >&2' ERR

# Disable errtrace
set +E

# Check status
set -o | grep errtrace

# Combine with errexit
set -eo pipefail -E    # exit on error + trap in functions
```

### Example
```bash
# Broken (ERR trap fires in every function)
set -E
trap 'echo "Error!" >&2' ERR
helper() { false; }
helper    # ERR trap fires

# Fixed
set -E
trap 'echo "Error at $BASH_COMMAND" >&2' ERR
helper() { false; }
# Disable trap in specific functions
trap - ERR
helper
trap 'echo "Error at $BASH_COMMAND" >&2' ERR
```""",
            },
            {
                "slug": "debug-trap-error",
                "title": "DEBUG Trap Error in Bash",
                "desc": "Fix DEBUG trap handler errors in Bash scripts.",
                "body": """\
The DEBUG trap fires before each command and can cause issues if not handled carefully.

### Common Causes
- Trap function has errors causing cascading failures.
- Trap modifies variables used by the current command.
- Infinite recursion from trap calling itself.

### How to Fix
```bash
# Set DEBUG trap
trap 'echo "Line $LINENO: $BASH_COMMAND" >&2' DEBUG

# Use a guard to prevent recursion
__debugging=0
trap '
    if (( __debugging == 0 )); then
        __debugging=1
        echo "Line $LINENO" >&2
        __debugging=0
    fi
' DEBUG

# Disable DEBUG trap
trap - DEBUG

# Check current DEBUG trap
trap -p DEBUG
```

### Example
```bash
# Broken (infinite recursion)
trap 'echo "debug"; false' DEBUG    # false triggers ERR -> more debug

# Fixed
trap 'echo "debug: $BASH_COMMAND" >&2' DEBUG
```""",
            },
            {
                "slug": "return-trap-error",
                "title": "RETURN Trap Error in Bash",
                "desc": "Fix RETURN trap handler errors in Bash functions.",
                "body": """\
The RETURN trap fires when a function or source completes and may have issues.

### Common Causes
- RETURN trap fires in functions that should not be trapped.
- Trap modifies the return value unexpectedly.
- RETURN trap in sourced files fires at script end.

### How to Fix
```bash
# Set RETURN trap in a function
my_func() {
    trap 'echo "Returning from my_func"' RETURN
    # ... function body ...
}

# The trap fires automatically when function exits
my_func

# Remove RETURN trap
trap - RETURN

# Check current RETURN trap
trap -p RETURN

# Use in sourced files
trap 'cleanup_on_return' RETURN
```

### Example
```bash
# Broken (RETURN trap in every function)
trap 'echo "return"' RETURN
func_a() { :; }    # fires trap
func_b() { :; }    # fires trap

# Fixed (trap only in specific function)
func_a() {
    trap 'echo "returning from func_a"' RETURN
    echo "inside func_a"
}
```""",
            },
            {
                "slug": "ps4-format-error",
                "title": "PS4 Format and Xtrace Prompt Error",
                "desc": "Fix PS4 custom xtrace prompt format errors in Bash.",
                "body": """\
The `PS4` variable has invalid format specifiers or is not set correctly.

### Common Causes
- Using undefined `PS4` variable references.
- `PS4` set before sourcing the file it references.
- Invalid escape sequences in PS4.

### How to Fix
```bash
# Common PS4 with file and line number
export PS4='+${BASH_SOURCE[0]:-unknown}:${LINENO}: ${FUNCNAME[0]:-main}: '

# With timestamp
export PS4='+$(date +%T.%N) ${BASH_SOURCE[0]}:${LINENO}: '

# Check current PS4
echo "$PS4"

# Safe PS4 with all defaults
PS4='+${BASH_SOURCE:-?}:${LINENO}:${FUNCNAME:-?}: '

# Enable xtrace with custom PS4
set -x
```

### Example
```bash
# Broken
export PS4='+${nonexistent_var}:${LINENO}: '    # unbound variable

# Fixed
export PS4='+${BASH_SOURCE[0]:-?}:${LINENO}: '
set -x
```""",
            },
            {
                "slug": "bash-xtracefd-error",
                "title": "BASH_XTRACEFD Error in Bash",
                "desc": "Fix BASH_XTRACEFD file descriptor redirection errors.",
                "body": """\
`BASH_XTRACEFD` is used to redirect xtrace output to a file descriptor, but the fd is invalid.

### Common Causes
- File descriptor not opened before setting BASH_XTRACEFD.
- FD number is already in use.
- BASH_XTRACEFD set to invalid value.

### How to Fix
```bash
# Open file descriptor and redirect xtrace
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
# ... commands ...
set +x
exec {fd}>&-

# Reset to default (stderr)
unset BASH_XTRACEFD
set -x

# Check current value
echo "$BASH_XTRACEFD"

# Use a safe pattern
trace_to_file() {
    local fd=$1
    local logfile=$2
    eval "exec {$fd}> $logfile"
    BASH_XTRACEFD=$fd
    set -x
}
```

### Example
```bash
# Broken
BASH_XTRACEFD=99    # fd 99 not open
set -x    # xtrace goes to nowhere

# Fixed
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
# ... commands ...
set +x
exec {fd}>&-
```""",
            },
        ],
    },
]


def slugify(title: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    return (
        title.lower()
        .replace("/", "-")
        .replace("(", "")
        .replace(")", "")
        .replace("'", "")
        .replace('"', "")
        .replace("`", "")
        .replace("$", "")
        .replace("{", "")
        .replace("}", "")
        .replace("#", "")
        .replace("@", "")
        .replace("!", "")
        .replace("|", "-")
        .replace(">", "-")
        .replace("<", "-")
        .replace("&", "-")
        .replace(";", "")
        .replace(",", "")
        .replace(".", "-")
        .replace(" ", "-")
    )


def generate_page(category_name: str, page: dict) -> str:
    """Generate a single markdown page."""
    title = page["title"]
    desc = page["desc"]
    body = page["body"]

    frontmatter = f"""---
title: "[Solution] {title}"
description: "{desc}"
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---
"""
    return f"""{frontmatter}
# [Solution] {title}

{body}
"""


def main():
    count = 0
    for category in CATEGORIES:
        cat_name = category["category"]
        for page in category["pages"]:
            filename = f"{page['slug']}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            content = generate_page(cat_name, page)
            with open(filepath, "w") as f:
                f.write(content)
            count += 1
    print(f"Generated {count} pages in {OUTPUT_DIR}")
    return count


if __name__ == "__main__":
    main()
