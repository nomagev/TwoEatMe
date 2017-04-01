# TwoEatMe.py

"TwoEatMe" is a little experiment to create a Twitter, text-based client, using git, Python and Python's [Tweepy library](https://github.com/tweepy/tweepy) to handle Twitter's API. 

# Premises

The following are a sequence of steps followed to prepare our system to be able to properly run-and-create TwoEatMe. This may serve you in case you want to play with the code.

Usage of it relies on your own responsibility: it's not Rocket Science, but in case something goes wrong, you are fully responsible for the use of it (the intended usage of whatever I put in here is for my own personal use).

Please [report bugs here](https://github.com/nomagev/twoeat/issues) if you find one.

The code and the things contained within the repository (excluding content accessible through links) are offered under a [GPL 2.0 License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html): Sharing is caring.

# Dependencies

To run this code, you may need to have installed in your computer or have available to the following set of components:

  1. **Python:** you need to have Python installed. I am working with Python 2.X, so I am not sure on whether the code may work with Python 3.X.
  2. **Python pip:** you need to have Python pip installed. This normally may be available on your Python Installation. Otherwise, please check [the Python Pip Page](https://pypi.python.org/pypi/pip/).
  3. **Tweepy:** you need to have Tweepy Installed. Once [Python](https://www.python.org) and [Pip](https://pypi.python.org/pypi/pip/) are installed, go into your terminal and shell and run `pip install tweepy`.
  4. **Twitter Account** You may need a [Twitter Account](https://www.twitter.com).
  5. **Twitter App Credentials** You DEFINITELY need a [Twitter App](https://apps.twitter.com) to gain the required credentials any developer needs to build an app, including:
    - Twitter Consumer Key
    - Twitter Consumer Secret Key
    - Twitter Access Token
    - Twitter Access Token Secret

# Program

The program is hosted under the [master folder](https://github.com/nomagev/twoeat/) on this repository (check 'TwoEatMe.py').

You can run it on your terminal (do not forget to check the "Dependencies" on the section above) or your Command Prompt by copying your file on your local drive and, on the same folder, run 'python TwoEatMe.py'.

# Current Status (as of March 29th 2017)

Current program is able to:
1. **Tweepy Library Check:** Program checks whether Tweepy Library is installed on your system.
2. **OS Check:** Program checks which OS are you using (Windows, macOS or Linux). 
3. **File containing Twitter Apps Check:**  Program checks whether 'Keys-DO-NOT-COMMIT.txt' file (containing user keys and tokens necessary to run the tool) exists.

  - If not, program will prompt you to enter your Twitter Apps Credentials and how to obtain them.
    - Program will then load them under 'Keys-DO-NOT-COMMIT.txt' file, so it won't ask you again about it.
  - If so, program will read your Twitter Apps keys

4. **TwoEatMe Options Menu**: the program displays a menu with some Twitter options you can trigger, including:

  - **Your Basic Twitter Information:** Display basic details on your Twitter Account.
  - **Your Additional Twitter Information:** Display additional details on your Twitter Account you may not be aware of.
  - **Your last Tweet's Basic Information:** Display basic details on your last published Tweet.
  - **Your last Tweet's Additional Information:** Display additional details on your last published Tweet you may not be aware of.
  - **The last 10 Tweets you received:** Display the last 10 Public tweets you may have received on your Twitter Timeline.
  - **The last 10 Tweets you sent:** Display the last 10 Public tweets you may have sent on Twitter.
  - **Send Tweets:** You are now able to send tweets from your Twitter Account (using your own [Twitter Apps Credentials](https://apps.twitter.com).
  - **Check Global Trends:** Display Twitter Global Trending Topics.

5. **Program Options Menu**: the program displays a couple of internal options you can trigger, including: 
  - **Clear the Screen:** The option will clear the text already displayed in the screen.
  - **Quit the Application:** The option will instruction the program to succesfully quit and go back to the command prompt on your shell.

# Road map

__[master branch](https://github.com/nomagev/TwoEatMe)__

- [x] Dependencies checks (tweepy library, chcp, API keys)
- [x] Display Menu with options:
  - [x] Send a Tweet.
  - [x] Display Twitter Global Trends
  - [x] Display Basic / Advanced Details on the last Tweet you sent.
  - [x] Display last 10 Tweets you Received / Sent
  - [x] Display Basic / Advanced Details on you at Twitter.
  - [x] Clear Screen / Quit the Program

__[next-release branch](https://github.com/nomagev/TwoEatMe/tree/next-release)__

- [ ] Review and Improve Code Quality

__Future: [See Issues Page](https://github.com/nomagev/TwoEatMe/issues)__

- [ ] Enter **YOUR** idea or request in [the issues area](https://github.com/nomagev/TwoEatMe/issues).
