import argparse
import mimetypes
import os
import json


def main():
    
    parser = argparse.ArgumentParser(
        description='Prosty program do wyświetlania i zapisywania informacji o pliku JSON.')

   
    parser.add_argument('filename', type=str, help='Ścieżka do pliku do przetworzenia')
    parser.add_argument('-o', '--output', type=str, help='Ścieżka do pliku wyjściowego')

   
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

  
    if mime_type != 'application/json':
        print(f"Plik {filename} nie jest plikiem JSON.")
        return

    
    try:
        with open(filename, 'r') as file:
            content = file.read()

            data = json.loads(content)
            print(f"Zawartość pliku JSON:\n{json.dumps(data, indent=4)}")
            print("Plik JSON jest poprawny składniowo.")

            if args.output:
                try:
                    with open(args.output, 'w') as output_file:
                        json.dump(data, output_file, indent=4)
                    print(f"Dane zostały zapisane do pliku {args.output}")
                except Exception as e:
                    print(f"Nie udało się zapisać danych do pliku {args.output}: {e}")
    except json.JSONDecodeError as e:
        print(f"Nie udało się odczytać pliku {filename}: Błąd składni JSON - {e}")
    except Exception as e:
        print(f"Nie udało się odczytać pliku {filename}: {e}")


if __name__ == "__main__":
    main()