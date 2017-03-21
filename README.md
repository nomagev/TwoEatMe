# nomagev-twtt

A little experiment using git, Python and the Twitter API

# Premises

The following are a sequence of steps followed to prepare our system to be able to properly run-and-create the application. This may serve you in case you want to play with the code.

Usage of it relies on your own responsibility: it's not Rocket Science, but in case something goes wrong, you are fully responsible for the use of it (the intended usage of whatever I put in here is for my own personal use).

The code and the things contained within the repository (excluding content accessible through links) are offered under a [GPL 2.0 License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html): Sharing is caring.

# Dependencies

To run this code, you may need to have installed in your computer or have available to the following set of components:

  1. **Python:** you need to have Python installed. I am working with Python 2.X, so I am not sure on whether the code may work with Python 3.X.
  2. **Python pip:** you need to have Python pip installed. This normally may be available on your Python Installation. Otherwise, please check [the Python Pip Page](https://pypi.python.org/pypi/pip/).
  3. **Tweepy:** you need to have Tweepy Installed. Once [https://www.python.org](Python) and [Pip](https://pypi.python.org/pypi/pip/) are installed, go into your terminal and shell and run `pip install tweepy`.
  4. **Twitter Account** You may need a [Twitter Account](https://www.twitter.com).
  5. **Twitter App Credentials** You DEFINITELY need a [Twitter App](https://apps.twitter.com) to gain the required credentials any developer needs to build an app, including:
    - Twitter Consumer Key
    - Twitter Consumer Secret Key
    - Twitter Access Token
    - Twitter Access Token Secret

# Program

The program is hosted under the [code master folder](https://github.com/nomagev/nomagev-twtt/tree/master/code) on this repository (check 'hellotweepy.py').

You can run it on your terminal (do not forget to check the "Dependencies" on the section above) or your Command Prompt by copying your file on your local drive and, on the same folder, run 'python hellotweepy.py'.

# Current Status (as of March 20th 2017)

Current program is able to:
1. **Tweepy Library Check:** Check whether Tweepy Library is installed on your system.
2. **File containing Twitter Apps Check:** Check whether 'Keys-DO-NOT-COMMIT.txt' file exists.
  - If not, program will prompt you to enter your Twitter Apps Credentials and how to obtain them.
    - Program will then load them under 'Keys-DO-NOT-COMMIT.txt' file, so it won't ask you again about it.
  - If so, program will read your Twitter Apps keys
3. **Your Basic Twitter Information:** Display basic details on your Twitter Account
4. **Your Basic last Twitt Information:** Display basic details on your last published Twitt.