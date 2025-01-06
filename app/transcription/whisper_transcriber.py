import whisper


class WhisperTranscriber:
    def __init__(self, audio_path: str, model: str = "base") -> None:
        self.audio_path = audio_path
        self.model = model

    def transcribe(self) -> str:
        whisper_model = whisper.load_model(self.model)
        result = whisper_model.transcribe(
            audio=self.audio_path,
            language="es",
            verbose=True,
            fp16=True,)
        return result["text"]
