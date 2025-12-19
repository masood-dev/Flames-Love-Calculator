# Purpose Calculator

A simple Flask web app. which is made of simple childhood love games. Like flames and nickname mashup etc, which you've probably heard in your childhood.
the important purpose of this app is to understand the complex logic behind of these small, simple games and the algorithms used in this games, algorithms are very complex and mind boggling sometimes but, they are beautiful once you start makeing sense of it. this simple games based on simple algorithms made it easy to understand the logic even better in fun way by playing simple games. you can fork the repository to learn and play around on you own.
The flames algorithm :


## Features

- Calculate relationship compatibility between two names
- Lightweight Flask backend and static frontend

## Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/flames-website.git
cd flames-website
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS / Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python -m flames_app.app
```

5. Open your browser at http://localhost:5000

## About `requests`

The project includes the `requests` library for making HTTP requests to external APIs. and it's useful for:

- Fetching external data (quotes, random names, or public APIs)
- Downloading files or images
- Sending form data or interacting with third-party services

Example usage:
```python
import requests

resp = requests.get('https://api.quotable.io/random')
if resp.ok:
	quote = resp.json().get('content')
	author = resp.json().get('author')
	print(f'"{quote}" — {author}')
```

`requests` is already listed in `requirements.txt`.

## Project Structure

```
flames-website/
├── flames_app/
│   ├── app.py
│   ├── requirements.txt
   ├── static/
   └── templates/
├── DEPLOYMENT.md
├── Procfile
├── requirements.txt
└── README.md
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment options and notes.

## Contributing

Contributions are welcome. Open an issue or submit a pull request.

## License

MIT License
