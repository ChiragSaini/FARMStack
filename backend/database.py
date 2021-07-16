from model import Todo

# * MongoDB Driver
from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/FARM')

database = client.TodoList

collection = database.todos

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos
    
async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {
        "description": description
    }})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True