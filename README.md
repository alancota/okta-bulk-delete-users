# Okta Preview: bulk deactivate and delete staged users
I came up with this script mostly to clean up preview tenants. At some point I had almost 12k users that I created from other tests and of course nobody got time to do it manually. So, Python to the rescue!

If you are like me and use the heck off of your tenant preview, this script might come in handy. I often have thousands and thousands of users after testing things and preparing some demo or POC. I'm just lazy and got no time to manually deleate one by one. This script does exactly that.

First of all, you need to be careful when using this script. I'm not responsible for any damage that it may cause. This is 100% on you. Also, I'm not a developer though I love to code from time to time. That said, any improvements are welcome and greatly appreciated :)

Before using it you are going to need an API token from your Okta preview. If you don't know how to get a token, please [click here](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/). Then remane the **constant.template** file to **constant.py** and add your Okta Tenant and as well created token information there. Do not change the PAYLOAD or HEADER constants unless you intend to change the code as well.

To run the script just open up your terminal and type:

```bash

python deleteStaged.py

```

Inside your **constant.py** file, you're going to find an USER_LIMIT variable. That can be helpful when testing it against your preview environment. You can limit it to 2 or 5 users while you test. However, the way this script was created, it will run while staged users are coming in the response. The limit means that the script will process only that amount of users in a loop. The limit of the Okta preview is 200 anyway.

Enjoy!
