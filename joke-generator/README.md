# 😄 Enhanced Random Joke Generator

A complete, production-ready joke generator with **Favorites**, **Dark Mode**, and **Copy to Clipboard** features! Includes implementations in Python and JavaScript with a beautiful responsive web UI.

## ✨ New Features Added

### 🌙 Dark Mode
- Toggle between light and dark themes
- Preference saved to browser (localStorage)
- Beautiful color transitions
- Fully responsive design

### ⭐ Favorites System
- Save jokes you love
- View all favorite jokes in a modal
- Manage favorites (copy, delete)
- Favorites persist in local storage (web) or JSON file (Python)
- Visual indicator for favorited jokes

### 📋 Copy to Clipboard
- One-click copy jokes to clipboard
- Smooth visual feedback
- Works with full two-part jokes (setup + punchline)
- Toast notification on successful copy

## 📋 Features Overview

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
- Gradient design with smooth transitions
- Dark mode support
- Mobile responsive
- Punchline reveal functionality
- Action buttons for favorites and copy

📱 **Data Persistence**
- Browser localStorage for web UI
- JSON file storage for Python CLI
- Automatic preference saving

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
- Save favorite jokes to file
- View all favorites
- Clear favorites
- Press Enter to reveal punchlines
- Safe mode enabled by default

### Web UI

**Usage:**
Simply open `joke_generator.html` in any modern web browser!

**Features:**
- Click "Get a Joke" to fetch
- Toggle dark mode (🌙)
- View favorites (⭐)
- Copy jokes (📋)
- Add to favorites (🤍)
- All preferences saved automatically

### JavaScript Module

**Usage:**
```javascript
const generator = new JokeGeneratorUI();
generator.init(); // Initialize with all features

// All features available through the UI:
// - Dark mode toggle
// - Favorites management
// - Copy to clipboard
// - Punchline reveal
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

### Python - Using Favorites

```python
from joke_generator import EnhancedJokeGenerator

gen = EnhancedJokeGenerator()

# Fetch a joke
joke = gen.get_joke("programming", safe_mode=True)
gen.display_joke(joke)

# Save to favorites
gen.save_favorite(joke)

# View all favorites
gen.view_favorites()

# Remove a favorite
gen.remove_favorite(0)
```

### JavaScript - Access Favorites

```javascript
const generator = new JokeGeneratorUI();
generator.init();

// Add current joke to favorites
generator.toggleFavorite();

// Open favorites modal
generator.openFavoritesModal();

// Copy joke to clipboard
await generator.copyJokeToClipboard();
```

### JavaScript - Dark Mode

```javascript
// Toggle dark mode
generator.toggleDarkMode();

// Check current mode
console.log(generator.darkMode);
```

## 🎨 Customization

### Change Colors

**CSS Variables in HTML:**
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --bg-primary: #ffffff;
    --text-primary: #333333;
    --accent-color: #667eea;
}
```

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

## 📂 File Structure

```
joke-generator/
├── joke_generator.py       # Python CLI with favorites
├── joke_generator.js       # JavaScript module (enhanced)
├── joke_generator.html     # Web UI with dark mode
└── README.md              # Documentation
```

## 🌟 Future Enhancements

- [ ] Export favorites as CSV/JSON
- [ ] Share jokes on social media
- [ ] Joke rating system (1-5 stars)
- [ ] Search favorites by keyword
- [ ] Multiple language support
- [ ] Voice/Text-to-Speech
- [ ] Joke categories in modal
- [ ] Shuffle favorites mode
- [ ] Service Worker for offline support
- [ ] Unit tests and coverage

## 🔗 Resources

- [JokeAPI Documentation](https://jokeapi.dev/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [MDN Web Docs - localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

## 💾 Data Storage

### Web UI (Browser)
- Favorites stored in `localStorage` (browser-specific, persists across sessions)
- Dark mode preference also in `localStorage`
- No server connection required
- Private to your browser

### Python CLI
- Favorites stored in `joke_favorites.json` in the application directory
- Human-readable JSON format
- Can be shared or backed up easily

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork, modify, and use this project as you wish. Suggestions for improvements are always welcome!

---

**Made with ❤️ for the developer community**

*Last Updated: 2026-05-14*
*Version: 2.0 (Enhanced)*
