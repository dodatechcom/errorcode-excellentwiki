---
title: "[Solution] Rust Egui Error — How to Fix"
description: "Fix egui immediate mode GUI errors. Resolve rendering context, state, and widget configuration issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Egui Error

Egui errors occur when using the egui immediate-mode GUI library — issues with painting, context management, and integration with rendering backends.

## Common Causes

```rust
use eframe::egui;

// Painting outside of a frame
let ctx = egui::Context::default();
ctx.begin_pass(egui::Pos2::ZERO, &egui::RawInput::default());
// Missing end_pass — causes panic

// Updating UI from wrong thread
// eframe contexts are single-threaded

// Missing repaint request — UI doesn't refresh
fn update(ctx: &egui::Context) {
    // Without request_repaint(), the UI freezes until next event
}
```

## How to Fix

1. **Always pair begin_pass with end_pass**

```rust
use eframe::egui;

fn draw_ui(ctx: &egui::Context) {
    egui::CentralPanel::default().show(ctx, |ui| {
        ui.heading("Hello, Egui!");
        if ui.button("Click me").clicked() {
            println!("Button clicked!");
        }
    });
}
```

2. **Use request_repaint for continuous updates**

```rust
use eframe::egui;

fn update(ctx: &egui::Context) {
    // Request repaint for animations or real-time updates
    ctx.request_repaint();

    egui::CentralPanel::default().show(ctx, |ui| {
        let time = ctx.input(|i| i.time);
        ui.label(format!("Time: {:.2}", time));
    });
}
```

3. **Use channels for cross-thread communication**

```rust
use std::sync::mpsc;

struct App {
    receiver: mpsc::Receiver<String>,
}

impl App {
    fn new() -> (Self, mpsc::Sender<String>) {
        let (tx, rx) = mpsc::channel();
        (App { receiver: rx }, tx)
    }
}

impl eframe::App for App {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        // Check for messages from other threads
        while let Ok(msg) = self.receiver.try_recv() {
            ctx.request_repaint();
        }
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.label("Egui app running");
        });
    }
}
```

## Examples

```rust
use eframe::egui;

struct MyApp { count: i32 }

impl Default for MyApp {
    fn default() -> Self { MyApp { count: 0 } }
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Egui Counter");
            ui.horizontal(|ui| {
                if ui.button("-").clicked() { self.count -= 1; }
                ui.label(format!("{}", self.count));
                if ui.button("+").clicked() { self.count += 1; }
            });
        });
    }
}

fn main() -> eframe::Result<()> {
    eframe::run_native(
        "My App",
        eframe::NativeOptions::default(),
        Box::new(|_| Ok(Box::new(MyApp::default()))),
    )
}
```

## Related Errors

- [Iced Error]({{< relref "/languages/rust/rust-iced-error" >}}) — Iced framework issues
- [Slint Error]({{< relref "/languages/rust/rust-slint-error" >}}) — Slint framework issues
- [Tauri Error]({{< relref "/languages/rust/rust-tauri-error" >}}) — Tauri framework issues
