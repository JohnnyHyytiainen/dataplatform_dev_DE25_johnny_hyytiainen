# Catch up övning. Ett fetch python script efter datamod labben för NASAS APOD api.

import httpx
import json

def download_nasa_image():
    # URL till NASAs API - DEMO_KEY för att slippa regga sig.
    api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

    print(f"=== STEP 1: Hämta metadata (JSON) ifrån {api_url} ===")

    # Steg 1. Hämta JSON(text)
    with httpx.Client() as client:
        response = client.get(api_url)

        # fail fast som vanligt:
        if response.status_code != 200:
            raise Exception(f"Något har gått fel. NASA svarar fel: {response.status_code}")
        
        metadata = response.json()
        # visa vad jag får för något(för att se strukturen)
        print("Fick svar. Här är bildens titel:")
        print(f"Titel: {metadata['title']}")
        print(f"URL till bilden: {metadata['url']}") # <--- DENNA jag vill åt!

        image_url = metadata['url']

        # Steg 2. Hämta själva bilden (BINÄR DATA!)
        print(f"\n=== STEP 2: Laddar ner bilden från {image_url} ===")

        # Ny request mot bild länken
        img_response = client.get(image_url)

        if img_response.status_code != 200:
            raise Exception(f"Något har gått fel. {img_response.status_code}")
        
        # Nu ska filen sparas.
        # 'wb' står för Write Binary. Utan 'b' försöker python spara allt som text och kraschar
        file_name = "nasa_apod_picture.jpg"

        with open(file_name, "wb") as file:
            # Skriv 'content' och inte 'text'
            file.write(img_response.content)


        print(f"Done. Bilden är sparad som '{file_name}' i root folder")

if __name__ == "__main__":
    download_nasa_image()
