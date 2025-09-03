from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def a():
    return {"hello": "gi"}

@app.post("/auth/me")
async def auth_me(authorization: str = Header(default=None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    # Aqui estamos assumindo que o header é do tipo "Bearer usuario"
    try:
        scheme, username = authorization.split()
        if scheme.lower() != "bearer":
            raise ValueError
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid authorization format. Use 'Bearer <username>'.")

    return JSONResponse(content={"user": username, "ping": "pong"})
