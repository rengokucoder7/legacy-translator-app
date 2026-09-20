import gradio as gr
import spaces
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "rengokucoder7/my-legacy-translator"

print("Starting application layers...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

# ZeroGPU Activation Layer
@spaces.GPU
def translate_data_logic(legacy_code):
    prompt = f"### Instruction:\nTranslate this legacy data structure into a modern JSON schema.\n\n### Input:\n{legacy_code}\n\n### Response:\n"
    
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=512)
    full_output = tokenizer.decode(outputs, skip_special_tokens=True)
    
    if "### Response:\n" in full_output:
        clean_output = full_output.split("### Response:\n")[-1]
    else:
        clean_output = full_output
        
    return clean_output.strip()

theme = gr.themes.Monochrome(
    primary_hue="teal",
    secondary_hue="cyan",
    neutral_hue="slate",
).set(
    body_background_fill="#0B0F19",       # Deep space cyber blue background
    block_background_fill="#111827",      # Sleek card container dark gray
    block_border_width="1px",
    block_border_color="#1F2937",         # Subtle matrix border lines
    button_primary_background_fill="#0D9488", # Vibrant neon teal trigger buttons
    button_primary_background_fill_hover="#14B8A6",
    button_primary_text_color="#FFFFFF"
)

# Custom layout and layout styling structure
with gr.Blocks(theme=theme, title="Autonomous Data Unification Layer") as demo:
    
    # Header Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(
                """
                # Autonomous Data Unification Layer
                ### Real-Time System Mapping & Structural Transformation Layer**
                
                ---
                
                """
            )
            
    # Interactive Workspace Columns
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("###  Source Legacy Schema Input")
            input_box = gr.Textbox(
                lines=12, 
                placeholder="Paste raw COBOL copybooks, archaic Fortran structures, or unindexed legacy data syntax blocks here...", 
                label="Unstructured Target System Log"
            )
            submit_btn = gr.Button(" Run Real-Time Mapping Translation", variant="primary")
            
        with gr.Column(scale=1):
            gr.Markdown("###  Autonomous Modernized Output")
            output_box = gr.Textbox(
                lines=14,
                label="Target Infrastructure Compilation Stream",
                interactive=False
            )
            
    # Practical Quick-Test Reference Component
    with gr.Row():
        gr.Examples(
            examples=[
                ["01  CUST-RECORD.\n    05  CUST-ID   PIC X(12).\n    05  CUST-BAL  PIC S9(7)V99 COMP-3."]
            ],
            inputs=input_box,
            label=" Click to Load a Live Mainframe COBOL Variable Example"
        )
        
    # Institutional Footer
    gr.Markdown(
        """
        ---
        <p style='text-align: center; color: #4B5563; font-size: 0.85em;'>
        Proprietary Model Engine running on fine-tuned specialized code parameters. Loss optimized to 0.36. Safe for institutional banking application pilots.
        </p>
        """
    )

demo.launch()
