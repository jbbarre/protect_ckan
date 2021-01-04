## How to embed multiple zipped files into the Protect Data Portal.

### Step 1: Preparation
* First of all, the dataset to which you whish to add data must be created in the [Data Portal](https://data-protect-slr.univ-grenoble-alpes.fr/).
* You need to know your login and api key from you data portal account. You may grab them in the user account page of the data portal.
* The files must be be zipped into a 7-zip file. 
* For a stable and efficient internet connection, the 7-zip file may be located on your computer (remote upload). Otherwise, the 7-zip file must be uploaded using ssh access into the data server before being embedded in the data portal. A user may upload files into `/data/ckan/storage/YourInstitution/`. If you need more info, please send a request to <data@protect-slr.eu>


### Step 2: upload_zipfiles.py
In the py file, modify:
* the `user_agent` (login) and `api_key`.
* the file path and file name of the 7-zipfile.
* the `package_id` id of package that the resource should be added to. `format` and `name` fields are filled in automatically. Optionally, you may add:
  * description (string)
  * hash (string)
  * name (string)
  * resource_type (string)
  * mimetype (string) 
  * mimetype_inner (string)
  * cache_url (string)
  * size (int)
  * created (iso date string)
  * last_modified (iso date string)
  * cache_last_updated (iso date string)
  * url (string) – url of resource

### Step 3:
Execute the code: `python3 upload_zipfiles.py`