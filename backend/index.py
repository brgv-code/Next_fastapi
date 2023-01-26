from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(user)

# handle cross origin resource sharing

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,

    allow_methods=["*"],
    allow_headers=["*"],
)


