from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.plateController import router as plate_router

app = FastAPI(title="Consulta de Placas - API")

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plate_router, prefix="/api", tags=["Placas"])
@app.get("/")
async def root():
    return {"status": "running", "message": "API de Placas activa"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10110, reload=True)
