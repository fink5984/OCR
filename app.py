from flask import Flask, request
import pytesseract
from PIL import Image
import io
import requests

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    image_url = request.json.get("image_url")  # מקבל את קישור התמונה ב-POST
    if not image_url:
        return {"error": "No image URL provided"}, 400

    # הורד את התמונה מהקישור
    try:
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content))
    except Exception as e:
        return {"error": f"Failed to download image: {str(e)}"}, 400

    # הפעל OCR על התמונה
    text = pytesseract.image_to_string(img)
    return {"text": text}

if __name__ == "__main__":
    app.run(debug=True)
