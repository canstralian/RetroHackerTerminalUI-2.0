import gradio as gr

# Function to simulate conversation with model selection
def chat_interface(user_input, selected_model):
    response = f"[{selected_model}] says: You entered '{user_input}'. This is a simulated response."
    return response

# List of available models
models = ["Canstralian/text2shellcommands", "Canstralian/RabbitRedux", "Canstralian/CySec_Known_Exploit_Analyzer"]

# Gradio Interface
with gr.Blocks(css="./static/styles.css") as demo:
    with gr.Row():
        gr.Markdown(
            "### Welcome to the Retro Hacker Chat! \n"
            "_Experience the retro vibe while interacting with your models._",
            elem_classes="retro-terminal"
        )
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
    with gr.Row():
        response_box = gr.Textbox(
            label="Model Response:",
            placeholder="The model's response will appear here...",
            elem_classes="retro-terminal"
        )
    with gr.Row():
        send_button = gr.Button("Send", elem_classes="retro-terminal")

    # Link input and output
    send_button.click(chat_interface, inputs=[user_input, model_selector], outputs=response_box)

# Launch the interface
demo.launch()
