---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
> [!info] Review
> 1. `for statement`: (int; condition; update)
> 2. `for ... in`: key
> 3. `for ... of`: value
> 4. `do ... while`: evaluate after statement
> 5. `while`: evaluate before statement

> [!example] for statement
> - Repeatedly execute a piece of code a known number of times
> ```JS
> // for (init; condition; update) {statement}
> 
> for (let i = 0; i < 5; i++) {
> 	console.log(i)
> }
> ```


> [!example] for...in 
> iterates enumerable properties of an object that are ==keyed== by ==strings==
> ```JS
> const object = { a: 1, b: 2, c: 3 }
> for (const property in object){
> 	console.log(`${property}: ${object[property]}`)
> }
> // "a: 1"
> // "b: 2"
> // "c: 3"
> ```

> [!example] for...of
> Executes a loop that operates on a ==sequence of values== sourced from an iterable object.
> ```JS
> const array1 = ['a', 'b', 'c']
> 
> for (const element of array1) {
> 	console.log(eleement)
> }
> // "a"
> // "b"
> // "c"
> ```

> [!example] do...while
> - creates a loop that executes a specified statement until the test condition evaluates to false
> - condition is evaluated after executing the statement,
> ```JS
> let result = ''
> let i = 0
> 
> do {
> 	i ++ 
> 	result += i
> } while (i < 5)
> 
> console.log(result)  // "12345" --> due to result init as 'str'
> ```

> [!example] while + break || continue
> - `break`: jump out of a loop or a switch block
> - `continue`: skip one loop iteration
> ```JS
> let i = 0
> let sum = 0
> 
> while ( i < 8) {
> 	i += 1
> 	
> 	if (i === 2) {continue}
> 	
> 	if (i === 6) {break}
> 	
> 	text = text + i
> }
> console.log(sum) // 1 + 3 + 4 + 5 = 13
> ```