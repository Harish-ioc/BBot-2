import torch
import torchaudio
import sounddevice as sd
from transformers import AutoProcessor, WhisperForConditionalGeneration


processor = AutoProcessor.from_pretrained("openai/whisper-tiny.en")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

# Load the audio from a local file using torchaudio
def audioFfile(audio_file_path = "audio/output.wav"):
    waveform, sample_rate = torchaudio.load(audio_file_path)
    print(waveform.shape)
    inputs = processor(waveform.squeeze().numpy(), sampling_rate=sample_rate, return_tensors="pt")
    return \

def audio_from_mic(duration=5, sample_rate=16000):
    print("Recording... Speak now!")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Recording complete!")
    waveform = torch.tensor(audio_data).float()
    waveform = waveform.T
    waveform = waveform / 32767.0
    inputs = processor(waveform.squeeze().numpy(), sampling_rate=sample_rate, return_tensors="pt")
    return inputs

def text(inputs):
    input_features = inputs.input_features
    generated_ids = model.generate(inputs=input_features)
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return transcription

print(text(audio_from_mic()))

