import os
import qrcode
from extract_flags import extract_all_flags

QR_OUTPUT_DIR = "./qrcodes"

def generate_qr_codes():
    flags = extract_all_flags()
    os.makedirs(QR_OUTPUT_DIR, exist_ok=True)

    for flag in flags:
        img = qrcode.make(flag)
        safe_name = flag.replace("/", "").replace(":", "").replace(" ", "_")
        path = os.path.join(QR_OUTPUT_DIR, f"{safe_name}.png")
        img.save(path)
        print(f"🧾 QR Code generated for flag: {flag}")

if __name__ == "__main__":
    generate_qr_codes()
    print("\n✅ All QR codes are saved in ./qrcodes/")