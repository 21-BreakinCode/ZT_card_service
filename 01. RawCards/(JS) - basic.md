---
source: roadmap.sh
tags:
- programming/JS
- project/JS/30days
---
# Introduction
- Statically-typed programming language
- Superset of JS
- Key different
	- `Type`: CAN specify data type of var, para, return value
	- `Syntax`: interfaces, classes, namespaces
	- `Tooling`: better editor, type checking, code refactoring tools support
	- `Backwards compatibility`: work with JS env
## Install & run with `dev env`
- flag: `--save` vs. `--save-dev`
```bash
# init npm
npm init

# use as default, can don't type --save flag
npm install --save typescript

# use as for dev dependency
npm install --save-dev typescript
```
## tsconfig file for compiling
> [!note] Doc
> - [tsconfig doc](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html#handbook-content)
> - [tsc CLI options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)


- Need to create `tsconfig.file` to specify compiler options, ex:
```TS
{
  "compilerOptions": {
    "target": "es5",  // the version of JS to compile to
    "module": "commonjs",  // module system to use
    "strict": true,  // enable strict type checking
    "outDir": "./dist",  // the dir to output the compiled JS files
    "rootDir": "./src" // the root dir of TS files
    "exclude": ["node_modules"] // array of file/dir to exclude from compilation
  },
  "include": ["src"] // array of file/dir to include from compilation
}
```

- Run compile with:
```bash
tsc

# run TS files by specifying file name
tsc ${file_name.ts}
```