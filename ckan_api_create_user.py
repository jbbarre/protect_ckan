from ckanapi import RemoteCKAN
import requests

session = requests.Session()
session.verify = False

# You must add your ckan API key in apikey='' and user_agent name

protect = RemoteCKAN('https://data-protect-slr.univ-grenoble-alpes.fr/',
    apikey='xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    user_agent='xxxxx',
    session=session)


protect.action.user_create(name = "xxxx", password = "xxxx", email = "xxx", fullname = "xxx")

# Close connection
RemoteCKAN.close(protect)

# Todo

# create API key : ckan.logic.action.update.user_generate_apikey(context, data_dict)
# Make a user a member of an organization
#   ckan.logic.action.create.organization_member_create(context, data_dict)

'''Parameters:	
id (string) – the id or name of the organization
username (string) – name or id of the user to be made member of the organization
role (string) – role of the user in the organization. One of member, editor, or admin'''