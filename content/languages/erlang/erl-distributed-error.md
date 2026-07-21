---
title: "Erlang distributed node connection error"
description: "Fix Erlang distributed node connection failures when net_kernel cannot establish connections between nodes."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Distributed node connection errors occur when two Erlang nodes cannot communicate. The `net_kernel` module manages connections, and failures result from cookie mismatches, network issues, or incorrect node naming.

## Common Causes

- Different Erlang cookies on connecting nodes
- Node names use different hostnames (short name vs long name)
- Firewall blocking the distributed Erlang port range
- DNS cannot resolve the hostname of the remote node
- Erlang distribution protocol version mismatch between nodes

## How to Fix

```erlang
%% WRONG: Different cookies on each node
%% Node A: erl -name a@host1 -setcookie secret1
%% Node B: erl -name b@host2 -setcookie secret2
net_adm:ping('b@host2').  %% pang -- connection refused

%% CORRECT: Same cookie on all nodes
%% Both nodes: erl -name a@host1 -setcookie mycookie
net_adm:ping('b@host2').  %% pong
```

```enrl
%% WRONG: Mixing short and long names
%% Node A: erl -name a@host1
%% Node B: erl -sname b
net_adm:ping('b@host1').  %% naming mismatch

%% CORRECT: Use consistent naming
%% Both: erl -name a@host1 -name b@host1
```

## Examples

```erlang
%% Example 1: Check node connectivity
pong = net_adm:ping('remote@host.example.com').

%% Example 2: Get connected nodes
Nodes = nodes().  %% returns list of connected node names

%% Example 3: Set cookie at runtime
erlang:set_cookie('mysecretcookie').
```

## Related Errors

- [Node down error](erlang-nodedown) -- node disconnects during operation
- [TCP error](erl-tcp-error) -- lower-level network failures
