---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
> [!info]+ Reference
> - [Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
> - [[Naming convention|JS naming convention]]

> A variable is a `container for a value`, like a number we might use in a sum, or a string that we might use as part of a sentence
# Variable declarations

- `var`
	- legacy way 
	- <mark style="background: #FFF3A3A6;">DON'T have</mark> block-level scope --> issues related to scoping and hoisting.
	- can be accessed before they're declared, However, their values are `undefined` until they're assigned a value.

- `const`
	- <mark style="background: #FF5582A6;">temporal dead zone</mark>: has block-level scope, meaning they're limited to the block in which they're defined (e.g., inside curly braces `{}`).
	- MUST assign a value to a `const` variable when declaring it.
	- declare variables whose <mark style="background: #FF5582A6;">values should not be re-assigned</mark> after they're assigned once.
		- BUT if the value is an<mark style="background: #FFF3A3A6;"> object or array</mark>, you can still modify its properties or elements

- `let`
	- <mark style="background: #FF5582A6;">temporal dead zone</mark>: has block-level scope, like `const`
	- mutable, meaning their values <mark style="background: #FFF3A3A6;">can be re-assigned</mark>
	- also hoisted to the top of their scope, but unlike `var`, their values are **not automatically initialized** to `undefined`
```JS
// var example
var x = 10;
if (true) {
  var x = 20;
}
console.log(x); // 20

// const example
const y = 10;
// y = 20; // Error: Cannot re-assign a const variable

// let example
let z = 10;
if (true) {
  let z = 20; // This creates a new variable in a different scope
}
console.log(z); // 10

```
# Scopes
## Global scope
> <mark style="background: #FF5582A6;">Declared outside</mark> any function or curly braces ’{}’ have Global Scope, and can be accessed from anywhere within the same Javascript code.
## Function scope
> Declared <mark style="background: #FF5582A6;">within a function</mark> can only be used within that same function. 
> 
> Outside that function, they are `undefined`.
## Block scope
> Declared <mark style="background: #FF5582A6;">within a block '{}'</mark> can not be accessed outside that block.
> 
> ONLY provided by `let`, `const`