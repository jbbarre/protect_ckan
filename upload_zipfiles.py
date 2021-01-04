# Upload data/ressource to an existing Dataset
# Project: Protect SLR - JB Barré - 9/12/2020

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

# Specify the zip file path + explore and get the files to upload

zip_path = '/data/ckan/storage/CNRS/'
zip_name = 'data_1go.7z'
 
# Check the metadata of the uploaded file 
with SevenZipFile(zip_path+zip_name,'r') as myzip:
    zipped_files = myzip.getnames()
    print("Files to Upload:",zipped_files)
    for fichier in zipped_files:
        filename, file_extension = os.path.splitext(zip_path+fichier)
        ressource_dict = {
            'package_id':'dataset_5',
            'upload': open(zip_path+fichier,'rb'), # for local file
            'name': fichier,
            'format':file_extension.replace('.',''),
            'description':'Upload with 7-zip file',
            'notes': 'A long description of my dataset',
            'url ':''
        }

        import_res = protect.action.resource_create(**ressource_dict)
        print(import_res["name"] + " Uploaded...")
        
RemoteCKAN.close(protect)


