---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
# Hoisting
> [!abstract] Explain
> process whereby the interpreter appears to move the _declaration_ of functions, variables, classes, or imports to the top of their scope, prior to execution of the code.

- Declaration hoisting: reference a variable in its scope before the line it is declared, which the value is always `undefined`
- can use variables or call functions <mark style="background: #FFF3A3A6;">before they are actually declared</mark> in the code.
- ONLY the <mark style="background: #FF5582A6;">declarations</mark> are hoisted, not the assignments or initializations.
```JS
console.log(x); // undefined
var x = 10;
console.log(x); // 10


foo(); // "Hello from foo!"
function foo() {
  console.log("Hello from foo!");
}


////////////////// temporal dead zone examples /////////////////
const x = 1;
{
  console.log(x); // ReferenceError
  const x = 2;
}

// to fix -> can't use same var name
const x = 1;
{
  console.log(x); // Outputs 1
  const y = 2;
}
////////////////////////////////////////////////////////////////


```