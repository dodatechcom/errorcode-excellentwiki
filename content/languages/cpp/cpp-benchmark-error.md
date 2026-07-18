---
title: "[Solution] C++ Benchmark Error — How to Fix"
description: "Fix C++ Google Benchmark errors including iteration count issues, incorrect state management, and measurement accuracy problems in performance testing."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Benchmark Error — How to Fix

Google Benchmark errors occur when `state.KeepRunning()` is called incorrectly, when benchmark functions modify shared state affecting measurements, when timing overhead from setup code dominates the measurement, or when fixtures aren't properly configured.

## Why It Happens

benchmark errors arise from placing expensive setup inside the timed loop, when `state.KeepRunning()` isn't used for fixed-iteration benchmarks, when the benchmark body is too fast for accurate measurement, when fixtures allocate resources in the constructor instead of the benchmark body, or when output format is misconfigured.

## Common Error Messages

1. `error: benchmark body too short — consider KeepRunning`
2. `warning: benchmark 'BM_Name' is too short`
3. `error: state must be passed by reference`
4. `error: fixture must inherit from ::benchmark::Fixture`

## How to Fix It

### Fix 1: Use Correct Benchmark Structure

```cpp
#include <benchmark/benchmark.h>
#include <vector>
#include <algorithm>

// CORRECT — simple benchmark
static void BM_VectorSort(benchmark::State& state) {
    for (auto _ : state) {
        state.PauseTiming();
        std::vector<int> v(state.range(0));
        std::iota(v.begin(), v.end(), 0);
        std::reverse(v.begin(), v.end());
        state.ResumeTiming();

        std::sort(v.begin(), v.end());
        benchmark::DoNotOptimize(v);
    }
}
BENCHMARK(BM_VectorSort)->Range(8, 1 << 20);
```

### Fix 2: Use Fixtures Properly

```cpp
#include <benchmark/benchmark.h>

class MyFixture : public benchmark::Fixture {
public:
    void SetUp(const benchmark::State& state) override {
        data_.resize(state.range(0));
    }

    void TearDown(const benchmark::State&) override {
        data_.clear();
    }

    std::vector<int> data_;
};

BENCHMARK_DEFINE_F(MyFixture, BM_FixtureSort)(benchmark::State& state) {
    for (auto _ : state) {
        std::sort(data_.begin(), data_.end());
        benchmark::DoNotOptimize(data_);
    }
}
BENCHMARK_REGISTER_F(MyFixture, BM_FixtureSort)->Range(8, 1 << 20);
```

### Fix 3: Control Timing Correctly

```cpp
#include <benchmark/benchmark.h>
#include <random>

static void BM_MeasuredWork(benchmark::State& state) {
    // CORRECT — setup outside the timed loop
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> dist(0, 1000);

    for (auto _ : state) {
        // PauseTiming for expensive non-measured setup
        state.PauseTiming();
        auto data = dist(rng);
        state.ResumeTiming();

        // Measured code
        benchmark::DoNotOptimize(data * data);
    }
}
BENCHMARK(BM_MeasuredWork)->Iterations(10000);
```

### Fix 4: Use Custom Counters

```cpp
#include <benchmark/benchmark.h>

static void BM_Throughput(benchmark::State& state) {
    int64_t total_items = 0;
    for (auto _ : state) {
        for (int i = 0; i < state.range(0); i++) {
            benchmark::DoNotOptimize(i);
        }
        total_items += state.range(0);
    }
    state.SetItemsProcessed(total_items);
    state.SetBytesProcessed(total_items * sizeof(int));
}
BENCHMARK(BM_Throughput)->Range(1, 1 << 10);
```

## Common Scenarios

- **Setup in loop**: Expensive initialization inside the timed loop skews results.
- **Compiler optimization**: Missing `DoNotOptimize` allows the compiler to remove dead code.
- **Small iteration counts**: Too few iterations produce noisy, unreliable measurements.

## Prevent It

1. Place all setup code before the timing loop or use `PauseTiming`/`ResumeTiming`.
2. Always use `benchmark::DoNotOptimize` to prevent dead code elimination.
3. Run benchmarks multiple times and report mean/median for reliability.

## Related Errors

- [Catch2 error]({{< relref "/languages/cpp/cpp-catch2-error.md" >}}) — testing issues.
- [Google test error]({{< relref "/languages/cpp/google-test-error" >}}) — testing issues.
- [CMake error]({{< relref "/languages/cpp/cpp-cmake-error-cpp.md" >}}) — build configuration issues.
