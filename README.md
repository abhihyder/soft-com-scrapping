# Software Company Scrapping

**Soft Company Scrapping** is a Python-based web scraper designed to search for companies on Google Maps and extract their names and website URLs. The results are saved in an Excel file for further processing.

## Features

- Search for companies on Google Maps based on an input query.
- Scroll through the results to capture more companies.
- Extract company names and website URLs.
- Save the results to an Excel file locally.

## Requirements

- Python 3.10 or higher
- Poetry (for managing dependencies)

## Installation

To get started with this project, follow the steps below:

### 1. Clone the repository

```bash
git clone <repository_url>
cd soft-com-scrapping
```

### 2. Install dependencies using Poetry

Ensure that you have **Poetry** installed. If not, you can install it from [here](https://python-poetry.org/docs/#installation).

Run the following command to install the project dependencies:

```bash
poetry install
```

## Usage

To run the scraper, you can use the following command:

### 1. With a custom search query:

```bash
poetry run start -s "Software company near Banani, Dhaka"
```

This will scrape Google Maps for companies near Banani, Dhaka.

### 2. With the default search query:

If no search query is provided, the scraper will use "Software company in Dhaka" as the default search term.

```bash
poetry run start
```

### 3. Result

After running the scraper, an Excel file (`companies.xlsx`) will be created in the local directory, containing the following columns:
- **Company Name**
- **Website URL**
