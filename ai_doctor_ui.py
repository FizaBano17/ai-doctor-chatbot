import gradio as gr
from chat import medical_chat
from speech import get_voice_input
from vision import analyze_image

def chat_fn(q):
    return medical_chat(q)

def voice_fn(dur):
    text = get_voice_input(dur)
    if not text:
        return "Could not understand speech."
    return f"You said: {text}\n\nAI Doctor: {medical_chat(text)}"

def image_fn(img):
    if img is None:
        return "Upload an image"
    img.save("temp.jpg")
    return analyze_image("temp.jpg")

with gr.Blocks(title="AI Doctor Assistant") as demo:
    gr.Markdown("# 🩺 AI Doctor Assistant")

    with gr.Tab("Text"):
        q = gr.Textbox(label="Ask a question")
        out = gr.Textbox()
        btn = gr.Button("Send")
        btn.click(chat_fn, q, out)

    with gr.Tab("Voice"):
        dur = gr.Slider(2, 10, value=5, label="Recording Duration")
        out2 = gr.Textbox()
        btn2 = gr.Button("Record & Diagnose")
        btn2.click(voice_fn, dur, out2)

    with gr.Tab("Image"):
        img = gr.Image(type="pil")
        out3 = gr.Textbox()
        btn3 = gr.Button("Analyze Image")
        btn3.click(image_fn, img, out3)

demo.launch()




#http://127.0.0.1:7860