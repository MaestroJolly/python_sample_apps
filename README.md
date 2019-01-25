# Rave Python Sample Apps

This is a Django project consisting of sample apps used to handle various transactions such as Split Payment, Subaccount, Preauth, Transfer, Tokenized Charge, 3DSecure and Redirect Url, Webhooks.

You can get your Rave Test/Sandbox Public and Secret Keys [Here](https://ravesandbox.flutterwave.com/dashboard/settings/apis).

## Sample Apps

- Split Payment
- Subaccount
- Preauth
- Transfer
- Tokenized Charge
- 3DSecure and Redirect Url
- Webhooks(Logging to database)

## Prerequisites

- Python
- Django
- Virtual Environment

## How To Set It Up

- Create a virtual environment for your Django project. You can check this links: [virtualenv](https://virtualenv.pypa.io/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) to set it up.
- activate the virtual environment you created.
- cd into the directory in which you would like to run the project.
- pip install -e django
- git clone https://github.com/MaestroJolly/python_sample_apps.git
- cd into python_sample_apps
- pip install -r requirements.txt
- Find `.env-example` file in the cloned directory, edit it and replace the `RAVE_PUBLIC_KEY` and `RAVE_SECRET_KEY` with the one from your [Rave](https://ravesandbox.flutterwave.com/dashboard/settings/apis) Sandbox Dashboard.
- Save it as `.env`, then source using `source .env from bash terminal` or `set .env from Windows Command Prompt/PowerShell Terminal.`
- To start the project locally, run `py manage.py runserver` to start the server.
- Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to load the apps on your browser.

## Setting Up Webhooks Locally

- Visit [ngrok](https://ngrok.com/) to signup for an `ngrok` account.
- Download `ngrok` for your current OS [here](https://ngrok.com/download), install it and make it available globally.
- To make it available globally on Windows, Extract the download `ngrok.zip` file to your preferred path. 
- Hit the `Windows + R` buttons simultaneously, Enter this into the input `sysdm.cpl` and press enter.
- Select the Advanced Option, Open the environment variable option, Select the `PATH` variable name, Click Edit, Click New, Then copy the path of the extracted `ngrok` file and paste it there.
- Click ok to save it.
- Go to your `ngrok` dashboard to get your `auth token`.
- Open a new terminal window, cd into the cloned sample apps directory then enter this command `ngrok authtoken <YOUR_AUTH_TOKEN>` change the `<YOUR_AUTH_TOKEN>` to the `auth token` from your dashboard.
- Next enter this command to start your auth server `ngrok http <PROJECT_SERVER_PORT_NUMBER>` say `ngrok http 8000`.
- Now you should see generated `urls` similar to this `http://a5e2530f.ngrok.io` and `https://a5e2530f.ngrok.io`, copy any of them and go to the webhooks [setting](https://ravesandbox.flutterwave.com/dashboard/settings/webhooks) on your rave dashboard.
- Paste the `url` you copied to the webhook input field and add your `webhook` path to it which should look similar to this `http://a5e2530f.ngrok.io/webhook`, then hit save button.
- Your webhook url is now listening for events/requests, `Rave` sends webhook requests for `card`, `account`, `ghana mobile money`, `uganda mobile money` successful transactions and `transfers`, check [here](https://developer.flutterwave.com/reference#webhooks) to understand more.
- Whenever the webhook is triggered the requests is logged to the database, you can find all the logged webhook requests at this [url](http://127.0.0.1:8000/webhook/logs/).


## Contributors

- [Anjola Bassey](https://github.com/anjolabassey/)

