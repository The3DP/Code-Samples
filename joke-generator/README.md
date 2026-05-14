# 😄 Random Joke Generator

A complete, production-ready joke generator that fetches random jokes from an external API (JokeAPI). Includes implementations in Python and JavaScript with a beautiful web UI.

## 📋 Features

✨ **Multiple Implementations**
- Python CLI with interactive menu
- JavaScript with async/await
- Responsive HTML5 web interface

✅ **Joke Categories**
- Any (random joke)
- General
- Programming
- Knock-Knock

🛡️ **Robust Error Handling**
- Network timeout handling
- Connection error recovery
- Graceful failure messages

🎨 **Beautiful UI**
- Gradient design
- Smooth animations
- Mobile responsive
- Punchline reveal functionality

📡 **External API Integration**
- Uses [JokeAPI](https://jokeapi.dev/)
- Free, no authentication required
- Fast and reliable

## 🚀 Quick Start

### Python CLI

**Requirements:**
```bash
pip install requests
```

**Usage:**
```bash
python joke_generator.py
```

**Features:**
- Interactive menu system
- Press Enter to reveal punchlines
- Safe mode enabled by default
- Session management with connection pooling

### Web UI

**Usage:**
Simply open `joke_generator.html` in any modern web browser!

**Features:**
- Click "Get a Joke" to fetch a random joke
- Select joke type from dropdown
- Press Enter key as shortcut
- Automatic punchline reveal button for two-part jokes

### JavaScript Module

**Usage:**
```javascript
const generator = new JokeGeneratorUI();
generator.init(); // Initialize event listeners

// Or fetch directly
const joke = await generator.fetchJoke("programming", true);
generator.displayJoke(joke);
```

## 📚 API Reference

### JokeAPI Endpoints

**Get Any Joke:**
```
GET https://v2.jokeapi.dev/joke/any?safe-mode=true
```

**Get Programming Joke:**
```
GET https://v2.jokeapi.dev/joke/programming?safe-mode=true
```

**Response Format (Single-part):**
```json
{
  "type": "single",
  "joke": "Why do Java developers wear glasses? Because they don't C#",
  "id": 1
}
```

**Response Format (Two-part):**
```json
{
  "type": "twopart",
  "setup": "Why did the scarecrow win an award?",
  "delivery": "He was outstanding in his field!",
  "id": 2
}
```

## 💻 Code Examples

### Python - Simple Usage

```python
from joke_generator import JokeGenerator

# Create instance
gen = JokeGenerator()

# Fetch and display a joke
joke = gen.get_joke("programming", safe_mode=True)
if joke:
    gen.display_joke(joke)
```

### Python - Custom Implementation

```python
from joke_generator import JokeGenerator

gen = JokeGenerator(timeout=15)
joke_data = gen.get_joke("knock-knock")

if joke_data["type"] == "twopart":
    print(joke_data["setup"])
    input("Press Enter for the punchline...")
    print(joke_data["delivery"])
```

### JavaScript - Fetch Joke

```javascript
const ui = new JokeGeneratorUI();

// Fetch a programming joke
const joke = await ui.fetchJoke("programming", true);

// Display it
ui.displayJoke(joke);
```

## 🔧 Customization

### Change API Endpoint

**Python:**
```python
generator.BASE_URL = "https://custom-api.com/jokes"
```

**JavaScript:**
```javascript
generator.baseUrl = "https://custom-api.com/jokes";
```

### Disable Safe Mode

**Python:**
```python
joke = generator.get_joke("any", safe_mode=False)
```

**JavaScript:**
```javascript
const joke = await generator.fetchJoke("any", false);
```

### Adjust Timeout

**Python:**
```python
generator = JokeGenerator(timeout=20)
```

**JavaScript:**
```javascript
generator.timeout = 20000; // milliseconds
```

## 🌟 Future Enhancements

- [ ] Save favorite jokes to local storage
- [ ] Share jokes on social media
- [ ] Rate jokes (like/dislike)
- [ ] Search by keyword
- [ ] Multiple language support
- [ ] Daily joke email notifications
- [ ] Dark mode toggle
- [ ] Accessibility improvements (WCAG 2.1)

## 📝 File Structure

```
joke-generator/
├── joke_generator.py       # Python CLI implementation
├── joke_generator.js       # JavaScript module
├── joke_generator.html     # Web UI
└── README.md              # Documentation
```

## 🔗 Resources

- [JokeAPI Documentation](https://jokeapi.dev/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork, modify, and use this project as you wish. Suggestions for improvements are always welcome!

---

**Made with ❤️ for the developer community**
