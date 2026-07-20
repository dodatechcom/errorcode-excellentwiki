---
title: "[Solution] Julia JuMP Optimization Error Fix"
description: "Fix Julia JuMP optimization errors when formulating or solving optimization problems."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1188
---

## What This Error Means

A JuMP error occurs when modeling or solving optimization problems. Common issues include infeasible problems, unbounded objectives, or solver errors.

## Common Causes

- Problem is infeasible (no solution exists)
- Problem is unbounded
- Wrong variable type (continuous vs integer)
- Solver not installed or configured

## How to Fix

```julia
using JuMP, HiGHS

model = Model(HiGHS.Optimizer)
@variable(model, x >= 0)
@objective(model, Min, x)
@constraint(model, x >= 1)

optimize!(model)
println(objective_value(model))  # 1.0
```

```julia
# Infeasible problem
model = Model(HiGHS.Optimizer)
@variable(model, x >= 10)
@constraint(model, x <= 5)
optimize!(model)
println(termination_status(model))  # INFEASIBLE
println(resulting_status = MOI.INFEASIBLE)
```

```julia
# Unbounded problem
model = Model(HiGHS.Optimizer)
@variable(model, x)
@objective(model, Min, x)
optimize!(model)
println(termination_status(model))  # UNBOUNDED
```

```julia
# Integer programming
model = Model(HiGHS.Optimizer)
@variable(model, x >= 0, Int)
@constraint(model, x <= 10)
@objective(model, Max, x)
optimize!(model)
println(objective_value(model))  # 10
```

## Related Errors

- [Julia domain error](julia-domain-error) - domain error
- [Julia dimension mismatch](julia-dimension-mismatch) - dimension issue
- [Julia type error](julia-type-error) - type error
