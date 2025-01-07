from app import TranscriptionService


def main():
    audio_path = input("Archivo de audio: ")
    model_size = input("Tamaño del modelo: ")
    name_output = input("Nombre del archivo: ")
    output_path = "./data/output/" + name_output + ".txt"

    transcription_service = TranscriptionService(audio_path, model_size)
    transcription = transcription_service.execute(output_path)

    if transcription:
        print(f"Finalizado")
    else:
        print("Transcripción fallida")


if __name__ == "__main__":
    main()
