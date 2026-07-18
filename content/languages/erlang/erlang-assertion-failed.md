---
title: "[Solution] Erlang Assertion Failed in Gen Server"
description: "Fix Erlang assertion_failed error in gen_server callbacks. Resolve state validation and callback contract violations."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `assertion_failed` error in gen_server indicates that an internal assertion or state validation check has failed. This typically happens when the gen_server state does not match expected invariants, or when callback return values violate the gen_server contract.

## Why It Happens

- State transitions violate expected invariants: The state machine enters an invalid state.
- Reply sent from wrong callback function: Using `reply` in `handle_cast` instead of `handle_call`.
- Return tuple from callback has wrong structure: The gen_server expects specific tuple formats for each callback.
- Terminating with invalid reason format: The stop reason does not match expected formats.
- Call or cast handler returns malformed state: The new state does not maintain required invariants.

## How to Fix It

Validate state at the beginning of each callback to ensure it meets expectations:

```erlang
init(Args) ->
    State = #{counter => 0, status => active},
    {ok, State}.

handle_call(get_count, _From, #{counter := Count} = State) ->
    {reply, Count, State};
handle_call(increment, _From, #{counter := Count} = State) ->
    NewState = State#{counter => Count + 1},
    {reply, ok, NewState};
handle_call(_Request, _From, State) ->
    {reply, {error, unknown_request}, State}.
```

Ensure return tuples follow gen_server contract. Each callback must return one of these formats:

```erlang
%% CORRECT return values for handle_call
{reply, Reply, NewState}           %% synchronous with reply
{reply, Reply, NewState, Timeout}  %% with timeout
{noreply, NewState}                %% async without reply
{noreply, NewState, Timeout}       %% async with timeout
{stop, Reason, Reply, NewState}    %% terminate with reply
{stop, Reason, NewState}           %% terminate without reply
```

Add defensive state validation to catch invariant violations early:

```erlang
handle_cast(update, #{status := active} = State) ->
    NewState = do_update(State),
    {noreply, NewState};
handle_cast(update, #{status := inactive} = State) ->
    {noreply, State};
handle_cast(update, State) ->
    {stop, {invalid_state, State}, State}.
```

Handle unexpected messages gracefully in handle_info:

```erlang
handle_info(Msg, State) ->
    io:format("Unexpected message: ~p~n", [Msg]),
    {noreply, State}.
```

Use a separate validation function for complex state invariants:

```erlang
validate_state(#{counter := C, status := S}) when C >= 0, 
    (S =:= active orelse S =:= inactive) ->
    ok;
validate_state(State) ->
    {error, {invalid_state, State}}.
```

## Common Mistakes

- Returning a plain value instead of `{reply, Value, State}`. The gen_server framework requires specific tuple formats.
- Modifying state without returning the full new state map. Always return the complete new state.
- Sending reply twice in a single callback. Only one reply should be sent per handle_call.
- Not handling all message types in handle_info. Any message not handled will cause issues.
- Forgetting to update timeout values when returning timeout tuples.

## Related Pages

- [process-crash]({{< relref "/languages/erlang/erlang-process-crash" >}}) - process crash
- [supervisor-restart]({{< relref "/languages/erlang/erlang-supervisor-restart" >}}) - supervisor restart
- [timeout-error]({{< relref "/languages/erlang/erlang-timeout-error" >}}) - gen_server timeout
- [try-catch-error]({{< relref "/languages/erlang/erlang-try-catch-error" >}}) - try/catch handling
