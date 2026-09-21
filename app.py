from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Enable cross-origin resource sharing so your Framer page can connect seamlessly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataPayload(BaseModel):
    legacy_code: str

@app.post("/translate")
def process_migration_stream(payload: DataPayload):
    if not payload.legacy_code.strip():
        return {"output": "SYSTEM_WARNING: Null input exception detected."}
        
    prompt = f"### Instruction:\nTranslate this legacy data structure into a modern JSON schema.\n\n### Input:\n{payload.legacy_code}\n\n### Response:\n"
    
    # 🌟 PASTE YOUR ACCESS KEY INSIDE THE EMPTY QUOTES BELOW
    HF_TOKEN = "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"
    API_URL = "https://huggingface.co"
    
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=30)
        if response.status_code == 200:
            result = response.json()
            full_output = result[0].get("generated_text", "") if isinstance(result, list) else str(result)
            if "### Response:\n" in full_output:
                full_output = full_output.split("### Response:\n")[-1]
            return {"output": full_output.strip()}
        return {"output": f"OPERATIONAL_EXCEPTION: Hub returned code ({response.status_code})"}
    except Exception as e:
        return {"output": f"SYSTEM_ERROR: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
