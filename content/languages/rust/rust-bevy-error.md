---
title: "[Solution] Rust Bevy Error — How to Fix"
description: "Fix Bevy game engine errors. Resolve ECS queries, resources, systems, and asset loading issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Bevy Error

Bevy errors occur during ECS setup, resource initialization, or when components are queried incorrectly. These errors surface during app building, system scheduling, or asset loading.

## Common Causes

```rust
use bevy::prelude::*;

// Conflicting query access — mutable and immutable on same component
fn bad_system(
    query: Query<&mut Transform>,
    other: Query<&Transform>, // ERROR: conflicting borrows
) { for t in &query { /* ... */ } }

// Missing resource that a system expects
fn system_with_resource(res: Res<MyResource>) {
    // Panics if MyResource was not inserted
}
```

## How to Fix

1. **Use disjoint components or filter to avoid query conflicts**

```rust
use bevy::prelude::*;

#[derive(Component)] struct Position(Vec3);
#[derive(Component)] struct Velocity(Vec3);

fn physics(mut positions: Query<(&mut Position, &Velocity)>) {
    for (mut pos, vel) in &mut positions { pos.0 += vel.0; }
}
```

2. **Initialize resources before systems that depend on them**

```rust
use bevy::prelude::*;

#[derive(Resource)]
struct GameState { score: u32 }
impl Default for GameState { fn default() -> Self { Self { score: 0 } } }

fn increment_score(mut state: ResMut<GameState>) { state.score += 1; }

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .init_resource::<GameState>()
        .add_systems(Update, increment_score)
        .run();
}
```

3. **Use `Option<Res<T>>` for optional resources**

```rust
use bevy::prelude::*;

#[derive(Resource)]
struct DebugMode(bool);

fn check_debug(debug: Option<Res<DebugMode>>) {
    if let Some(mode) = debug { if mode.0 { println!("Debug active"); } }
}
```

## Examples

```rust
use bevy::prelude::*;

#[derive(Component)] struct Player;
#[derive(Component)] struct Health(f32);
#[derive(Resource)] struct Score(u32);

fn spawn_player(mut commands: Commands) { commands.spawn((Player, Health(100.0))); }

fn damage_system(mut query: Query<&mut Health>, time: Res<Time>) {
    for mut health in &mut query {
        health.0 -= 10.0 * time.delta_secs();
        if health.0 <= 0.0 { println!("Player died!"); }
    }
}

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .insert_resource(Score(0))
        .add_systems(Startup, spawn_player)
        .add_systems(Update, damage_system)
        .run();
}
```

## Related Errors

- [Tokio Runtime Error]({{< relref "/languages/rust/rust-tokio-runtime-error" >}}) — async runtime issues
- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — concurrent access issues
- [Box Error]({{< relref "/languages/rust/rust-box-error" >}}) — allocation and sizing issues
