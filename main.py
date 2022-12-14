from fastapi import FastAPI
from routes.intinerary import intineraty_router
import uvicorn


app = FastAPI()
# Register routes
app.include_router(intineraty_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)