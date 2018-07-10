# HotReloadPy
HotReloadPy is a development support script. It watches Python files (*.py) in your project and runs a command when you change a file. This is very useful when you are developing python web server.

## Usage
``` sh
./hot_reload.py <project-directory> [<command> ...]
```

## Example
### Run python server
``` bash
./hot_reload.py . python test/server.py

> listening on port: 8080
# edit port 8080 -> 8888 in test/server.py
> [changed]  test/server.py
> listening on port: 8888
```
