---
title: "[Solution] Rust Quote Error — How to Fix"
description: "Fix quote macro errors. Resolve token stream generation, hygiene, and code emission issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Quote Error

Quote errors occur when using the `quote` crate to generate Rust token streams — incorrect interpolation, missing imports, or malformed token output.

## Common Causes

```rust
use quote::quote;

// Wrong interpolation — using {} instead of #
let name = "MyType";
let tokens = quote! {
    struct {name} { // ERROR: should be #name
        field: i32,
    }
};

// Missing span for error reporting
let tokens = quote! {
    impl MyTrait for #name {
        fn method(&self) -> #unknown_type { } // unknown_type not in scope
    }
};

// Forgetting to handle generic parameters
let input: syn::DeriveInput = todo!();
let name = &input.ident;
let (impl_generics, ty_generics, where_clause) = input.generics.split_for_impl();
```

## How to Fix

1. **Use `#` for variable interpolation**

```rust
use quote::quote;

fn generate_struct(name: &syn::Ident, fields: &[&syn::Ident]) -> proc_macro2::TokenStream {
    quote! {
        pub struct #name {
            #(#fields: String),*
        }
    }
}

fn main() {
    let name = syn::Ident::new("Config", proc_macro2::Span::call_site());
    let fields = vec![
        syn::Ident::new("name", proc_macro2::Span::call_site()),
        syn::Ident::new("value", proc_macro2::Span::call_site()),
    ];
    println!("{}", generate_struct(&name, &fields));
}
```

2. **Handle generics properly**

```rust
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(MyTrait)]
pub fn my_derive(input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    let (impl_generics, ty_generics, where_clause) = input.generics.split_for_impl();

    let expanded = quote! {
        impl #impl_generics MyTrait for #name #ty_generics #where_clause {
            fn name(&self) -> &str { stringify!(#name) }
        }
    };
    proc_macro::TokenStream::from(expanded)
}
```

3. **Use `format_ident!` for creating identifiers**

```rust
use quote::{quote, format_ident};

fn generate_getters(fields: &[(syn::Ident, syn::Type)]) -> proc_macro2::TokenStream {
    let methods = fields.iter().map(|(name, ty)| {
        let getter = format_ident!("get_{}", name);
        quote! {
            pub fn #getter(&self) -> &#ty {
                &self.#name
            }
        }
    });
    quote! { #(#methods)* }
}
```

## Examples

```rust
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(Builder)]
pub fn builder_derive(input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    let builder = format_ident!("{}Builder", name);

    let fields = match &input.data {
        syn::Data::Struct(data) => &data.fields,
        _ => panic!("Builder only works on structs"),
    };

    let field_names: Vec<_> = fields.iter().map(|f| f.ident.as_ref().unwrap()).collect();
    let field_types: Vec<_> = fields.iter().map(|f| &f.ty).collect();

    let expanded = quote! {
        pub struct #builder {
            #(#field_names: Option<#field_types>),*
        }

        impl #builder {
            pub fn new() -> Self {
                Self { #(#field_names: None),* }
            }

            pub fn build(self) -> Result<#name, String> {
                Ok(#name {
                    #(#field_names: self.#field_names.ok_or("missing field")?),*
                })
            }
        }
    };
    proc_macro::TokenStream::from(expanded)
}
```

## Related Errors

- [Syn Error]({{< relref "/languages/rust/rust-syn-error" >}}) — syntax parsing
- [Proc Macro Error]({{< relref "/languages/rust/rust-proc-macro-error" >}}) — proc macros
- [Derive Error]({{< relref "/languages/rust/rust-derive-error" >}}) — derive macros
