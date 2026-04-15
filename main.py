from fastapi import FastAPI
from routers.news import router as news_router
from routers.user import router as user_router
app=FastAPI()

app.include_router(news_router)
app.include_router(user_router)