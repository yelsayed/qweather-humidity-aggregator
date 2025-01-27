## Intro

This small program uses data that is provided by the Qatari weather forcast to find the area and time with the highest
humidity in the next three days.

![image](https://github.com/user-attachments/assets/7f9011a8-c723-442a-9b88-6b6fe1dec4e4)

### How to run

Make sure you have Python 3.12 installed on your computer. You can go to [this link](https://www.python.org/downloads/) to install it on your machine.

Once installed, open your terminal or command line and run the following.

```
$ python -m venv ./env
$ source env/bin/activate
$ pip install -r requirements.txt
```

These three commands will install the necessary code to run the program.

Now what's left is to run the program!

```
$ python main.py
```

### Known issues

This program relies on `qweather.gov.qa` for it's data. If `qweather.gov.qa` is down for any reason then this program will fail to run.

### Additional Work

- Filter out dates in the past + add a grace period.
- Report errors in case data is not available.
