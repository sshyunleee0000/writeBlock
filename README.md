# Write Block

### Windows external storage write blocking software

- external storage write blocking software
- Manipulate Windows registry
- Using PyQt6 for GUI
- Can build .exe file with Pyinstaller

### Tested environments
1) OS: Windows 7 and later
2) Python: 3.7.0 and later
3) Python package
   1) PyInstaller:  4.6

---
### Setup development environments
1) Setup venv.
```shell
py -m venv venv
```
2) Install requirements.
```shell
pip install -r requirements.txt
```

---
### Build .exe file
1) Build.
```shell
pyinstaller --uac-admin --onefile --windowed --icon=logo.ico --name=WriteBlock main.py
```
2) It is created in the dist directory
