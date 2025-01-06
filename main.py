from app.transcription.transcription_service import TranscriptionService


def main():
    # audio_path = input("Archivo de audio: ") or "./public/audio-5m.mp3"
    audio_path = "./public/audio-15m.mp3"
    # model_size = input("Tamaño del modelo: ") or "base"
    model_size = "turbo"
    # output_path = input("Nombre del archivo: ") or "./public/output.txt"
    output_path = "./public/output1.txt"

    transcription_service = TranscriptionService(audio_path, model_size)
    transcription = transcription_service.execute(output_path)

    if transcription:
        print(f"La transcripción: {transcription}")
    else:
        print("Transcripción fallida")


if __name__ == "__main__":
    main()
