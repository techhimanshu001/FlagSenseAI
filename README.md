# FlagSenseAI 🔍

An AI-powered APK analysis tool that leverages the CodeGemma language model to assist in reverse engineering and deobfuscation of Android applications.

## Features

- 🤖 Uses CodeGemma 2B model for code analysis
- 📱 Decompiles APK files using JADX
- 🔍 Detects potential flags, secrets, and debug bypasses
- 💡 Provides clear explanations of code functionality
- ✨ Suggests improved naming for variables and methods

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Hugging Face token:
```
HUGGING_FACE_TOKEN=your_token_here
```

3. Place your APK file in the `apk` directory

## Usage

```bash
python scripts/decompile.py  # Decompile APK
python scripts/analyze.py    # Run AI analysis
```

## Project Structure

- `scripts/` - Python source code
  - `decompile.py` - APK decompilation logic
  - `ai_model.py` - CodeGemma integration
  - `extract_flags.py` - Flag detection
- `apk/` - APK files for analysis
- `decompiled/` - Decompiled Java code
- `ai_output/` - Analysis results