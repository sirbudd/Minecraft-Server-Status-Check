# Minecraft-Server-Status-Check
Minecraft Server Status Check

## Libriaries/Frameworks used

1. [mcstatus](https://github.com/Dinnerbone/mcstatus)
    - `pip install mcstatus`
2. [Crontab](https://pypi.org/project/python-crontab/)
    - `pip install python-crontab`

## Configuring you parameters

### The app is in main-app

First open `cfg.json` and edit it for your needs.

The `"server_ip"` parameter is for configuring your server ip that you want to inspect.

The `"sender_email_address"` , `"sender_password"` can be left as is.

## Running the app



## Adding cronjobs

If you want to add those 2 python scripts to your crontab run `cronjob.py`.

Run `crontab -l` in your terminal to check if they have been added.

Run `crontab -r` to remove all cronjobs from your crontab