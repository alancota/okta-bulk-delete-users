import constant
import requests
import json
import ast

# Function to check the number of staged users
def stagedUsers():
    whatToReturn = -1
    response = requests.request("GET", constant.FILTER_API, headers=constant.HEADERS, data = constant.PAYLOAD)
    users = response.json()
    if len(users) > 0:
        whatToReturn = users
    return whatToReturn
            

# Function to deactivate an User
def deactivateUser(userID):
    url = constant.OKTA_API_ENDPOINT + '/' + userID +'/lifecycle/deactivate'
    resp = requests.request("POST", url, headers=constant.HEADERS, data = constant.PAYLOAD)
    if resp.status_code == 200:
        # Call function to delete user
        deleteUser(userID)
    # This function doesn't return anything
    return

def deleteUser(userID):
    url = constant.OKTA_API_ENDPOINT + '/' + userID
    requests.request("DELETE", url, headers=constant.HEADERS, data = constant.PAYLOAD)
    #print("Deleted user " + userID)
    return


# Main
def main():
    processed = 0
    loopNumber = 0
    totalUsers = len(stagedUsers())
    while totalUsers != -1:
        loopNumber += 1
        print("Starting the loop: ["+str(loopNumber)+"]\n")
        processed = processed+totalUsers
        for user in stagedUsers():
            print("Processing "+user['id'])
            deactivateUser(user['id'])
        
        totalUsers = len(stagedUsers())
        print("\nFound more " + str(totalUsers)+ ", restarting the loop...")
        print("----------\n")
    else:
     print("End of loop: " + str(processed)+" users deleted")

if __name__ == '__main__':
    main()