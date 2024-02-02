from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from users import users_list
import httpx


app = FastAPI(title="Demo Microservice w/ FastAPI")


# Print Hello World from the server
@app.get("/")
def get_root():
    return {"Hello":"World"}


# Get all users
@app.get("/users")
def get_all_users():
    return users_list

# Get a users age
@app.get("/users/{name}")
def get_all_users(name: str):
    user = users_list[name]
    if user is None:
        return {"error": "User does not exist!"}
    return {"age": user}


# Get a random picture of coffee
@app.get("/coffee")
async def get_coffee():
    async with httpx.AsyncClient() as client:
        coffee_api = "https://coffee.alexflipnote.dev/random"
        try:
            # Fetching the image from the URL
            response = await client.get(coffee_api)
            response.raise_for_status()  # Raises an exception for 4XX/5XX responses
        except httpx.RequestError as exc:
            raise HTTPException(status_code=400, detail=f"Request error: {exc}") from exc
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"HTTP error: {exc}") from exc

        # Stream the response back
        return StreamingResponse(response.iter_bytes(), media_type=response.headers['Content-Type'])

# Create a simple webpage
@app.get("/home")
async def get_homepage():
    page = \
        """
            <script>
                function btn_click() {
                    alert('You clicked this button');
                }
            </script>

            <html style="background-color: blue;">
                <center>
                    <h1>Welcome to my webpage!!</h1>
                    <button id='btn' onclick='btn_click();'>Click me</button>
                </center>
            </html>
        """
    return HTMLResponse(content=page)