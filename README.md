# URLFilteringTester
Simple script to run on endpoint to test Secure Web Gateway URL filtering capabilities.

To get started run the script as a cron job.

Update Crontab with the following job - runs every 15mins:

```
crontab -e
```
```
*/15 * * * * (cd ~/URLFilteringTester; /usr/bin/python3 fetch_urls.py)
```
