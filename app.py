import gradio as gr
import pandas as pd
from utils.dataset_loader import load_dataset

# Load dataset
df = load_dataset()

# Function to simulate conversation with model selection
def chat_interface(user_input, selected_model, prompt_id=None):
    if df is not None and prompt_id is not None:
        prompt = df.iloc[prompt_id]["prompt_text"]  # Replace with the actual column name
        response = f"[{selected_model}] used the debugging prompt: '{prompt}'.\nUser said: '{user_input}'\nResponse: Simulated output."
    else:
        response = f"[{selected_model}] says: You entered '{user_input}'. This is a simulated response."
    return response

# List of available models (Updated as per your request)
models = ["Canstralian/text2shellcommands", "Canstralian/RabbitRedux", "Canstralian/CySec_Known_Exploit_Analyzer"]
prompt_ids = df.index.tolist() if df is not None else []

# Gradio Interface
with gr.Blocks(css="./static/styles.css") as demo:
    with gr.Row():
        gr.Markdown("### Retro Hacker Chat with Debugging Prompts", elem_classes="retro-terminal")
    with gr.Row():
        user_input = gr.Textbox(
            label="Enter your message:",
            placeholder="Type your message here...",
            elem_classes="retro-terminal"
        )
        model_selector = gr.Dropdown(
            choices=models,
            label="Select Model",
            value=models[0],
            elem_classes="retro-terminal"
        )
        if prompt_ids:
            prompt_selector = gr.Dropdown(
                choices=prompt_ids,
                label="Select Debugging Prompt ID",
                value=prompt_ids[0],
                elem_classes="retro-terminal"
            )
        else:
            prompt_selector = None
    with gr.Row():
        response_box = gr.Textbox(
            label="Model Response:",
            placeholder="The model's response will appear here...",
            elem_classes="retro-terminal"
        )
    with gr.Row():
        send_button = gr.Button("Send", elem_classes="retro-terminal")

    # Link input and output
    if prompt_selector:
        send_button.click(chat_interface, inputs=[user_input, model_selector, prompt_selector], outputs=response_box)
    else:
        send_button.click(chat_interface, inputs=[user_input, model_selector], outputs=response_box)

# Launch the interface
demo.launch()
