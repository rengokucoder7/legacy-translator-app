import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "rengokucoder7/my-legacy-translator"

print("Starting operational infrastructure compilation layers...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float32, 
    device_map="auto"
)

def translate_data_logic(legacy_code):
    prompt = f"### Instruction:\nTranslate this legacy data structure into a modern JSON schema.\n\n### Input:\n{legacy_code}\n\n### Response:\n"
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=512)
    full_output = tokenizer.decode(outputs, skip_special_tokens=True)
    
    if "### Response:\n" in full_output:
        clean_output = full_output.split("### Response:\n")[-1]
    else:
        clean_output = full_output
        
    return clean_output.strip()

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

with gr.Blocks(theme=theme, title="Parity Labs - Autonomous Data Unification Layer") as demo:
    
    # Administrative Core Header Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(
                """
                # Parity Labs | Enterprise System Infrastructure Console
                ### **Autonomous Data Unification Layer (ADUL) v1.0.0**
                
                ---
                SYSTEM DEPLOYMENT STATUS: `ACTIVE` | PRIVACY GATEWAY ENFORCEMENT: `ON-PREMISE COMPLIANCE`
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
        Confidentiality Notice: This system compiles schemas locally. Operational telemetry values conform to institutional data management parameters.
        </p>
        """
    )

# Establish port binding to integrate with Render's infrastructure host rules
demo.launch(server_name="0.0.0.0", server_port=10000)
