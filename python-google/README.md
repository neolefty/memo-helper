# python-google

Try out the Google Cloud Speech-to-Text API.

## Getting Started

1. Install the [Homebrew](https://brew.sh/) package manager, then run (in the `python-google` directory):

```bash
brew install rye portaudio
rye sync
```

Then, to start a development session and run the code:

```bash
. .venv/bin/activate
python src/python_google/speech.py
```

Note that `rye` pins Python 3.11, which is needed for `portaudio` as described [here](https://medium.com/@yashwant-das/installing-pyaudio-on-macos-14-0-with-an-m1-macbook-3952c73598d6)