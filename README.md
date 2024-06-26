# Twitter API Tester

This repository contains a simple Python script to test Twitter API authentication and posting capabilities. It's designed to help developers navigate Twitter's API authentication process and verify their setup before embarking on larger Twitter automation projects.

## Table of Contents

1. [Why This Project Exists](#why-this-project-exists)
2. [Twitter Developer Portal Setup](#twitter-developer-portal-setup)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Troubleshooting](#troubleshooting)
6. [License](#license)

## Why This Project Exists

Twitter's Developer Portal can be confusing, especially if you're just looking to automate personal tweets. This project aims to simplify the process of testing your Twitter API authentication and posting capabilities. It's useful for:

- Verifying your Twitter API credentials are set up correctly
- Testing if your authentication is working before starting a larger project
- Quickly diagnosing issues if your existing Twitter automation breaks
- Staying up-to-date with any changes Twitter makes to their API

A key point to note is that Twitter requires setting up OAuth 2.0 authentication first, even if you're using OAuth 1.0a for posting tweets. This script helps you navigate this quirk and ensure everything is working as expected.

Why not use OAuth 2.0? Because the setup is more complicated and its unnecesary for just posting personal tweets. Oauth1.0a works fine for that and is a breeze to setup.

## Twitter Developer Portal Setup

1. Go to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and sign up for a developer account if you haven't already.

2. Create a new project and app in the developer portal. If you already have a default project and app set up, you can skip this step. At this point you can create Oauth1.0a credentials but they won't work.

3. Set up OAuth 2.0 authentication first:
   - Navigate to your app's settings
   - In the "User authentication settings" section, click "Set up"
   - Notice it says "These permissions enable OAuth 1.0a Authentication"
   - Set the app permissions to "Read and write"
   - In Type of App select Web App, Automated App or Bot
   - Set the callback URL and website URL (these can be placeholder URLs if you're just testing)
   - Save your changes

4. After setting up OAuth 2.0, you'll be able to use OAuth 1.0a credentials:
   - Go to the "Keys and tokens" tab
   - You'll see your API Key and API Key Secret (also known as Consumer Key and Consumer Secret)
   - Generate your Access Token and Access Token Secret
   - You don't need the bearer token for this script

5. Keep these four credentials handy, you'll need them for the script.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/esoteric-git/twitter-api-tester.git
   cd twitter-api-tester
   ```

2. Install the required Python package:
   ```
   pip install tweepy
   ```

## Usage

1. Open the `twitter_api_tester.py` file in your preferred text editor.

2. Replace the placeholder credentials with your own:
   ```python
   consumer_key = "your_consumer_key"
   consumer_secret = "your_consumer_secret"
   access_token = "your_access_token"
   access_token_secret = "your_access_token_secret"
   ```

3. (Optional) Modify the `tweet_text` variable if you want to change the content of the test tweet.

4. Run the script:
   ```
   python twitter_api_tester.py
   ```

5. If everything is set up correctly, you should see a message indicating that the tweet was posted successfully, along with the Tweet ID.

## Troubleshooting

If you encounter any errors, here are some common issues and solutions:

- "Invalid or expired token": Double-check your OAuth 1.0a credentials (consumer key, consumer secret, access token, access token secret).
- "Could not authenticate you": Ensure you've set up OAuth 2.0 in the developer portal before trying to use OAuth 1.0a.
- "App not authorized": Make sure you've given your app the necessary permissions (read and write) in the developer portal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
