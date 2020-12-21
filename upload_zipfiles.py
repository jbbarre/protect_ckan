# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Upload data/ressource to an existing Dataset
# Create new Dataset using Ckan API
# Project: Protect SLR - JB Barré - 9/12/2020
# 

# %%
from ckanapi import RemoteCKAN
import requests
from urllib.request import urlopen
from py7zr import SevenZipFile
import os

session = requests.Session()
session.verify = False

protect = RemoteCKAN('https://data-protect-slr.univ-grenoble-alpes.fr/',
    apikey='xxxxxxxxxxxxxxxxxx',
    user_agent='xxxxxxxxxxxx',
    session=session)

# ## Specify the zip file path + explore and get the files to upload

# %%
zip_path = '/data/ckan/storage/CNRS/'
zip_name = 'data_1go.7z'

# # Parameters: 
# - package_id (string) – id of package that the resource should be added to.
# - url (string) – url of resource

### Optionals:
# 
# - description (string)
# - format (string)
# - hash (string)
# - name (string)
# - resource_type (string)
# - mimetype (string) – 
# - mimetype_inner (string) – 
# - cache_url (string) – 
# - size (int) – 
# - created (iso date string) – 
# - last_modified (iso date string) – 
# - cache_last_updated (iso date string) – 
# - upload (FieldStorage  needs multipart/form-data) – 

 
with SevenZipFile(zip_path+zip_name,'r') as myzip:
    zipped_files = myzip.getnames()
    print("Files to Upload:",zipped_files)
    for fichier in zipped_files:
        filename, file_extension = os.path.splitext(zip_path+fichier)
        ressource_dict = {
            'package_id':'dataset_5',
            'upload': open(zip_path+fichier,'rb'), #for local file
            'name': fichier,
            'description':'1 Go upload with 7zip',
            'format':file_extension.replace('.',''),
            'notes': 'A long description of my dataset',
            'url ':''
        }

        import_res = protect.action.resource_create(**ressource_dict)
        print(import_res["name"] + " Uploaded...")
        

RemoteCKAN.close(protect)


