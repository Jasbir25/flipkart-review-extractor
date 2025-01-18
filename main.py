from fastapi import FastAPI, HTTPException
from urllib.parse import urlparse
from reviews_extractor import extract_reviews

app = FastAPI()

def validate_url(url: str) -> bool:
    """
    Validates if the provided URL is properly formatted.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

@app.get("/api/reviews")
async def get_reviews(url: str):
    """
    API endpoint to extract reviews from a product page.
    :param url: URL of the product page
    :return: JSON response with reviews or an error message
    """
    if not validate_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL format. Please provide a valid URL.")
    
    try:
        data = await extract_reviews(url)
        return data
    except Exception as e:
        return {"error": str(e)}
