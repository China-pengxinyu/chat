from setuptools import setup, find_packages

setup(
    name="voice_assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sounddevice>=0.4.6",
        "pydub>=0.25.1",
        "faster-whisper>=0.10.0",
        "ollama>=0.1.6",
        "requests>=2.31.0"
    ],
)
