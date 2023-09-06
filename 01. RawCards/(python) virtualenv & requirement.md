---
source: python
tags:
- programming/python
---
> [!info] Reference
> - [DAY03-搞懂Python的virtualenv ](https://ithelp.ithome.com.tw/articles/10199980)

# Basic intro

- 產生一個「虛擬資料夾」for 乾淨的環境重新使用
- specify python version
```bash
virtualenv --python=/opt/python-3.6/bin/python venv
```

- Create
```bash
python3 -m venv venv
```

- Enter
	- In macOS/Linux: `source ./venv/bin/activate`
- Leave
	- `deactivate`

# Requirements

- Layout `requirement.txt`
```bash
pip freeze > requirements.txt
```
- Install with requirement.txt
```bash
pip install -r requirements.txt
```