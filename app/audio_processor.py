import os
from typing import Optional


class AudioProcessor:
    def __init__(self, audio_path: str) -> None:
        self.audio_path = audio_path

    def validate_audio(self) -> bool:
        formats_allowed = (".mp3",)
        if not os.path.exists(self.audio_path):
            return False

        if not self.audio_path.lower().endswith(formats_allowed):
            return False

        return True

    def load_audio(self) -> bool:
        if self.validate_audio():
            return True
        return False