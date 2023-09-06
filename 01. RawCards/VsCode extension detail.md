---
source: iT邦邦忙
tags:
- programming/IDE
- project/vscode
---
# Context menu
> 點擊 extension icon 時，side bar 會顯示的內容

- [Reference](https://ithelp.ithome.com.tw/articles/10242098)

- 可以透過 extension project 的 `Contribution Point` 註冊 context menu
```json
"contributes": 
	{ ... 
		"menu": { 
			"${選單元件位置}": [ { 
				command: "${commandId}", 
				when: "${boolean}", 
				alt: "${commandId}", 
				group: "${Sorting Group}" 
			} ] 
	}
```

|屬性|描述|
|---|---|
|command|command的id，如前幾天所介紹|
|alt|備用的第二個commandId，按住alt鍵再點擊選單觸發|
|when|讀取context變數進行條件判斷後回傳的boolean決定是否顯示選單選項|
|group|選單選項的排序群組，不同UI排序群組各不相同，並可以照`${自訂群組名稱}@${順序數字}`的規則自訂順序群組([詳見](https://code.visualstudio.com/api/references/contribution-points#contributes.views)）|

# Extension in status bar & command interact
> - [Official API website](https://code.visualstudio.com/api/references/vscode-api#window)
> - https://ithelp.ithome.com.tw/articles/10244031
> - https://ithelp.ithome.com.tw/articles/10244737

> [!note] show
> - 狀態欄物件： `vscode.window.createStatusBarItem`
> - 使用者輸入框: `vscode.window.showInputBox`
> - 下拉選單: `vscode.window.showQuickPick`
> - 通知訊息：`vscode.window.showInformationMessage`
## register

- vscode.window.`createStatusBarItem`
## trigger
- trigger via vscode.commands.`registerCommand`
## create cmd platte toggle
- Create command toggle (`cmd+shift+p`) --> `vscode.window.showQuickPick`

## VsCode API outline
### variable
- <mark style="background: #FF5582A6;">取得</mark>，對當前colorTheme、window、textEditor、terminal的狀態與<mark style="background: #FFF3A3A6;">當前活躍</mark>(active)中的(termainal、textEditor)物件
### event
- 當前colorTheme、window、textEditor、terminal進行監聽的方法
- 可以在這些對象<mark style="background: #FFF3A3A6;">狀態發生改變</mark>時對其做些<mark style="background: #FFF3A3A6;">處理</mark>
### function
- 創建元件的方法與顯示提示訊息的message彈窗
- 創建元件類：諸如`createWebview`、`createStatusBarItem`、`createQuickPick`、`createInputBox`、`createOutputChannel`、`createTerminal`、`createTreeView`

# Extension workspace options
> - https://ithelp.ithome.com.tw/articles/10242706
> - https://code.visualstudio.com/api/references/contribution-points#contributes.configuration

# Data storage configuration
> - https://ithelp.ithome.com.tw/articles/10243437
> - https://code.visualstudio.com/api/extension-capabilities/common-capabilities