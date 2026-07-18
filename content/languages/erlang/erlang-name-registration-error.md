---
title: "[Solution] Erlang Name Already Registered Error"
description: "Fix Erlang name already registered error when starting named processes. Resolve global or local name conflicts."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `name already registered` error occurs when attempting to start a process with a name that is already in use by another process. Both local and global name registries enforce uniqueness, so only one process can hold a given name at any time.

## Why It Happens

- Previous process with same name is still alive: The old process has not yet terminated.
- Restart attempt without proper cleanup of old process: The supervisor restarts before the old process fully exits.
- Global registry conflict across distributed nodes: Two nodes try to register the same global name.
- Supervisor restarting process before old one fully terminated: Race condition during process restart.
- Manual process creation with duplicate registered name: Calling `register/2` with a name already in use.

## How to Fix It

Check if the name is already registered before starting:

```erlang
case whereis(my_server) of
    undefined -> {ok, Pid} = my_server:start();
    Pid -> io:format("Server already running at ~p~n", [Pid])
end.
```

Use gen_server start_link with proper supervision. Let the supervisor handle name uniqueness:

```erlang
{ok, Pid} = supervisor:start_child(MySupervisor, #{
    id => my_server,
    start => {my_server, start_link, []},
    restart => transient,
    type => worker
}).
```

Unregister old process before registering new one in init:

```erlang
init([]) ->
    case whereis(?MODULE) of
        undefined -> ok;
        OldPid -> 
            unlink(OldPid),
            unregister(?MODULE)
    end,
    register(?MODULE, self()),
    {ok, State}.
```

Use unique names with dynamic registration for concurrent workers:

```erlang
Name = list_to_atom("worker_" ++ integer_to_list(Id)),
register(Name, self()).
```

Handle the case where registration fails gracefully:

```erlang
safe_register(Name, Pid) ->
    case register(Name, Pid) of
        true -> ok;
        false -> {error, name_taken}
    end.
```

## Common Mistakes

- Using `permanent` restart type when process should not restart. Use `transient` for processes that should only restart on abnormal termination.
- Not unlinking old process before unregistering. This can cause the new process to receive signals intended for the old one.
- Assuming process is dead when it may be shutting down slowly. Always check with `whereis/1` before registering.
- Using atoms as names without considering memory implications. Atoms are never garbage collected, so dynamic atom creation can exhaust memory.
- Not handling the race condition between `whereis` and `register`. Use a process dictionary or ETS for atomic registration.

## Related Pages

- [noproc]({{< relref "/languages/erlang/noproc" >}}) - process not found
- [process-crash]({{< relref "/languages/erlang/erlang-process-crash" >}}) - process crash
- [supervisor-restart]({{< relref "/languages/erlang/erlang-supervisor-restart" >}}) - supervisor behavior
- [timeout-error]({{< relref "/languages/erlang/erlang-timeout-error" >}}) - timeout errors
