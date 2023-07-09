# wg_updater

This is a quick-and-dirty Python script to periodically update a WG-Gesucht.de listing so it gets pushed to the top of all listings.

It utilizes selenium-webdriver and chromedriver to automate a Chrome/Chromium browser that runs in headless mode.

## dependencies

You'll need to install **selenium-webdriver** first:

```
pip install selenium
```

Then adjust the config at the beginning of the file and run the script

```
python flat_updater.py
```

