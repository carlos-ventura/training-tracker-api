from fastapi import HTTPException, Request
import os


async def validate_api_key(request: Request):
    if request.cookies.get("api_key") != os.getenv("API_KEY"):
         raise HTTPException(status_code=401, detail="Unauthorized")