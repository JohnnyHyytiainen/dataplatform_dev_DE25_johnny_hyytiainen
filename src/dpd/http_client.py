from __future__ import annotations

from typing import Any
import httpx


class FetchError(RuntimeError):
    """Raised when an HTTP fetch fails in a readable way."""


def fetch_json(url: str, *, timeout: float = 10.0) -> Any:
    """
    Fetch JSON from a URL and return it as Python data (dict/list).
    Fail-fast with a readable error message.
    """
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            resp = client.get(url)

        # 4xx/5xx => exception
        resp.raise_for_status()

        # Parse JSON => Python data (list/dict)
        return resp.json()

    except httpx.TimeoutException as e:
        raise FetchError(f"Timeout after {timeout}s for URL: {url}") from e

    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        raise FetchError(f"HTTP {status} from URL: {url}") from e

    except ValueError as e:
        # JSON parsing failed
        raise FetchError(f"Response was not valid JSON from URL: {url}") from e
