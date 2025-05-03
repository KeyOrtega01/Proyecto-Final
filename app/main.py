from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router as rutas_api
from app.auth import router as rutas_auth  # Asegura que auth.py tiene el router definido
    
app = FastAPI(title="Biblioteca API", debug=True)

app.include_router(rutas_api)
app.include_router(rutas_auth)  # Agrega autenticación
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
