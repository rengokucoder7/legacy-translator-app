import gradio as gr
import requests
import json

# Institutional Monochrome Corporate Interface Specifications
theme = gr.themes.Monochrome(
    primary_hue="slate",
    secondary_hue="slate",
    neutral_hue="slate",
).set(
    body_background_fill="#0F172A",       # Institutional dark gray background
    block_background_fill="#1E293B",      # Secured system interface card containers
    block_border_width="1px",
    block_border_color="#334155",         # Standard network boundary line styling
    button_primary_background_fill="#1E3A8A", # Dark corporate navy blue execution buttons
    button_primary_background_fill_hover="#1E40AF",
    button_primary_text_color="#FFFFFF"
)

def translate_data_logic(legacy_code):
    if not legacy_code.strip():
        return "SYSTEM_WARNING: Null input exception detected."
        
    prompt = f"### Instruction:\nTranslate this legacy data structure into a modern JSON schema.\n\n### Input:\n{legacy_code}\n\n### Response:\n"
    API_URL = "https://huggingface.co"
    
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 512, "return_full_text": False}
    }
    
    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                full_output = result[0].get("generated_text", "")
            elif isinstance(result, dict):
                full_output = result.get("generated_text", str(result))
            else:
                full_output = str(result)
                
            if "### Response:\n" in full_output:
                return full_output.split("### Response:\n")[-1].strip()
            return full_output.strip()
            
        elif response.status_code == 503:
            return "SYSTEM_NOTICE: Foundational model parameters initializing in backend cluster cache. Re-execute translation layer in 60 seconds."
            
        return f"OPERATIONAL_EXCEPTION: Error Code {response.status_code} - {response.text}"
        
    except requests.exceptions.Timeout:
        return "OPERATIONAL_EXCEPTION: Request transmission timeout. Network execution pass terminated."
    except Exception as e:
        return f"SYSTEM_ERROR: {str(e)}"

with gr.Blocks(theme=theme, title="Parity Labs - Autonomous Data Unification Layer") as demo:
    
    # Administrative Core Header Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(
                """
                # Parity Labs | Enterprise System Infrastructure Console
                ### **Autonomous Data Unification Layer (ADUL) v1.0.0**
                
                ---
                SYSTEM DEPLOYMENT STATUS: `ACTIVE` | PRIVACY GATEWAY ENFORCEMENT: `HYBRID APIS COMPLIANCE`
                """
            )
            
    # System Architecture Data Panels
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Source Legacy System Schema Input")
            input_box = gr.Textbox(
                lines=12, 
                placeholder="Insert target mainframe records, structural source strings, or legacy data layouts...", 
                label="Source Enterprise Syntax Block"
            )
            submit_btn = gr.Button("Execute Real-Time Schema Compilation", variant="primary")
            
        with gr.Column(scale=1):
            gr.Markdown("### Target Infrastructure Unified Output")
            output_box = gr.Textbox(
                lines=14,
                label="Target Schema Target Format Stream",
                interactive=False
            )
            
    # Connect UI button trigger directly to the logic engine loop
    submit_btn.click(fn=translate_data_logic, inputs=input_box, outputs=output_box)
            
    # Reference Pipeline Evaluation Dataset Component
    with gr.Row():
        gr.Examples(
            examples=[
                ["01  CUST-RECORD.\n    05  CUST-ID   PIC X(12).\n    05  CUST-BAL  PIC S9(7)V99 COMP-3."]
            ],
            inputs=input_box,
            label="System Test Schema: Mainframe COBOL Framework Reference Data"
        )
        
    # Regulatory Footer Notice
    gr.Markdown(
        """
        ---
        <p style='text-align: center; color: #64748B; font-size: 0.85em;'>
        Confidentiality Notice: This interface routes transaction queries through secure architectural API layers. Operational parameters match target infrastructure compliance codes.
        </p>
        """
    )

# Enforce port binding configuration matching Render's gateway rules
demo.launch(server_name="0.0.0.0", server_port=10000)
