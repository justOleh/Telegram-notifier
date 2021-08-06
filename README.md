### Telegram Notifier Bot

### installation
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Setup/build

```
python setup.py py2app
```

### Usage
  
change TOKEN to your bot's TOKEN  
change chat_id to your id of chat with bot. 

#### Running python code
    python3 main.py path_to_interpreter path_to_script arguments
#### Running built app


copy config.yaml into dist/main.app/Contents/Resources/config.yaml
```
dist/main.app/Contents/MacOS/main path_to_interpreter path_to_script arguments
```
