from fastapi import FastAPI
from gq.database import engine, Base
from gq.routers import booking,package,user,login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Or specify ["http://127.0.0.1:5500"] if using a local server for SignUp.html
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(engine)

app.include_router(package.router)
app.include_router(user.router)
app.include_router(booking.router)
app.include_router(login.router)