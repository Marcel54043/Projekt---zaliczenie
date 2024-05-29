import argparse
import mimetypes
import os


def main():
    
    parser = argparse.ArgumentParser(description='Prosty program do wyświetlania informacji o pliku.')

    
    parser.add_argument('filename', type=str, help='Ścieżka do pliku do przetworzenia')

   
    args = parser.parse_args()

    
    filename = args.filename

    
    if not os.path.isfile(filename):
        print(f"Plik {filename} nie został znaleziony.")
        return

    
    print(f"Nazwa pliku: {os.path.basename(filename)}")

 
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type is None:
        mime_type = 'Nieznany'
    print(f"Rodzaj pliku: {mime_type}")

 
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Zawartość pliku:\n{content}")
    except Exception as e:
        print(f"Nie udało się odczytać pliku {filename}: {e}")


if __name__ == "__main__":
    main()