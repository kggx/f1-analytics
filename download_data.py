import requests
import zipfile
import pathlib

# Download data
r = requests.get('https://ergast.com/downloads/f1db_csv.zip')
local_data = pathlib.Path('f1_data.zip')

if r.status_code == 200:
    with open(local_data, 'wb') as raw:
        raw.write(r.content)
        
    # Unzip file
    with zipfile.ZipFile(file=local_data) as zip:
        zip.extractall('./source')
        
        # Delete file
        if pathlib.Path(local_data).exists():
            local_data.unlink()
            
    