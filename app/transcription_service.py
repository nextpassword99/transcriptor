from app.audio_processor import AudioProcessor
from app.file_manager import FileManager
from app.whisper_transcriber import WhisperTranscriber


class TranscriptionService:
    def __init__(self, audio_path: str, model_size: str = "base"):
        self.audio_path = audio_path
        self.model_size = model_size

    def execute(self, output_path: str) -> bool:
        ins_audio_processor = AudioProcessor(self.audio_path)
        audio = ins_audio_processor.load_audio()
        if not audio:
            return None

        ins_transcriber = WhisperTranscriber(self.audio_path, self.model_size)
        transcription = ins_transcriber.transcribe()

        if not transcription:
            return None

        ins_file_manager = FileManager()
        ins_file_manager.save_to_file(transcription, output_path)

        return transcription
