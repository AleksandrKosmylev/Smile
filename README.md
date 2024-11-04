### Installation
Install environment
```
python3 -m venv .venv
```
Activate environment
```
source .venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
### Start script
* Change webhook in bitrix_candidate.py: 

BITRIX_WEBHOOK_URL = '***'

* Get candidate data and write to xmls file.

Creates canidate_table.xlsx with data
```
python bitrix_candidate.py 
```

* Send data to bitrix  smartcard

Sends data from database.xlsx
```
python smart_card.py 
```

