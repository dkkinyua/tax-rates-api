# tax-rates-api
This is a repository for the Sales Tax API.

# Installing packages.

Install your packages and modules required in this project by running
```bash

pip install requirements.txt

```
# Endpoints.
This is a simple API with one endpoint. It fetches tax rate data from a .json file that is updated daily.

| Method | Route                 | Status       | Purpose                     |
|--------|-----------------------|--------------|-----------------------------|
| GET    | /                     | Not Protected| Home page                   |
| GET    | /api/taxrates?state={state}          | Get taxrates by state       |

# Parameters
There is one required parameter which is ```state```.
1. ```state``` - Required.
   Example: /api/taxrates?state={Florida}.
   Returns all the tax rates for Florida which are ```combined_rate```, ```average_rate```, ```state_rate```.
   Status code: 200 OK.
