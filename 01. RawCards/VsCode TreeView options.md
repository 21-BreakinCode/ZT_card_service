---
source: iT邦邦忙
tags:
- programming/IDE
- project/vscode
---
> [!info] Reference
> - [Official website](https://code.visualstudio.com/api/extension-guides/tree-view)
> - https://ithelp.ithome.com.tw/articles/10245169
# Register
- In `config.json` 的 `Contribution Points`
```json
"contributes": { 
	"views": { 
		"${選單元件位置}": [ { 
			"id": "${樹狀選單Id}", 
			"name": "${樹狀選單名字}", 
			"icon": "${選單Icon路徑}", 
			"contextualTitle": "${樹狀選單標題}" 
		} ] 
}
```