import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import random

# Load the models and tokenizer
model_name = "Canstralian/text2shellcommands"  # Choose your model, can be changed based on use case
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate shell command or response based on the prompt
def generate_shell_command(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)
    command = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return command

# Function to simulate a retro terminal environment with some 90s hacker vibe
def terminal_ui(prompt):
    # Simulate typing effect
    fake_typing_effect = [
        "Initializing...\n",
        "Boot sequence complete...\n",
        "Connecting to secure network...\n",
        "Accessing restricted files...\n",
        "Running diagnostics...\n",
        "Command input: " + prompt + "\n"
    ]
    
    # Adding some suspense and random time delays to create that 'hacker' feel
    for line in fake_typing_effect:
        time.sleep(random.uniform(0.5, 1.5))  # Simulate typing delay
        print(line)  # Simulate print to terminal
        time.sleep(0.3)
    
    # Get AI-generated response for the command prompt
    command_response = generate_shell_command(prompt)
    
    # Simulate result display with some retro terminal feedback
    result_output = f"\n[ SYSTEM STATUS: OK ]\n[ {random.choice(['OK', 'ERROR', 'WARNING'])} ]\n\n"
    result_output += f"Command executed: {command_response}\n"
    result_output += "[ End of output ]"
    
    return result_output

# Create a Gradio interface with a retro terminal design
def retro_terminal_interface(prompt):
    result = terminal_ui(prompt)
    return result

# Launch the Gradio app with a terminal theme
iface = gr.Interface(
    fn=retro_terminal_interface, 
    inputs=gr.Textbox(placeholder="Type your shell command here...", label="Enter Command:"),
    outputs=gr.Textbox(label="Terminal Output", lines=20, interactive=False),
    theme="compact",  # Use Gradio's built-in compact theme for a terminal-like feel
    live=True  # Enable live feedback to simulate a real-time terminal experience
)

iface.launch()
