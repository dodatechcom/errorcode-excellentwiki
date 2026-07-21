---
title: "[Solution] Vagrant Config Parse Error"
description: "Fix Vagrant config parse errors when the Vagrantfile contains invalid Ruby syntax."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Config Parse Error

A Vagrant config parse error occurs when the Vagrantfile contains invalid Ruby syntax that cannot be parsed.

## Why This Happens

- Missing end keyword
- Unclosed string or block
- Incorrect Ruby syntax
- Invalid variable reference
- Missing comma in hash

## Common Error Messages

- `vagrant_config_parse_error`
- `vagrant_vagrantfile_syntax_error`
- `vagrant_ruby_syntax_error`
- `vagrant_config_invalid`

## How to Fix It

### Solution 1: Check Ruby Syntax

Validate the Vagrantfile syntax:

```bash
ruby -c Vagrantfile
```

### Solution 2: Fix Common Syntax Errors

Ensure proper block closure:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
```

### Solution 3: Check Variable References

Ensure variables are properly referenced:

```ruby
# Correct
box_name = "ubuntu/focal64"
config.vm.box = box_name

# Incorrect
config.vm.box = $box_name  # Avoid global variables
```

### Solution 4: Use a Linter

Install a Ruby linter to catch syntax errors:

```bash
gem install rubocop
rubocop Vagrantfile
```

## Common Scenarios

- **Missing end keyword:** Count do/end blocks carefully
- **Unclosed strings:** Check all string delimiters
- **Invalid hash syntax:** Use proper Ruby hash syntax

## Prevent It

- Use an editor with Ruby syntax highlighting
- Run syntax validation before vagrant commands
- Keep Vagrantfile simple and well-formatted
