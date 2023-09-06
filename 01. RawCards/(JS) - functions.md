---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
> [!info] 
> Consist of `function` keyword, followed by:
> - name of function
> - list of parameters that define the function, enclosed in curly brackets `{}`.
> - parameters configuration: 
> 	- `Default value(=)`: default value of input parameter
> 	- `Rest parameters(...)`: accept an indefinite number of arguments as an array

# Function declaration
### Syntax
```JS
function functionName(para1, para2){
	return para1 * para2
}

// setting default value
function functionName(para1, para2 = 2){
	return para1 * para2
}

// Rest parameters
function sum(...theArgs) {
  let total = 0;
  for (const arg of theArgs) {
    total += arg;
  }
  return total;
}

console.log(sum(1, 2, 3)) // 6
console.log(sum(1, 2, 3, 4)) // 10
```
## arguments object

> [!info] `arguments` key word
> - Array-like object accessible inside [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) that contains the values of the arguments passed to that function.

```JS
function func1(a, b, c) {
  console.log(arguments[0]);
  // Expected output: 1

  console.log(arguments[1]);
  // Expected output: 2

  console.log(arguments[2]);
  // Expected output: 3
}

func1(1, 2, 3);
```

## Function expression
> [!info] function can be **anonymous**.

### Syntax
```JS
const square = function (number) {
  return number * number;
};

console.log(square(4)); // 16

```

## Arrow function
> [!info] Alternative to traditional expression with some differences
> - Arrow functions don't have their own `bindings` to `this`, [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments), or [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super), and should not be used as [methods](https://developer.mozilla.org/en-US/docs/Glossary/Method).
> - Arrow functions cannot be used as [constructors](https://developer.mozilla.org/en-US/docs/Glossary/Constructor). Calling them with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new) throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError). They also don't have access to the [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target) keyword.
> - Arrow functions cannot use [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield) within their body and cannot be created as generator functions.

### Syntax
```JS
() => expression

param => expression

(param) => expression

(param1, paramN) => expression

() => {
  statements
}

param => {
  statements
}

(param1, paramN) => {
  statements
}
```

```JS
// Traditional anonymous function
(function (a) {
  return a + 100;
});

//////// Translate to arrow function //////
// 1. Remove the word "function" and place arrow between the argument and opening body bracket
(a) => {
  return a + 100;
};

// 2. Remove the body braces and word "return" — the return is implied.
(a) => a + 100;

// 3. Remove the parameter parentheses
a => a + 100;

```

# IIFE
> [!info] Immediately-Invoked Function Expression => `+ ()`
> - A function that is executed immediately after it is created.
> - Add a pair of brackets at the end of the function

```JS
(function () {
  // …
})();

(() => {
  // …
})();

(async () => {
  // …
})();
```