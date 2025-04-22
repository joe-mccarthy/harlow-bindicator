# Harlow Bindicator

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/joe-mccarthy/harlow-bindicator/build-test.yml?cacheSeconds=1&style=for-the-badge)
![Coveralls](https://img.shields.io/coverallsCoverage/github/joe-mccarthy/harlow-bindicator?cacheSeconds=1&style=for-the-badge)
![Sonar Quality Gate](https://img.shields.io/sonar/quality_gate/joe-mccarthy_harlow-bindicator?server=https%3A%2F%2Fsonarcloud.io&cacheSeconds=1&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/harlow-bindicator?style=for-the-badge&link=https%3A%2F%2Fpypi.org%2Fproject%2Fharlow-bindicator%2F)
![GitHub License](https://img.shields.io/github/license/joe-mccarthy/harlow-bindicator?cacheSeconds=1&style=for-the-badge)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [PyPI Installation](#pypi-installation)
  - [Manual Installation](#manual-installation)
- [Configuration](#configuration)
  - [Required Parameters](#required-parameters)
- [Usage](#usage)
  - [Running as a GitHub Action](#running-as-a-github-action)
  - [Running Locally](#running-locally)
  - [Command Line Options](#command-line-options)
  - [Scheduling with Cron](#scheduling-with-cron)
- [Examples](#examples)
- [Notification Format](#notification-format)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Harlow Bindicator is an automated tool that helps Harlow residents stay informed about their bin collection schedules. The application scrapes the Harlow Local Authority website to retrieve bin collection dates for a specified property and sends timely notifications through ntfy.sh when bins need to be put out. Never miss bin day again!

A "bindicator" is a notification system for bin collection days - the name is a blend of "bin" and "indicator."

## Features

- Automatically retrieves bin collection dates from the Harlow Local Authority website
- Sends notifications when bins need to be put out
- Specifies which bin type needs collection (recycling, general waste)
- Can be run locally or as a GitHub Action
- Easy setup and configuration
- Customizable notification options
- Cross-platform compatibility

## Installation

### Prerequisites

- Python 3.7 or higher
- Chromedriver (for web scraping)
- Internet connection
- A UPRN (Unique Property Reference Number) for your address
- A ntfy.sh topic for notifications

### PyPI Installation

The easiest way to install Harlow Bindicator is via pip:

```bash
pip install harlow-bindicator
```

### Manual Installation

If you prefer to install from source:

```bash
git clone https://github.com/joe-mccarthy/harlow-bindicator.git
cd harlow-bindicator
pip install -e .
```

### Platform-Specific Dependencies

#### Debian/Ubuntu
```bash
sudo apt-get install chromium-chromedriver
```

#### macOS
```bash
brew install --cask chromedriver
```

#### Windows
Download ChromeDriver from https://chromedriver.chromium.org/downloads and add it to your PATH.

## Configuration

### Required Parameters

- **UPRN**: Unique Property Reference Number that identifies your property. You can find your UPRN at [Find My Address](https://www.findmyaddress.co.uk/search).
- **ntfy.sh Topic**: Create a unique topic name at [ntfy.sh](https://ntfy.sh/) to receive notifications.

## Usage

### Running as a GitHub Action

There's a workflow file in this repository, [check-binday.yml](https://github.com/joe-mccarthy/harlow-bindicator/blob/main/.github/workflows/check-binday.yml), which is scheduled to run early each morning to check for bin collections. 

To use this workflow:

1. Fork this repository
2. Add two repository secrets in your GitHub settings:
   - `UPRN`: Your property's Unique Property Reference Number
   - `NTFY_TOPIC`: Your ntfy.sh topic name
3. Enable GitHub Actions for your repository

The workflow will run automatically according to the schedule defined in the workflow file.

### Running Locally

After installation, you can run Harlow Bindicator from the command line:

```bash
harlow-bindicator --uprn "12345678" --topic "your-topic-name"
```

### Command Line Options

```
harlow-bindicator [OPTIONS]

Options:
  --uprn TEXT         UPRN for the property to check [required]
  --topic TEXT        ntfy.sh topic to publish notifications to [required]
```

### Scheduling with Cron

To run automatically on Linux/macOS, add a cron job:

```bash
# Edit crontab
crontab -e

# Add this line to run at 7:00 AM every day
0 7 * * * /usr/local/bin/harlow-bindicator --uprn "12345678" --topic "your-topic-name"
```

## Examples

### Basic Usage
```bash
harlow-bindicator --uprn "12345678" --topic "bin-notifications"
```

## Notification Format

When a bin collection is detected, you will receive a notification via ntfy.sh with:

- Title: "Bin Collection Tomorrow: [Bin Type]"
- Message: Information about which bin(s) need to be put out
- Priority: Default (adjustable in future versions)

Example notification:
> **Bin Collection Tomorrow: Recycling**
>
> Please put out your Blue Recycling bin tonight for collection tomorrow.

## Troubleshooting

### Common Issues

1. **ChromeDriver Error**: 
   - Make sure ChromeDriver is installed and in your PATH
   - Check if the ChromeDriver version matches your Chrome version

2. **No Notifications Received**:
   - Verify your ntfy.sh topic is correct
   - Check if you're subscribed to the topic in ntfy.sh
   - Ensure your internet connection is stable

3. **UPRN Not Working**:
   - Double-check your UPRN is correct
   - Verify your property is within the Harlow Local Authority area

## FAQ

**Q: What is a UPRN?**  
A: A Unique Property Reference Number (UPRN) is a unique identifier for addressable locations in the UK. You can find yours at [Find My Address](https://www.findmyaddress.co.uk/search).

**Q: What is ntfy.sh?**  
A: ntfy.sh is a free, simple HTTP-based publish-subscribe notification service. It allows you to send notifications to your phone or desktop without setting up any accounts.

**Q: How do I receive the notifications?**  
A: Download the ntfy app ([Android](https://play.google.com/store/apps/details?id=io.heckel.ntfy), [iOS](https://apps.apple.com/us/app/ntfy/id1625396347)), or use the [web interface](https://ntfy.sh/). Subscribe to your topic name.

**Q: Does this work for areas outside Harlow?**  
A: No, this tool is specifically designed for the Harlow Local Authority website. Fork the project to adapt it for other regions.

**Q: How accurate are the notifications?**  
A: The tool scrapes the official Harlow Council website, so the notifications are as accurate as the data provided by the council.

## Architecture

Harlow Bindicator works by:

1. Using ChromeDriver to open a headless browser session
2. Navigating to the Harlow Council bin collection page
3. Submitting the UPRN to retrieve collection information
4. Parsing the returned data for upcoming collections
5. Determining if a notification is needed based on the collection dates
6. Sending a notification via ntfy.sh if a collection is scheduled within the specified timeframe

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [ntfy.sh](https://ntfy.sh/) for providing a simple notification service
- [Selenium](https://www.selenium.dev/) for web automation
- [Harlow Council](https://www.harlow.gov.uk/) for providing the bin collection data
- All contributors who have helped improve this project
