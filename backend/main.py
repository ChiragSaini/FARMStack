from model import Todo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# * App Object
app = FastAPI()

from database import create_todo, fetch_all_todos, fetch_one_todo, update_todo, remove_todo

origin = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

@app.get('/')
def read_route():
    return {
        'Ping': 'Pong'
    }

@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get('/api/todo{title}', response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no Todo item with this title {title}')


@app.post('/api/todo', response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')

@app.put('/api/todo{title}', response_model=Todo)
async def update_my_todo(title:str, description:str):
    response = await update_todo(title, description)
    if response:
        return response
    raise HTTPException(404, f"there is no todo with this title {title}")

@app.delete('/api/todo{title}')
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return 'Deleted Successfully !!! ;)' 
    raise HTTPException(404, f"there is no todo with this title {title}")