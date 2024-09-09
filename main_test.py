from fastapi.testclient import TestClient
from PIL import Image
import io
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_predict_image():
    img = Image.new("RGB", (100, 100), color = "red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    files = {"image": ("test.png", img_byte_arr, "image/png")}
    response = client.post("/predict/", files=files)

    assert response.status_code == 200
    data = response.json()
    assert data["width"] == 100
    assert data["height"] == 100
    assert data["message"] == "Prediction simulated"

def test_predict_invalid_image_type():
    file_content = b"Hello, this is not an image!"
    files = {"image": ("test.txt", file_content, "text/plain")}
    response = client.post("/predict/", files=files)

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid image type. Only JPEG and PNG are supported."}
