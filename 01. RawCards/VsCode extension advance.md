---
source: iT邦邦忙
tags:
- programming/IDE
- project/vscode
---


# createOutputChannel API
> [!info] 
> https://ithelp.ithome.com.tw/articles/10245877


> 將 extension output 輸出到 panel 的 `Output` item

- API name: `createOutputChannel`
```JS
const channel = vscode.window.createOutputChannel('YourChannelName');
```
## under channel API object
|OutputChannel方法|描述|
|---|---|
|append|在panel中訊息的尾部換行後輸出訊息。|
|appendLine|在panel中訊息的尾部輸出訊息，不換行。|
|clear|清除所有panel上輸出的訊息。|
|dispose|釋放vscode分配給output channel的資源。|
|hide|隱藏顯示中的OutputChannel。|
|show|打開panel並呈現extension的OutputChannel訊息。|

# Webview
> [!info] 
> - [Webview 1](https://ithelp.ithome.com.tw/articles/10247079)
> - [Webview 2](https://ithelp.ithome.com.tw/articles/10247668)
> - [Webview 3](https://ithelp.ithome.com.tw/articles/10247935)
> - [Webview 4](https://ithelp.ithome.com.tw/articles/10248236)

# Using 3rd party extension
> [!info]
> - https://ithelp.ithome.com.tw/articles/10252996

- api name: `vscode.extension.###`

|Extensions API|描述|
|---|---|
|all|唯讀屬性，VSCode安裝的extension的物件陣列|
|getExtension|給定指定的extensionId，取得對應的extension物件|
|onDidChange|監聽extension被安裝、卸載、停用、啟用的方法|

- Extension object attributes

|Extension物件屬性or方法|描述|
|---|---|
|id|唯讀屬性，extension的id|
|isActive|唯讀屬性，VSCode安裝的extension的狀態|
|packageJSON|唯讀屬性，安裝的extension的package.json設定檔|
|extensionPath|唯讀屬性，安裝的extension的路徑|
|extensionUri|唯讀屬性，安裝的extension的VSCode Uri物件，物件底下有path等資訊。|
|extensionKind|唯讀屬性，extension的類型，用於區分是否為remote的extension。|
|exports|唯讀屬性，第三方extension exports的api，只能在extension已經active以後取得。|
|active|active獲取的extension的方法，會回傳一個thenable，可以在active結束後取得extension的public api。|