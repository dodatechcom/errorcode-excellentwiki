---
title: "[Solution] Rust Proc Macro Error — How to Fix"
description: "Fix procedural macro errors. Resolve macro definition, token manipulation, and compilation issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Proc Macro Error

Proc macro errors occur when writing or using procedural macros — syntax errors in macro input, incorrect token manipulation, or compilation errors in the macro implementation.

## Common Causes

```rust
// In a proc macro crate
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

// panicking in a proc macro
#[proc_macro]
pub fn bad_macro(input: TokenStream) -> TokenStream {
    panic!("This macro always fails"); // Not a good error message
}

// Incorrect token stream generation
#[proc_macro_derive(BadDerive)]
pub fn bad_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    // Missing generics, where clause, etc.
    let expanded = quote! {
        impl MyTrait for #name {
            fn process(&self) -> String { String::new() }
        }
    };
    TokenStream::from(expanded)
}
```

## How to Fix

1. **Use `compile_error!` for user-friendly error messages**

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(MyTrait)]
pub fn my_trait_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;

    // Validate input
    match &input.data {
        syn::Data::Struct(_) => {},
        _ => {
            return syn::Error::new_spanned(
                name,
                "MyTrait can only be derived for structs",
            ).to_compile_error().into();
        }
    }

    let expanded = quote! {
        impl MyTrait for #name {
            fn process(&self) -> String { String::from("processed") }
        }
    };
    TokenStream::from(expanded)
}
```

2. **Use proper error reporting with `syn::Error`**

```rust
use syn::{parse_macro_input, DeriveInput, Fields};
use proc_macro::TokenStream;
use quote::quote;

#[proc_macro_derive(Builder)]
pub fn builder_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    let builder_name = quote::format_ident!("{}Builder", name);

    let fields = match &input.data {
        syn::Data::Struct(data) => &data.fields,
        _ => {
            return syn::Error::new_spanned(name, "Builder only works on structs")
                .to_compile_error().into();
        }
    };

    let field_names: Vec<_> = fields.iter().map(|f| &f.ident).collect();
    let field_types: Vec<_> = fields.iter().map(|f| &f.ty).collect();

    let expanded = quote! {
        pub struct #builder_name {
            #(pub #field_names: Option<#field_types>),*
        }

        impl #builder_name {
            pub fn new() -> Self {
                #builder_name { #(#field_names: None),* }
            }
            pub fn build(self) -> Result<#name, String> {
                Ok(#name {
                    #(#field_names: self.#field_names.ok_or("missing field")?.into()),*
                })
            }
        }
    };
    TokenStream::from(expanded)
}
```

3. **Test macros with `trybuild` crate**

```rust
// tests/ui/should_fail.rs
use my_macro::MyTrait;

#[derive(MyTrait)]
enum NotAStruct { A, B } // Should fail — only structs

// tests/ui/pass.rs
#[derive(MyTrait)]
struct Works { name: String }
```

## Examples

```rust
// A complete derive macro example
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(Describe)]
pub fn describe_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    let name_str = name.to_string();

    let expanded = quote! {
        impl #name {
            pub fn describe() -> &'static str {
                #name_str
            }
        }
    };
    TokenStream::from(expanded)
}
```

## Related Errors

- [Syn Error]({{< relref "/languages/rust/rust-syn-error" >}}) — syntax parsing
- [Quote Error]({{< relref "/languages/rust/rust-quote-error" >}}) — token generation
- [Derive Error]({{< relref "/languages/rust/rust-derive-error" >}}) — derive macros
