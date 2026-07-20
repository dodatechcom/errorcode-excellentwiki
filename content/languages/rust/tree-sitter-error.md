---
title: "[Solution] tree-sitter Parse Error Fix"
description: "Fix tree-sitter parse errors. Handle grammar loading, node traversal, and error recovery."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# tree-sitter Parse Error

The `tree-sitter` crate provides incremental parsing for source code using grammar files. Errors occur when the grammar is not loaded correctly, when the input contains syntax the grammar doesn't recognise, or when tree-sitter is used without compiling the grammar via a `build.rs` script. The parser returns a `tree_sitter::Tree` with a `root_node()` that may contain `has_error()` nodes.

## Common Causes

```rust
use tree_sitter::{Parser, Language};

// 1. Grammar not loaded — parser has no language
let mut parser = Parser::new();
// parser.set_language(language) never called
let tree = parser.parse("fn main() {}", None);
// tree.root_node().has_error() == true

// 2. Grammar compiled from wrong source
// build.rs must call tree_sitter_cli::generate::generate_parser_for_grammar()

// 3. Input exceeds parser's internal buffer for large files
// For files > 32KB, incremental parsing may be needed

// 4. Using wrong grammar for the language
// e.g., parsing Rust with a JavaScript grammar
```

## How to Fix

1. **Set up the grammar correctly in build.rs**

```rust
// build.rs
fn main() {
    let src_dir = std::path::Path::new("vendor/tree-sitter-rust");

    println!("cargo:rerun-if-changed={}", src_dir.join("src/parser.c").display());
    println!("cargo:rerun-if-changed={}", src_dir.join("src/scanner.c").display());

    cc::Build::new()
        .include(&src_dir)
        .file(src_dir.join("src/parser.c"))
        .file(src_dir.join("src/scanner.c"))
        .compile("tree-sitter-rust");
}
```

2. **Check for parse errors after parsing**

```rust
use tree_sitter::{Parser, Node};

fn parse_and_check(source: &str) -> Result<Node, String> {
    let mut parser = Parser::new();
    parser.set_language(&tree_sitter_rust::language())
        .map_err(|e| format!("Failed to set language: {}", e))?;

    let tree = parser.parse(source, None).ok_or("Parse returned None")?;
    let root = tree.root_node();

    if root.has_error() {
        // Walk the tree to find error nodes
        let mut cursor = root.walk();
        let mut errors = Vec::new();
        loop {
            let node = cursor.node();
            if node.is_error() || node.is_missing() {
                errors.push(format!(
                    "Error at {}:{}: {}",
                    node.start_position().row + 1,
                    node.start_position().column + 1,
                    node.to_sexp()
                ));
            }
            if !cursor.goto_next_sibling() {
                break;
            }
        }
        Err(errors.join("\n"))
    } else {
        Ok(root)
    }
}
```

3. **Use incremental parsing for large files**

```rust
use tree_sitter::Parser;

let mut parser = Parser::new();
parser.set_language(&tree_sitter_rust::language()).unwrap();

// Parse in chunks for large files
let mut current_tree = None;
let chunks = vec!["fn main() {", "\n    println!(\"hello\");", "\n}"];

for chunk in chunks {
    current_tree = parser.parse(chunk, current_tree.as_ref());
}

let tree = current_tree.unwrap();
println!("Root: {}", tree.root_node().kind()); // "source_file"
```

4. **Use query patterns for structured extraction**

```rust
use tree_sitter::{Parser, Query, QueryCursor};

let mut parser = Parser::new();
parser.set_language(&tree_sitter_rust::language()).unwrap();
let tree = parser.parse("fn add(a: i32, b: i32) -> i32 { a + b }", None).unwrap();

let query = Query::new(
    &tree_sitter_rust::language(),
    "(function_item name: (identifier) @fn-name)"
).unwrap();

let mut cursor = QueryCursor::new();
for match_ in cursor.matches(&query, tree.root_node(), source.as_bytes()) {
    for capture in match_.captures {
        println!("Found: {}", capture.node.text());
    }
}
```

## Examples

```rust
use tree_sitter::Parser;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut parser = Parser::new();
    parser.set_language(&tree_sitter_rust::language())?;

    let source = r#"
        fn main() {
            let x = 42;
            let y = x + 1;
            println!("{}", y);
        }
    "#;

    let tree = parser.parse(source, None).unwrap();
    let root = tree.root_node();

    println!("Root kind: {}", root.kind());
    println!("Has errors: {}", root.has_error());
    println!("Child count: {}", root.child_count());

    for i in 0..root.child_count() {
        let child = root.child(i).unwrap();
        println!("  Child {}: {} ({})",
            i,
            child.kind(),
            &source[child.start_byte()..child.end_byte()]
        );
    }

    Ok(())
}
```

## Related Errors

- [Syntex Error]({{< relref "/languages/rust/syntex-error" >}}) — deprecated syntax extension
- [Regex Error]({{< relref "/languages/rust/regex-error" >}}) — pattern matching
- [Regex Error v2]({{< relref "/languages/rust/regex-error-v2" >}}) — regex v2
