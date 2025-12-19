# Crushcheck? 🙄

## What's This About?

Remember those childhood games where you'd calculate if your crush likes you back using FLAMES? This is exactly that, but as a web app. I built this mainly to learn Flask and understand how these "magical" games actually work behind the scenes.

Turns out, these simple games have some pretty interesting logic. What seemed like magic when you were a kid is actually just string manipulation and some clever counting. Building this helped me understand algorithms in a fun way instead of just doing boring textbook problems.

## Why I Made This

It's one of my Friend's silly idea 😎

Honestly, I wanted to learn web development but most tutorial projects are either too simple (hello world) or too complex (build Instagram clone). This felt like a good middle ground - simple enough to finish, but complex enough to learn actual concepts.

Plus, the whole point isn't just writing code. I wanted to learn the full process: writing code, using Git properly, deploying to the cloud, making something that actually works online. It's more fun when you can share a real link with friends instead of just showing them code on your laptop.

**Check it out live:** [crushcheck.me](https://crushcheck.me)

### How the FLAMES Algorithm Works

![FLAMES Algorithm Flow](https://github.com/user-attachments/assets/ead584e2-cb3a-4dba-b714-885264ad00b0)

The algorithm is actually pretty smart when you break it down:
1. Take two names, remove spaces, make them lowercase
2. Cross out all the matching letters between both names
3. Count what's left and use that number to eliminate letters from "FLAMES"
4. Whatever letter remains is your "result"

It's simple but teaches you a lot about string processing, loops, and working with arrays.

## Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/crushcheck-fla.git
cd crushcheck-fla
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

## About the `requests` Library

I added the `requests` library because I wanted to learn how to work with external APIs. It's pretty useful for pulling in random quotes, facts, or any data from the internet.

Here's a simple example of how you could use it:

```python
import requests

resp = requests.get('https://api.quotable.io/random')
if resp.ok:
    quote = resp.json().get('content')
    author = resp.json().get('author')
    print(f'"{quote}" — {author}')
```

You could add this to show a random quote on the homepage or something. It's already in `requirements.txt` so feel free to play around with it.

## Project Structure

Here's how everything is organized:

```
crushcheck-fla/
├── flames_app/              # Main app folder
│   ├── app.py              # Flask routes and game logic
│   ├── static/             # CSS and JavaScript files
│   └── templates/          # HTML templates
├── DEPLOYMENT.md           # How to deploy this thing
├── Procfile               # For cloud deployment
├── requirements.txt        # Python packages needed
├── runtime.txt            # Python version
├── startup.sh             # Startup script
└── wsgi.py                # Entry point for production server
```

The structure is pretty standard for Flask apps. Templates go in `templates/`, CSS/JS goes in `static/`, and the main logic is in `app.py`.

## Deployment

Check out [DEPLOYMENT.md](DEPLOYMENT.md) for instructions on how to deploy this. I've included notes for deploying to Azure, Render, and other platforms. The process is actually pretty straightforward once you get the hang of it.

## Contributing

If you want to add features or improve something, go for it! Some ideas:
- Add more games (like compatibility by birthdate, zodiac signs, etc.)
- Make the UI look better
- Add animations
- Integrate some fun APIs

Fork it, mess around with it, break things, fix them. That's how you learn. Open an issue if you have questions or submit a pull request if you built something cool.

## License

MIT License - do whatever you want with this code.
