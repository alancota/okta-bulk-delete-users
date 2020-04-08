# okta-bulk-delete-users
I came up with this script mostly to clean up preview tenants. At some point I had almost 12k users that I created from other tests and of course nobody got time to do it manually. So, Python to the rescue!

Full disclosure: I'm no developer and the code may not be the prettiest or best, but it's working :)

Feel free to change it to fit your needs and of course I'm no responsible for anything this script may cause in your environment. Use it with caution!

The way this is designed, just run **deleteStaged.py** and the script will run while there are any staged users available. In order to use the script, you need to rename the file **constant.template** to **constant.py** and update it with your Okta preview information and API token. Check out [this link](https://support.okta.com/help/s/article/How-do-I-create-an-API-token) in case you don't know how to create an API token in your Okta dashboard.

To run the script just open up your terminal and type:

```bash
python deleteStaged.py
```
**!! And remember that the script will enter in a loop while there are staged users. You can always stop the loop by pressing CTRL + X of course. !!**

Improvements are welcome and greatly appreciated.

