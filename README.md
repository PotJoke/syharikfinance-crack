# DARK HUMOR PENTEST TOOL
Provided script can be used to farm diamonds on github.com/Syharik3316/SyharikFinance
  
## Process Description
1. Script asks if you want to launch hydra mode(deleting one accaunt creates two new) 
2. Launches web initialize (Tor enabled by default)
3. Launches main exploit (api abuse)
4. If exploit struggles to connect account, it just creates new one (hydra script)
5. If script detects that ip is banned, it's just changes it (with tor help)


## Features

- Integrated tor network to awoid ip ban with auto-update
- Hydra: multiplying feature: if account is down - creates two new accounts

## Setup


- Install dependencies:
```
	pip install tor_proxy
	pip install pysocks
	pip install stem
```
- On Windows:
 ```
	 pip install win-tor-resources
 ```
 - Edit torrc in your tor by adding
```
ControlPort 9051
CookieAuthentication 0
HashedControlPassword 16:...(generate hash password)
```
-Also change in torrc:
```DisableNetwork 0```
	to
```DisableNetwork 1```
- Rename config.py.example TO config.py AND insert actual data
- Launch tor
- Launch code:
```python main.py```
or
```python3 main.py```


