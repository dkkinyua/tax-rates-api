# tax-rates-api
This is a repository for the Sales Tax API.

### Website URL
**Website URL**: [tax-rates-api.onrender.com](https://tax-rates-api.onrender.com)

### Features
- Retrieve state-specific sales tax rates.
- Access average local and combined rates.
- Lightweight and easy to integrate into any project requiring U.S. tax information.

# Installing packages.

Install your packages and modules required in this project by running
```bash

pip install requirements.txt

```
# Endpoints.
This is a simple API with one endpoint. It fetches tax rate data from a .json file that is updated daily.

| Method | Route                 |Purpose                                     |
|--------|-----------------------|--------------------------------------------|
| GET    | /                     |       Home page                             |
| GET    | /api/taxrates?state={state}| Get taxrates by state                 |

# Parameters.
There is one required parameter which is ```state```.
1. ```state``` - Required.
   Example: /api/taxrates?state={Florida}.
   Returns all the tax rates for Florida which are ```combined_rate```, ```average_rate```, ```state_rate```.
   Status code: 200 OK.

# Errors and Rate Limits.
In this project, ```django-ratelimit``` has been used to limit the rate of GET requests for a user based on their IP addresses and limited to 20 requests per minute(20/m). 
To install ```django-ratelimit``` run the following command in your terminal:

```bash

pip install django-ratelimit

```

The code snippet below shows the amount of requests per minute per user, limited to a user's IP address by the use of the ```ratelimit``` decorator imported from ```django_ratelimit.decorators```.

```python

@ratelimit(key='ip', rate='20/m', block=True)
@api_view(['GET'])
def get_tax_rates(request):
    # Logic here

```

Parameters for ```@ratelimit```:
    1. ```key```: This param is used to determine what will identify the user, in this case, I used the user's IP address.
    2. ```rate```: The max amount of requests allowed per user per minute
    3. ```block=True```: This block the user's IP after exceeding 20 requests per minute, and a ```429 Too Many Requests``` error will appear.

**Errors:**
    1.  ```429 Too Many Requests```: This error appears when the user has exceeded 20 requests per minute
    2. ```500 Internal Server Error```: There is an error with the server, might be a minor maintenance.
    3. ```400 Bad Request```: Shows that the user might have used the wrong params, entered an invalid state or the state doesn't exist.

**Areas to work on later:**
This API has been used for a project of mine becuase I didn't want to pay $15 for a sales tax API. There is a lot of things to be worked on. They are:
    1. **Authentication**: Users should be authenticated or logged in so as to send requests to the server
    2. **Subscriptions**: Adding a subscription feature to bill users monthly for using the API for their projects. A small charge will do, probably $2.99/month or $3.99/month.
    3. **Security measures**: Adding secure connections such as HTTPS to prevent attacks.

**Feel free to contact me if you would want to collaborate on this project!**