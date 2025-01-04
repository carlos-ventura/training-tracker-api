from fastapi import HTTPException, Request, Security
from fastapi.security import api_key
import os

api_key_header = api_key.APIKeyHeader(name="X-API-KEY")


async def validate_api_key(key: str = Security(api_key_header)):
    if key != os.getenv("API_KEY"):
         raise HTTPException(status_code=401, detail="Unauthorized")
