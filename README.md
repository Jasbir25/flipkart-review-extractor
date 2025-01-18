# Flipkart Review Extractor

This Python project uses [Playwright](https://playwright.dev) to scrape reviews from Flipkart product pages. The script extracts product reviews, including the rating, title, and body, from the specified URL. It can also handle pagination and gather reviews from multiple pages.

## Features
- Extracts product reviews from Flipkart product pages.
- Retrieves review details like rating, title, and body.
- Automatically handles pagination to fetch reviews from multiple pages.
- Skips the "READ MORE" link and retrieves the full review body.

## Prerequisites
- Python 3.9 or higher
- Playwright library for Python

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flipkart-review-extractor.git
   cd flipkart-review-extractor
   ```

2. Create and activate a conda environment:

   ```bash
   conda create --name flipkart-review-extractor python=3.9
   conda activate flipkart-review-extractor
   ```

3. Install the required dependencies:

   ```bash
   pip install playwright
   ```

4. Install Playwright browsers:

   ```bash
   playwright install
   ```

## Usage

1. Import the `extract_reviews` function in your script:

   ```python
   from extract_reviews import extract_reviews
   ```

2. Call the `extract_reviews` function with the URL of the Flipkart product page:

   ```python
   url = "https://www.flipkart.com/product-page-url"
   reviews = await extract_reviews(url)
   print(reviews)
   ```

   The `extract_reviews` function will return a dictionary with the following structure:

   ```json
   {
       "reviews_count": 10,
       "reviews": [
           {
               "rating": "4.5",
               "title": "Great Product!",
               "body": "The product is excellent, highly recommended!"
           },
           {
               "rating": "3.0",
               "title": "Good but not perfect",
               "body": "The product is okay but has some flaws."
           }
           // More reviews
       ]
   }
   ```

3. To run the script, ensure you are using an asynchronous environment or wrap the call inside an event loop.

## Contributing

If you have any suggestions or improvements, feel free to create a pull request or open an issue.
