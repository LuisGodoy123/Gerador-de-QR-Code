import re
from urllib.parse import urlparse
import qrcode

def build_filename_from_url(url: str, max_length: int = 80) -> str:
	"""Create a filesystem-friendly PNG filename derived from the URL."""
	parsed = urlparse(url)
	base = (parsed.netloc + parsed.path) or "qrcode"
	base = base.strip("/") or "qrcode"
	base = base.replace("/", "_")
	base = re.sub(r"[^A-Za-z0-9._-]+", "-", base)
	base = base.strip("-._") or "qrcode"
	if len(base) > max_length:
		base = base[:max_length]
	return f"{base}.png"


url = input("Insira a url para gerar o QR Code: ")

img = qrcode.make(url)
filename = build_filename_from_url(url)

img.save(filename)
print(f"QR Code salvo como '{filename}'")