---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
> [!info] Reference
> - https://www.w3schools.com/js/js_scope.asp
# Global
> Declared Globally (outside any function) have Global Scope. 
> **Automatically**: assign a value to a variable that has not been declared.
> Global variables can be accessed from anywhere in a JavaScript program.

```JS
myFunction();  
  
// code here can use carName: Automatcially assign to global scope
  
function myFunction() {  
  carName = "Volvo";  
}
```

```JS
let carName = "Volvo";  
// code here can use carName  
  
function myFunction() {  
// code here can also use carName  
}
```

# Function
> Declared `inside a function`, it is only accessible within that function and cannot be used outside that function

```JS
function myFunction() {  
  const carName = "Volvo";   // Function Scope  
}

// code here can NOT use carName
```
# Block
> Variables declared `inside a { }` block cannot be accessed from outside the block
> ONLY use with key word: `let`, `const`

```JS
function exampleFunction() {
  // Function scope
  const functionVar = 2;

  if (true) {
    // Block scope
    let blockVar = 3;
    const blockConst = 4;
  }

  console.log(functionVar); // Accessible
  
  console.log(blockVar); // Error: blockVar is not defined
  console.log(blockConst); // Error: blockConst is not defined
}

// console.log(functionVar); // Error: functionVar is not defined
// console.log(blockVar); // Error: blockVar is not defined
// console.log(blockConst); // Error: blockConst is not defined
```