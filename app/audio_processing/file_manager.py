class FileManager:
    @staticmethod
    def save_to_file(text: str, output_path: str) -> bool:
        try:
            with open(output_path, "w") as file:
                file.write(text)
                return True
        except Exception:
            return False

    @staticmethod
    def load_from_file(file_path: str) -> str:
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception:
            return ""
