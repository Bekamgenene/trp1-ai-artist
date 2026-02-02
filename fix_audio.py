"""Convert raw PCM audio to proper WAV format with headers."""

import wave
import struct
from pathlib import Path

def add_wav_header(raw_pcm_path: Path, output_wav_path: Path, sample_rate: int = 24000, channels: int = 1, sample_width: int = 2):
    """
    Add WAV header to raw PCM data.
    
    Google Lyria outputs raw PCM16 mono at 24kHz.
    """
    # Read raw PCM data
    raw_data = raw_pcm_path.read_bytes()
    
    # Create WAV file with proper headers
    with wave.open(str(output_wav_path), 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(raw_data)
    
    print(f"✓ Converted {raw_pcm_path.name} -> {output_wav_path.name}")
    print(f"  Size: {len(raw_data):,} bytes")
    print(f"  Duration: {len(raw_data) / (sample_rate * channels * sample_width):.1f}s")

if __name__ == "__main__":
    exports_dir = Path("exports")
    
    # Find all raw audio files
    raw_files = [
        "lyria_20260202_131233.wav",
        "lyria_20260202_131515.wav", 
        "lyria_20260202_133454.wav",
    ]
    
    for filename in raw_files:
        raw_path = exports_dir / filename
        output_path = exports_dir / filename.replace(".wav", "_fixed.wav")
        
        if raw_path.exists():
            add_wav_header(raw_path, output_path)
