from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz, friendly_messages

description = """
This is an example FastAPI application. See [https://fastapi.tiangolo.com/tutorial/metadata/](https://fastapi.tiangolo.com/tutorial/metadata/)

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details

Here's a link to [my GitHub](https://www.github.com/andrewlee977)

<img src="https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg">
"""

app = FastAPI(
    title="Andrew's FastAPI Application",
    description=description,
    docs_url='/',
)


# Option 1
# # Same thing as @router in db.py
# @app.get('/another_message')
# def second_message():
#     return {'message': 'Here is another one'}

# Option 2 - use APIRouter to distribute these endpoints across files to keep it more organized
# important to attach all routers back to app to connect it to app
my_router = APIRouter()
# Option 2
@my_router.get('/another_message')
def second_message():
    return {'message': 'Here is another one'}

app.include_router(my_router)


# Tags are a way of organizing on Swagger doc, doesn't affect how code runs
app.include_router(db.router, tags=["Andrew's Database Endpoint"])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])
app.include_router(friendly_messages.router, tags=['My Friendly Messages'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)