# Create new Dataset using Ckan API
# Project: Protect SLR
# JB Barré - 9/12/2020

from ckanapi import RemoteCKAN
import requests

session = requests.Session()
session.verify = False

# You must add your ckan API key in apikey='' and user_agent name

protect = RemoteCKAN('https://data-protect-slr.univ-grenoble-alpes.fr/',
    apikey='xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    user_agent='xxxxx',
    session=session)

# Mandatory parameters : 'name' and 'owner_org':
#   01_cnrs,02_ubremen,03_uzh,04_nioz,05_ukri-bas,06_gcf,07_brgm,08_pik,
#   09_uu,10_ulb,11_uleeds,12_ubris,13_dmi,14_vub,15_uliege,16_kcl,17_uswansea,
#   18_asiaq,19_ethz,20_unn,21_dtu,22_awi,23_me,24_tud,25_knmi,26_uea

#groups may be wp2,wp3,wp4wp,5,wp6 or wp7

dataset_dict = {
    'name':'dataset-15',
    'owner_org': '02_ubremen',
    'author':'',
    'groups':[{'name':'wp4'}],
    'notes': 'A long description of my dataset',
    'private': False
}

protect.action.package_create(**dataset_dict)

RemoteCKAN.close(protect)