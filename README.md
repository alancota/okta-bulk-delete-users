# okta-bulk-delete-users
I came up with this script mostly to clean up preview tenants. At some point I had almost 12k users that I created from other tests and of course nobody got time to do it manually. So, Python to the rescue!

Full disclosure: I'm no developer and the code may not be the prettiest or best, but it's working :)

Feel free to change it to fit your needs and of course I'm no responsible for anything this script may cause in your environment. Use it with caution!

The way this is designed, just run deleteStaged.py and the script will run while there are any staged users available. In order to use the script, please go to the contant.py file and update it with your Okta preview information and API token.


Improvements are most appreciated.

