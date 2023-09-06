---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---

> [!info] Reference
> - [Data structures](https://www.freecodecamp.org/news/data-structures-in-javascript-with-examples/#what-is-a-data-structure)
> - [Introduction to the Stack Data Structure](https://youtu.be/4F-BnR2XwqU)
> - [Introduction to the Queue Data Structure](https://youtu.be/GRA_3Ppl2ZI)
> - [Intro to Recursion: Anatomy of a Recursive Solution](https://youtu.be/yBWlPte6FhA)
> - [Binary Tree Algorithms for Technical Interviews - Full Course](https://youtu.be/fAAZixBzIAI)
> - [Graph Algorithms for Technical Interviews - Full Course](https://youtu.be/tWVWeAqZ0WU)
> - [Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://youtu.be/oBt53YbR9Kk)



- Type: 
	- Primitive (built-in)
	- Non-primitive (not built-in)

# Indexed Collections

> [!example] Collections of data that are ordered by an index value
## Typed Arrays
> Ref: [Introduction](https://www.youtube.com/watch?v=UYkJaW3pmj0)

- Declaration

|Type|Value Range|Size in bytes|Web IDL type|
|---|---|---|---|
|[`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)|-128 to 127|1|`byte`|
|[`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)|0 to 255|1|`octet`|
|[`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)|0 to 255|1|`octet`|
|[`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)|-32768 to 32767|2|`short`|
|[`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array)|0 to 65535|2|`unsigned short`|
|[`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)|-2147483648 to 2147483647|4|`long`|
|[`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)|0 to 4294967295|4|`unsigned long`|
|[`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)|`-3.4e38` to `3.4e38`|4|`unrestricted float`|
|[`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)|`-1.8e308` to `1.8e308`|8|`unrestricted double`|
|[`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)|-263 to 263 - 1|8|`bigint`|
|[`BigUint64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)|0 to 264 - 1|8|`bigint`|

## Arrays

- Declaration
```JS
let arr = []
```
- Method
	- array`.length`: call the length of the array

	- `push`: adds element to the end
	- `pop`: takes element from the end

	- `shift`: remove first element
	- `unshift`: add to the first element
- Iterate
```JS
// Way 1
for (let i = 0; i < arr.length; i++){
	alert( arr[i] );
}

// Way 2
for (let item of array){
	alert( item );
}

// Way3
for (let key in array){
	alert( array[key] )
}
```
# Keyed Collections
## Map
> [!example] Hold key-value pairs & remembers original insertion order.
> The main difference is `Map` allows keys of **any type**.

- Declaration & Methods
```JS
let map = new Map()

// map.set(key, value)
map.set('1', 'str1')
map.set(1, 'num1')
map.set(true, 'bool1')

// map.get(key) -> return value
map.get('1') // expected str1
map.get(1) // expected num1

// map.has(key) -> return bool
map.has(1) //true
map.has('error_key')  // false

// map.delete(key): remove element by key
map.delete(1) 

// map.clear(): removes everything from the map

// map.size -> count of element in map
```

- Iteration
```JS
let recipeMap = new Map([
	['cucumber', 500],
	['tomatoes', 350],
	['onion', 50]
]);

// map.key()
for (let vegetable of recipeMap.keys()) {
	alert(vegetable); // cucumber, tomatoes, onion
}

// map.value()
for (let amount of recipeMap.values()) {
	alert(amount); // 500, 350, 50
}

// iterate over [key, value] entries
for (let entry of recipeMap) { // the same as of recipeMap.entries()
	alert(entry); // cucumber,500 (and so on)
}
```
## Weak Map
> [!example] Map-like collection BUT keys must be `objects`

```JS
let weakMap = new WeakMap()
let obj = {}

weakMap.set(obj, 'this is allow')  // works fine 
weakMap.set('test', 'invalid') // Error, due to 'test' != object
```
## Set
> [!example] Store **unique values** of any type

- Declaration
```JS
// Way 1
const emptySet = new Set()

// Way 2
const set = new Set(['red', 'green', 'blue'])

// Way 3
const set = new Set()
.add('red')
.add('green')
.add('blue')
```

- Methods
```JS
// .add() -> adds an element to Set
set.add('unique value')

// .has() -> checks element exist: bool
const expectExist = set.has('red')
assert.equal(expectExist, true)

// .delete() -> removes element
set.delete('red')

// .size() -> number of elements in Set
set.size()

// .clear() -> removes all elements
set.clear()
```

- Iterate
```JS
for (const element in set){
	console.log(x)
}
```
## Weak Set
> [!example] Set-like collection BUT elements must be `objects`


# Structure Data
## JSON
> [!info] JavaScript Object Notation
> Standard text-based format for representing structured data based on JavaScript object syntax