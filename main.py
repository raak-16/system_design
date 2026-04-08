from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
def home():
	return {"message": "API Running"}


@app.post("/add_user")
def add_user(user: str):
	print(user)
	users.append(user)
	return {"message": "User added"}


@app.get("/users")
def get_users():
	return users
