import os
import subprocess

APK_PATH = "./apk/GL_Bajaj_v1.apk"
OUTPUT_DIR = "./decompiled"

def run_decompilation():
    if not os.path.exists(APK_PATH):
        print("APK file not found!")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Running JADX decompilation...")

    result = subprocess.run([
        r"C:\Users\hs285\Downloads\jadx-1.5.2\bin\jadx.bat", "-d", OUTPUT_DIR, APK_PATH
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ Decompilation complete!")
    else:
        print("❌ Error during decompilation:")
        print(result.stderr)

if __name__ == "__main__":
    run_decompilation()