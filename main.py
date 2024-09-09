from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/predict/")
async def predict_image(image: UploadFile = File(...)):
    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type. Only JPEG and PNG are supported.")

    image = Image.open(BytesIO(await image.read()))

    # Simular procesamiento de imagen (aquí se colocaría la lógica del modelo)
    # Por ahora, solo vamos a retornar las dimensiones de la imagen como una predicción simulada.
    width, height = image.size
    prediction = {
        "width": width,
        "height": height,
        "message": "Prediction simulated"
    }

    return prediction
