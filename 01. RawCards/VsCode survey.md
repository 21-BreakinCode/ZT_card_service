---
source: iT邦邦忙
tags:
- programming/IDE
- project/vscode
---

> 1. [iT邦邦忙](https://ithelp.ithome.com.tw/users/20108634/ironman/3815?sc=hot)
> 2. [Official website](https://code.visualstudio.com/api)
> 3. [GitHub samples](https://github.com/microsoft/vscode-extension-samples)

- VsCode: 
	- IDE - Integrated Development Environment
	- base on Electron & Typescript
	- open source
- Basic structure
	- Editor: 編輯檔案的介面
	- Side bar: 左邊欄位，呈現不同功能的 view, 投過 activity bar 點擊
	- Activity bar: 最左邊側欄，可以自訂 icon 顯示或隱藏
	- Status bar: 最下面欄位，呈現目前 file 的狀態
	- Panels: integrate extensions output, `cmd+j` to open
- `settings.json` scope
	- User settings: global scope
	- Workspace settings: under `./vscode` or `.code-workspace`
	- debug settings: setting for debugging