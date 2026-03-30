from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import whisper
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="MigraineChatAPI", version="0.1.0")

# Load Whisper model
model = whisper.load_model("base")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Validate file extension
    if not file.filename.lower().endswith(('.mp3', '.m4a')):
        raise HTTPException(status_code=400, detail="Only .mp3 and .m4a files are allowed")

    # Save file temporarily
    temp_path = f"/tmp/{file.filename}"
    try:
        with open(temp_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Transcribe with Whisper
        result = model.transcribe(temp_path)
        transcription = result["text"].strip()

        if not transcription:
            raise HTTPException(status_code=500, detail="Transcription failed or empty")

        # Send transcription to Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"First, please respond to this text as if you were a medical assistant, trying to get information about the patient's condition. Second, generate structured notes summarizing key points from the transcription: {transcription}",
                }
            ],
            model="llama-3.3-70b-versatile",  # Using Groq's Llama 3 model
        )

        analysis = chat_completion.choices[0].message.content

        return {
            "transcription": transcription,
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.get("/")
async def root():
    return {"message": "MigraineChatAPI is running"}

 