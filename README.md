# CoinMarketCap Historical Data Scraper

This project scrapes historical cryptocurrency data from CoinMarketCap using Selenium. The scraper navigates to the given historical page, loads the data, and exports it to a CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)


## Introduction

The purpose of this project is to scrape historical cryptocurrency data from CoinMarketCap and store it in a structured CSV format for analysis. The script automatically scrolls through the page, loads additional data, and extracts it into a pandas DataFrame.

## Features

- Automates the loading of additional content by interacting with the "Load More" button.
- Scrolls through the page to ensure all data is loaded.
- Extracts tabular data and converts it to a CSV file.
- Handles potential missing elements using try-except blocks.

## Technologies Used

- **Python**: Core language used for the scraper.
- **Selenium**: To automate browser actions.
- **Pandas**: For data manipulation and exporting to CSV.
- **ChromeDriver**: To interact with the Chrome browser.

### Prerequisites

1. Install Python 3.x from [here](https://www.python.org/downloads/).
2. Install Google Chrome from [here](https://www.google.com/chrome/).
3. Download the matching version of **ChromeDriver** for your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).


