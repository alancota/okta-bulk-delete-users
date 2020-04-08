PAYLOAD = {}
HEADERS = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'SSWS 00e5vNSqGlvyy_AcYjLWNtXlGJ4t-j1ev9vA-MMeG6'
}
OKTA_ORG = "https://jediacademy.oktapreview.com"
OKTA_API_ENDPOINT = "/api/v1/users"
USERS_LIMIT="&limit=1000"
FILTER_API = OKTA_ORG + OKTA_API_ENDPOINT + "?filter=status eq \"STAGED\""+USERS_LIMIT
DEACTIVATE_API = OKTA_ORG + OKTA_API_ENDPOINT + OKTA_API_ENDPOINT