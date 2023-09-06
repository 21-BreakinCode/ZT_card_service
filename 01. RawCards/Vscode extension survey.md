---
source: iT邦邦忙
tags:
- programming/IDE
- project/vscode
---
> - [iT邦邦忙](https://ithelp.ithome.com.tw/articles/10240741)
> - https://yeoman.io/
> - [package.json manifest](https://code.visualstudio.com/api/references/extension-manifest)
> - [VsCode API](https://code.visualstudio.com/api/references/vscode-api)
> - [cmd](https://code.visualstudio.com/api/extension-guides/command)
> - [built-in cmd](https://code.visualstudio.com/api/references/commands)
> - [Key-binding reference](https://code.visualstudio.com/docs/getstarted/keybindings)


# yoman

- VSCode官方已經發布了VSCode Yoman專案，並且定期更新，因此我們可以直接使用yo指令產生VSCode Extension，無需手動開發yoman樣板
- `npm install -g yo generator-code`
- `yo code`
# Extension types

|Extension選項|描述|
|---|---|
|New Extension(Typescript)|產生使用typescript開發的extension專案|
|New Extension(Javascript)|產生使用javascript開發的extension專案|
|New Color Theme|配置VSCode介面顏色的擴充套件專案(詳見: Color Theme)|
|New Language Support|程式語言(Programming Languages)擴充套件|
|New Code Snippets|程式碼片段擴充套件|
|New Keymap|快捷鍵擴充套件，keymap讓使用者得以在vscode中使用vim、sublime等等不同編輯器的快捷鍵開發。|
|New Extension Pack|打包多個已發佈的extension，讓使用者一鍵快速安裝。|
|New Language Pack (Localization)|配置VSCode編輯器多國語氣的擴充套件。|

# under /.vscode
|檔案名稱|說明|
|---|---|
|task.json|設定defaultBuild Task，用於compile extension專案的typescript程式。|
|launch.json|配置debug mode的兩個選項：`Run extension`與`Test extension`，用於執行extension主程式與相關測試程式，程式執行前，會先執行defulat buildTask。|
|settings.json|extension專案的設定檔，此處的設定會覆蓋user settings跟default settings。|
|extensions.json|設定用於輔助extension專案安裝的extension recommendations list，此處推薦安裝eslint extension。|

# cmd API
|Command API|描述|
|---|---|
|getCommands|取得vscode中註冊的commands，可以給一個boolean值決定是否列出vscode內部使用的command(預設會列出)，內部command的id均以下劃線開頭。|
|registerCommand|跟vscode註冊一個可以被keyborad shortcut、extension程式或其他ui元件呼叫(invoke)的命令。註冊同一個command id兩次會產生錯誤。|
|registerTextEditorCommand|與registerCommand類似，但只有在vscode有開啟文件的editor(active Editor)時才會觸發。|
|executeCommand|透過給定的commandId執行對應的內建或extension註冊的command。|
