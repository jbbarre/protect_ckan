# Create new Dataset using Ckan API
# Project: Protect SLR
# JB Barré - 9/12/2020



from ckanapi import RemoteCKAN
import requests

session = requests.Session()
session.verify = False

protect = RemoteCKAN('https://data-protect-slr.univ-grenoble-alpes.fr/',
    apikey='xxxxxxxx',
    user_agent='xxxxxxxxxxxxx',
    session=session)


# Parameters: Id (name or Id)
id = "dataset_8"

# Purging a dataset cannot be undone!
protect.action.dataset_purge(id = id)

# or use the function package_delete to put the package in the trash
# protect.action.package_delete(id = id)

RemoteCKAN.close(protect)


