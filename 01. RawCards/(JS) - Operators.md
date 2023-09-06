---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---

> [!info] Reference
> - [YT explain](https://www.youtube.com/watch?v=nMQlXMHMz_Y)

> [!example]+ Operators brief
> - [[(JS) - Equality Comparisons]]
> - Assign
> - Comparison
> - Arithmetic
> - Bitwise
> - String concat
> - Logical (double symbol)
> - Condition
> - Comma
# Type 

- Assignment 
	- `'='`
- Comparison
	- `>`, `<`, `>=`, `<=`, `'=='`, `'==='`, `!=`, `!===`
- Arithmetic 
	- `+`
	- `-`
	- `*`
	- `**`
	- `/`
	- `%`
	- `++` (increment)
	- `--` (decrement)
- Bitwise
	- > perform their operations on such binary representations, but they return standard JavaScript numerical values.

	- `&` (AND)
	- `|` (OR)
	- `^` (XOR)
	- `~` (NOT)
	- `<<` (Left SHIFT)
	- `>>` (Right SHIFT)
	- `>>>` (Zero-Fill Right SHIFT)
- String concat
	- `+`
	- `+=`
- Logical
	- `&&` --> and
	- `||` --> or
	- `!` --> not
	- `??` --> Nullish Coalescing
		- returns its right-hand side operand when its left-hand side operand is `null` or `undefined`, and otherwise returns its left-hand side operand.
```JS
const foo = null ?? 'default string'
console.log(foo) // default string

const baz = 0 ?? 42
console.log(baz) // 0
```

- Condition 
```JS
condition ? 'true statement' : 'false statment'
```

- Comma
	- > operator evaluates each of its operands (from left to right) and returns the value of the last operand. This is commonly used to provide multiple updaters to a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) loop's afterthought.
```JS
let x = 1;

x = (x++, x)
console.log(x) // 2

x = (2, 3)
console.log(x) // 3
```