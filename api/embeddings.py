import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# import the FastAPI app defined in the package
from open.text.embeddings.server.app import app as fastapi_app

# Expose your FastAPI app at the Serverless entrypoint
app = fastapi_app


# (Optional) if you want to log the health check:
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
