---
source: homebrew
tags:
- software/packageManager
---


- `brew list`: list pkg installed by brew
	- `brew list > brew-list.txt`: print current brew requirements
	- `brew install $(cat brew-list.txt)`: install pkg from **brew-list.txt**
- `brew --cask`: for installing **GUI** tools with specific software 