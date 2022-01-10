# Minecraft-Server-Status-Check
Minecraft Server Status Check

Simple python script using `mcstatus` to monitor your servers activity.
The script has been deployed to a free tier AWS EC2 instance where it runs every X minutes (cronjob).

## Libriaries/Frameworks used

1. [mcstatus](https://github.com/Dinnerbone/mcstatus)
    - `pip install mcstatus`
2. [Crontab](https://pypi.org/project/python-crontab/)
    - `pip install python-crontab`

## Configuring you parameters

First open `cfg.json` and edit it for your needs.

The `"server_ip"` parameter is for configuring your server ip that you want to inspect.

The `"sender_email_address"` , `"sender_password"` can be left as is.

## Adding cronjobs

Run `crontab -e` in your terminal 

Run `crontab -l` in your terminal to check if they have been added.

Run `crontab -r` to remove all cronjobs from your crontab