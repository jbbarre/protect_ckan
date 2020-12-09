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

# method GET

#groups = protect.action.group_list()
#print (groups)

#org = protect.action.organization_list()
#print (org)

#users = protect.action.user_list()
#print (users)


# Method CREATE

#protect.action.group_create(name = "wp2", description = "Co-design and co-production of sea level projections and coastal climate services")
#protect.action.group_create(name = "wp3", description = "Process understanding and model improvement")
#protect.action.group_create(name = "wp4", description = "Contribution of the Antarctic Ice Sheet to SLR")
#protect.action.group_create(name = "wp5", description = "Contribution of the Greenland Ice Sheet to SLR")
#protect.action.group_create(name = "wp6", description = "Contribution of glaciers to SLR")
#protect.action.group_create(name = "wp7", description = "Regional sea-level change and implications")

groups = protect.action.group_list()
print (groups)


RemoteCKAN.close(protect)