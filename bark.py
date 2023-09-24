from transformers import AutoProcessor, BarkModel
import torch
import scipy
import io


# processor = AutoProcessor.from_pretrained("suno/bark")
# model = BarkModel.from_pretrained("suno/bark")
processor = AutoProcessor.from_pretrained("suno/bark-small")
model = BarkModel.from_pretrained("suno/bark-small")
model = model.to_bettertransformer()
print("Model loaded")

if torch.cuda.is_available():
    model = model.to("cuda")


def run_inference(text: str, voice: str = None):
    inputs = processor(text, voice)

    if torch.cuda.is_available():
        inputs = {key: value.to("cuda") for key, value in inputs.items()}

    audio_array = model.generate(**inputs)

    if torch.cuda.is_available():
        audio_array = audio_array.to("cpu")

    audio_array = audio_array.cpu().numpy().squeeze()

    return audio_array


def create_audio_buffer(audio_array):
    sample_rate = model.generation_config.sample_rate
    audio_buffer = io.BytesIO()
    scipy.io.wavfile.write(audio_buffer, rate=sample_rate, data=audio_array)
    audio_buffer.seek(0)
    return audio_buffer.getvalue()
