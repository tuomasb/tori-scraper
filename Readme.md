# Simple tori.fi scraper
This is a simple tori.fi scraper with web push notifications because their own watch functionality is pretty bad.
Default 1 request every 60 seconds can be changed in source. Might get rate limited by Cloudfront if using faster intervals.

## Installing (with virtual env)
- (optional) python -m venv .env
- (optional) source .env/bin/activate
- pip install -r requirements.txt
- notify_run register
- python scraper.py
- or screen -d -m python scraper.py
