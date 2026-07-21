---
title: "[Solution] Vagrant Trigger Error"
description: "Fix Vagrant trigger errors when pre/post action triggers fail to execute."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vagrant Trigger Error

Vagrant triggers fail to execute before or after VM actions.

```
Error executing trigger: undefined method 'run'
```

## Common Causes

- Trigger syntax incorrect
- Shell command not found in trigger context
- Trigger runs in wrong directory
- Error in trigger script not handled
- Trigger depends on VM state

## How to Fix

### Basic Trigger Syntax

```ruby
Vagrant.configure("2") do |config|
  config.trigger.before :up do
    puts "Starting VM..."
  end
  
  config.trigger.after :halt do
    puts "VM stopped"
  end
end
```

### Run Shell Commands

```ruby
config.trigger.after :up, type: :shell do
  run "echo 'VM is ready'"
  run_remote "echo 'Connected to VM'"
end
```

### Handle Trigger Errors

```ruby
config.trigger.after :provision do
  begin
    run "echo 'Provision complete'"
  rescue => e
    puts "Trigger error: #{e.message}"
  end
end
```

### Use Trigger with Conditions

```ruby
config.trigger.after :up do |trigger|
  trigger.info = "Running setup..."
  trigger.run = { inline: "echo 'Setup complete'" }
end
```

### Available Trigger Events

```ruby
# :up, :halt, :destroy, :reload, :provision, :ssh, :validate_config
```

## Examples

```ruby
# Complete trigger setup
Vagrant.configure("2") do |config|
  config.trigger.before :up do
    run "docker-machine ls"
  end
  
  config.trigger.after :up do
    run "echo 'VM ready at $(date)'"
  end
  
  config.trigger.after :destroy do
    run "echo 'VM destroyed'"
  end
end
```
