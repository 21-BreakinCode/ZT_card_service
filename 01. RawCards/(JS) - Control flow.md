---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
# Conditional Statements
## if...else
> [!info]
> - if
> - else if
> - else
```JS
if (condition) {
  statement1
} else if (condition3) {
  statement2
} else {
  statement3
}
```

## Switch
> [!info]
> - switch (value_condition)
> - case need to break at the end
> - `default` will be jumped to if no `case` matches
```JS
const expr = 'Papayas';

switch (expr) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
    
  case 'Mangoes':
	console.log('Mangoes are $0.41 a pound.')
  
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // Expected output: "Mangoes and papayas are $2.79 a pound."
    break;
    
  default:
    console.log(`Sorry, we are out of ${expr}.`);
}
```
# Exception Handling
> [!info] Basic knowledge of exceptions in JS
> - All exceptions are simply objects. 
> - While the majority of exceptions are implementations of the global Error class, any old object can be thrown.
> - Two ways to throw an exception: directly via an Error object, and through a custom object.

## throw statement
> Generates an custom error`

```JS
function getRectArea(width, height) {
  if (isNaN(width) || isNaN(height)) {
	// throw statment
    throw new Error('Parameter is not a number!')
  }
}

try {
  getRectArea(3, 'A');
} catch (e) {
  console.error(e)// Error: Parameter is not a number!
}
```


## try / catch / finally
> [!info] Explain
> - `try`: defines a code block to run
> - `catch`: defines a code block to handle any error
> - `finally` code block to run regardless of the result

```JS
try {  
  // Block of code to try  
}  
catch(err) {  
  // Block of code to handle errors  
}  
finally {  
  // Code block to be executed regardless of the try / catch result  
}
```

## Utilizing Error Objects
> [!info] JS also has other core Error constructors.
> - [AggregateError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError)
> - [EvalError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/EvalError)
> - [InternalError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)
> - [RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
> - [ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
> - [SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

```JS
try {
  willGiveErrorSometime();
} 
catch (error) {
  if (error instanceof RangeError) {
    rangeErrorHandler(error);
  } 
  else if (error instanceof ReferenceError) {
    referenceErrorHandle(error);
  } 
  else {
    errorHandler(error);
  }
}
```