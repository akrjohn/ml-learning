"""
Simple script to delete customers from finicity.
Make sure to change parameters as needed and change customer limit to a sutaible limit while deleting.
"""
import requests
import json
url = "https://api.finicity.com/aggregation/v2/partners/authentication"
customer_url = "https://api.finicity.com/aggregation/v1/customers"
customer_limit = 1
app_key = "7bd50447b9d78731d9305839bededede"
app_token = "vgwqTmcH98X4dYfPq3A8"
partner_id = "2445582611507"
partner_secret = "KjE0TPc5UHSwWTpnqR13"

customer_header = {
    'Content-Type': "application/json",
    'Finicity-App-Key': app_key,
    'Accept': "application/json",
    'Finicity-App-Token': app_token,
    'type': "testing",
    'limit': "100",
    'Cache-Control': "no-cache",
    }

payload = '{"partnerId": "'+partner_id+'", "partnerSecret": "'+partner_secret+'"}'

headers = {
    'Content-Type': "application/json",
    'Finicity-App-Key': app_key,
    'Accept': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
json_data = json.loads(response.text)
token = json_data.get('token')

if token is not None:
    customer_header['Finicity-App-Token']=token
    response_users = requests.request("GET", customer_url+'?limit='+str(customer_limit), headers=customer_header)
    user_data = json.loads(response_users.text)
    isMoreAvailable = user_data.get('moreAvailable')
    total_users = user_data.get('found')
    print("Total customers :" +str(total_users))
    #print(response_users.text)
    customers = user_data.get('customers');
    if customers is not None:
        for c in customers:
            print('Delete customer with ID: '+c.get('id'))
            cc = requests.request("DELETE", customer_url+'/'+c.get('id'), headers=customer_header)
            print(cc.status_code)
