import uvicorn
from config import variables as config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from view import table_view


app = FastAPI()
origins = [
    "*"
]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(table_view.router)

    
if __name__ == "__main__":
    uvicorn.run("app:app", port=int(config["PORT"]))