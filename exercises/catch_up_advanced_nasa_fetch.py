from __future__ import annotations
from pathlib import Path
import httpx


def download_apod(api_key: str = "DEMO_KEY", out_dir: str = "data/processed") -> Path | None:
    api_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    with httpx.Client(timeout=20.0, follow_redirects=True) as client:
        meta_resp = client.get(api_url, params=params)
        meta_resp.raise_for_status()
        meta = meta_resp.json()

        title = meta.get("title")
        media_type = meta.get("media_type")
        url = meta.get("url")
        date = meta.get("date", "unknown-date")

        print(f"Title: {title}")
        print(f"Media type: {media_type}")
        print(f"URL: {url}")

        if media_type != "image":
            print("Not an image today. Skipping download.")
            return None

        if not url:
            raise RuntimeError("No URL found in metadata")

        img_resp = client.get(url)
        img_resp.raise_for_status()

        # välj suffix från url, fallback till .bin
        suffix = Path(url).suffix or ".bin"
        filename = f"apod_{date}{suffix}"
        file_path = out_path / filename

        file_path.write_bytes(img_resp.content)
        print(f"Saved: {file_path}")

        return file_path


if __name__ == "__main__":
    download_apod()
