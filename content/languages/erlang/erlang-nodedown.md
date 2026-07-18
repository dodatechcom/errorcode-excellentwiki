---
title: "[Solution] Fix nodedown no connection to node in Erlang"
description: "Resolve nodedown errors in Erlang by verifying node names, checking cookie authentication, adjusting net_ticktime settings, and confirming firewall rules."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

A `nodedown` error occurs when an Erlang node cannot establish or maintain a connection to another node. This happens during distributed Erlang operations such as `rpc:call`, `erlang:send`, or monitored processes across nodes.

The error appears as:

```erlang
{badrpc, nodedown}
```

or:

```erlang
** error: {nodedown, 'node@hostname'}
```

## Why It Happens

This error occurs due to distributed node connectivity issues:

- Target node is not running or has been stopped
- Node names or hostnames are incorrect
- Different Erlang cookies between nodes
- Firewall blocking the distribution port (default 4369)
- Network connectivity issues between hosts
- `net_ticktime` timeout exceeded

## How to Fix It

Verify node names and connectivity:

```erlang
%% Check current node name
node().
%% 'my_node@hostname'

%% Check connected nodes
nodes().
%% List of connected node names
```

Ensure matching Erlang cookies:

```erlang
%% Check cookie on both nodes
erlang:get_cookie().

%% Set matching cookie
erlang:set_cookie('my_secret_cookie').

%% Or start nodes with same cookie
%% erl -name node1 -setcookie my_secret_cookie
```

Check node availability before calling:

```erlang
safe_call(Node, Module, Function, Args) ->
    case net_adm:ping(Node) of
        pong ->
            rpc:call(Node, Module, Function, Args);
        pang ->
            {error, {nodedown, Node}}
    end.
```

Verify host resolution:

```bash
%% Check hostname resolution
ping hostname

%% Ensure /etc/hosts or DNS resolves correctly
cat /etc/hosts
```

Adjust net_ticktime for slow networks:

```erlang
%% In sys.config or application config
[{kernel, [{net_ticktime, 60}]}]. %% 60 seconds tick

%% Or change at runtime
net_kernel:set_net_ticktime(60).
```

Check firewall settings:

```bash
%% Allow Erlang distribution port
sudo ufw allow 4369/tcp
%% Or range for distribution
sudo ufw allow 9100:9200/tcp
```

## Common Mistakes

- Using short names (`-sname`) when nodes are on different hosts
- Not ensuring all nodes use the same Erlang cookie
- Forgetting that `net_ticktime` must be configured on all nodes
- Not monitoring node connectivity in production systems
- Assuming `rpc:call` will automatically retry on connection failure
- Mixing `-name` and `-sname` node types in the same cluster

## Related Pages

- [gen_server call timed out](/languages/erlang/erlang-timeout-error)
- [Application start failed](/languages/erlang/erlang-application-failed)
- [Supervisor terminated children](/languages/erlang/erlang-supervisor-restart)
