---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
> [!info] Reference
> - [JS - primitive data type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structure)
> - 


# Primitive
> #### Explain: Not an object & no methods or properties
> - Except `null`, can be tested by `typeof`
> - Except `null` & `undefined`, have their corresponding object wrapper types, which provide useful methods for working with the primitive values.

|Type|`typeof` return value|Object wrapper|
|---|---|---|
|[Null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#null_type)|`"object"`|N/A|
|[Undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#undefined_type)|`"undefined"`|N/A|
|[Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)|`"boolean"`|[`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)|
|[Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)|`"number"`|[`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)|
|[BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#bigint_type)|`"bigint"`|[`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)|
|[String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)|`"string"`|[`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)|
|[Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)|`"symbol"`|[`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)|

# Primitive
```JS
// Number
let integer = 42;
let float = 3.14;

// BigInt -> arbitrary-precision integers
let bigIntValue = 1234567890123456789012345678901234567890n;

// String
let message = "Hello, World!";

// Boolean
let isTrue = true;
let isFalse = false;

// Null: intentional absence of any value or object
let noValue = null;

// Undefined
let uninitialized;
 
// Symbol -> unique and immutable value
let uniqueSymbol = Symbol("description");

```
## typeof operator

```JS
console.log(typeof 42);
// Expected output: "number"

console.log(typeof 'blubber');
// Expected output: "string"

console.log(typeof true);
// Expected output: "boolean"

console.log(typeof undeclaredVariable);
// Expected output: "undefined"
```
# Object
> [!example]- Built in object in JS
> #### Reference: [mdn docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
> - Number
> - Math
> - Date
> - String
> - Error
> - Function
> - Boolean

> Collection of key-value pairs

```JS
let person = {
  name: "John",
  age: 30,
  isStudent: false,
};
```

## Prototypes 
> [!info] Prototype object
> - Prototype object acts as a template or blueprint from which new objects inherit properties and methods.
> - Access through `.prototype` property

## Prototypal Inheritance
> [!info] OOP language implement
> - A feature in javascript used to add methods and properties in objects.
> - <mark style="background: #FF5582A6;">Object can inherit</mark> the properties and methods of another object.

```JS
Object.create()
```


```JS
// Creating a prototype object
const animalPrototype = {
  makeSound: function() {
    console.log("Some generic sound");
  },
}

// Creating a new object that inherits from animalPrototype
const dog = Object.create(animalPrototype)
dog.makeSound()  // "Some generic sound"

// Adding a property to the prototype
animalPrototype.numLegs = 4

console.log(dog.numLegs)  // 4 (inherited from prototype)

// Creating a new object with its own properties
const bird = {
  numLegs: 2,
  fly: function() {
    console.log("Flying high")
  },
}

bird.makeSound();  // "Some generic sound"
console.log(bird.numLegs)  // 2 (overriding inherited property)
bird.fly()  // "Flying high"

///////////////// Access through .prototype ///////////////////

function Animal() {
  // Constructor code
}

Animal.prototype.makeSound = function() {
  console.log("Some generic sound");
};

function Dog() {
  // Constructor code
}

// Set up the prototype chain
Dog.prototype = Object.create(Animal.prototype);

const dog = new Dog();
dog.makeSound();  // Outputs: "Some generic sound"


```