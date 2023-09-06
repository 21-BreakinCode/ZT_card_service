---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---

# Equality algorithms

- isLooselyEqual: <mark style="background: #FF5582A6;">double equal</mark>
	- Return `boolean`
	- Doesn't check type  (will do type conversion)
	- `Nan != NaN`
	- `-0 == +0`
- isStrictlyEqual: <mark style="background: #FF5582A6;">triple equal</mark>
	- Return `boolean`
	- Check type
	- `Nan != NaN`
- SameValue: <mark style="background: #FF5582A6;">object.is()</mark>
	- `Type(x)` is not `Type(y)` return False: `boolean`
	- If `x` is Number, then return `Number::sameValue(x,y)`
		- else `SameValueNonNumber(x,y)`
	- `NaN == NaN` (different with ==triple equal==)
	- `-0 != +0`
- SameValueZero: <mark style="background: #FF5582A6;">used by many built in Operations</mark>
	- `Type(x)` is not `Type(y)` return False: `boolean`
	- If `x` is Number, then return `Number::sameValueZero(x,y)`
		- else `SameValueNonNumber(x,y)
	- `NaN == NaN`
	- `-0 == 0`


# Value Comparisons
## Loose equality
> [!info] ==
> - <mark style="background: #FF5582A6;">DON'T</mark> check data type.
> - Convert  values to common type of comparison. 

```JS
1 == "1"; // true (number 1 is coerced to string "1")
true == 1; // true (boolean true is coerced to number 1)
0 == false; // true (number 0 is coerced to boolean false)
```
## Strict equality
> [!info] ===
> - Check BOTH type and values.

```JS
1 === "1"; // false (number 1 is not the same as string "1")
true === 1; // false (boolean true is not the same as number 1)
```

## SameValue
> [!info] `Object.is()`
> 