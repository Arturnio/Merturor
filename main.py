from fastapi import FastAPI
from backend.routes import users, workouts  # Импорт роутеров

app = FastAPI()

@app.get("/")
async def general():
    return {"message": "Приложение запускается"}

@app.get("/ping")
async def ping():
    return {"message": "Server is running"}

# Подключаем маршруты
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(workouts.router, prefix="/workouts", tags=["Workouts"])

print("Маршруты приложения:", app.routes)  # Отладка!