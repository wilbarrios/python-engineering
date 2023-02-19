# Useful python commands 💻

|Action|Command|Usage|
|---|---|---|
|Update pip|`pip3 install --upgrade pip`|n/a|
|pip help|`pip3`|n/a|
|Installed pips|`pip3 list`|n/a|
|Create dependencies static requirements|`pip3 freeze > *file_name.txt*`|`pip3 freeze > requirements.txt`|
|Remove all dependencies|`pip3 freeze | xargs pip3 uninstall -y`|n/a|
|Install all `freeze` dependencies|`pip3 install -r requirements.txt`|n/a|
