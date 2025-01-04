# Harlow Bindicator

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/joe-mccarthy/harlow-bindicator/build-test.yml?cacheSeconds=1&style=for-the-badge)
![Coveralls](https://img.shields.io/coverallsCoverage/github/joe-mccarthy/harlow-bindicator?cacheSeconds=1&style=for-the-badge)
![Sonar Quality Gate](https://img.shields.io/sonar/quality_gate/joe-mccarthy_harlow-bindicator?server=https%3A%2F%2Fsonarcloud.io&cacheSeconds=1&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/harlow-bindicator?style=for-the-badge&link=https%3A%2F%2Fpypi.org%2Fproject%2Fharlow-bindicator%2F)
![GitHub License](https://img.shields.io/github/license/joe-mccarthy/harlow-bindicator?cacheSeconds=1&style=for-the-badge)

Script when run goes the the Harlow Local Authority website collects the bin collection dates for a given __UPRN__ then sends a notification to __ntfy.sh__ if required. This script can either be run locally or as with this repository as a GitHub action.

## Running Harlow Bindicator

This script can be run two ways either as a stand alone script that's scheduled using a cron job or as with this Repository a GitHub Action.

### Running as a GitHub Action

There is a workflow within this repository [check-binday.yaml](https://github.com/joe-mccarthy/harlow-bindicator/blob/main/.github/workflows/check-binday.yml) which is scheduled for early morning each day to check for bin collections. This workflow requires two secrets, firsly the [UPRN](https://www.findmyaddress.co.uk/search) to be checked for, and the [ntfy.sh](https://ntfy.sh/) topic to publish the message to. Then you'll start recieving notifications when you'll need to put bins out and which bin it is.

### Running locally

The script requires additional tools to run, in order to load the webpage that provides the bin information from Harlow Local Authority which is the chromium-chromedriver, just run the command below.

```bash
sudo apt-get install chromium-chromedriver
```

Install Harlow Bindicator

```
pip install harlow-bindicator
```

The set up is very similar to how it's run on GitHub actions, with the requirement of a uprn and a ntfy.sh topic. Running the script is as simple as 

```bash
harlow-bindicator--uprn "12379870" --topic "topic-name"
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
1. Create your Feature Branch (git checkout -b feature/AmazingFeature)
1. Commit your Changes (git commit -m 'Add some AmazingFeature')
1. Push to the Branch (git push origin feature/AmazingFeature)
1. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
