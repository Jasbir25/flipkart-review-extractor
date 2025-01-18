from playwright.async_api import async_playwright

async def extract_reviews(url):
    """
    Extract reviews from Flipkart product pages using Playwright.

    Args:
        url (str): URL of the product page.

    Returns:
        dict: JSON response containing reviews and review count.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Block heavy resources to optimize performance
        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "stylesheet", "font"] else route.continue_())

        # Navigate to the URL
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print(f"Failed to load the page: {e}")
            return {"error": "Failed to load the page"}

        reviews = []

        # Function to extract reviews from the current page
        async def extract_current_page_reviews():
            review_elements = await page.query_selector_all('div.ZmyHeo.MDcJkH')  # Parent container for each review
            for review in review_elements:
                try:
                    # Extract rating
                    rating_element = await review.query_selector('div.XQDdHH.Ga3i8K._9lBNRY')
                    rating = await rating_element.text_content() if rating_element else "N/A"

                    # Extract title
                    title_element = await review.query_selector('div._11pzQk')
                    title = await title_element.text_content() if title_element else "N/A"

                    # Extract body (without "READ MORE" handling)
                    body_element = await review.query_selector('span.wTYmpv span')
                    if body_element and await body_element.text_content() == "READ MORE":
                        body_element = await review.query_selector('span.wTYmpv')  # Use the full body without "READ MORE"
                    body = await body_element.text_content() if body_element else "N/A"

                    reviews.append({
                        "rating": rating.strip(),
                        "title": title.strip(),
                        # "body": body.strip(),
                    })
                except Exception as e:
                    print(f"Error extracting review: {e}")

        # Extract reviews from the current page
        await extract_current_page_reviews()

        # Handle pagination
        while True:
            try:
                next_button = await page.query_selector('a[rel="next"]')  # Flipkart's "Next" button
                if next_button:
                    await next_button.click()
                    await page.wait_for_timeout(2000)  # Adjust delay for loading the next page
                    await extract_current_page_reviews()
                else:
                    break
            except Exception as e:
                print(f"Pagination error: {e}")
                break

        await browser.close()
        return {"reviews_count": len(reviews), "reviews": reviews}
