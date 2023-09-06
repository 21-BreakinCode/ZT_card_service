---
source: Prompt Engineer
tags:
- programming/AI
---
> [!info]+ What is Prompt?
> A set of instructions for AI to do a task.

![[PE basic.excalidraw|1080]]
# Prompt format
- Different format
	- context
	- instructions
	- multiple QA examples
	- other prompt

- Standard prompt
```txt
What is the capital of France?
```


# Technique
## [Role prompting](https://learnprompting.org/docs/basics/roles)

> Assign a role to AI
- Giving some context to AI and helps  the AI **understand the question better
```txt
You are a brilliant mathematician who can solve any problem in the world. 
Attempt to solve the following problem: What is 100*100/400*56?
```
# Few shot
> Standard prompt **with several examples** that prompt is trying to solve
```txt
Q: What is the capital of Spain?  
A: Madrid  

Q: What is the capital of Italy?  
A: Rome  

Q: What is the capital of France?
A: 
```

# Complex prompt
> Include context, instructions, and multiple examples prompt

```txt
Twitter is a social media platform where users can post short messages called "tweets".
Tweets can be positive or negative, and we would like to be able to classify tweets as
positive or negative. Here are some examples of positive and negative tweets. Make sure 
to classify the last tweet correctly.

Q: Tweet: "What a beautiful day!"
Is this tweet positive or negative?

A: positive

Q: Tweet: "I hate this class"
Is this tweet positive or negative?

A: negative

Q: Tweet: "I love pockets on jeans"

A:
```

