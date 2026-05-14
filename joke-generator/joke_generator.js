/**
 * Random Joke Generator - Enhanced JavaScript Implementation
 * Features: Favorites, Dark Mode, Copy to Clipboard
 * Fetches jokes from JokeAPI and displays them with smooth animations
 * Includes XSS protection and comprehensive error handling
 */

class JokeGeneratorUI {
    constructor() {
        this.baseUrl = "https://v2.jokeapi.dev/joke";
        this.timeout = 10000; // milliseconds
        this.jokeTypes = ["any", "general", "programming", "knock-knock"];
        this.currentJoke = null;
        this.isLoading = false;
        this.favorites = this.loadFavorites();
        this.darkMode = this.loadDarkMode();
    }

    /**
     * Initialize event listeners and apply saved preferences
     */
    init() {
        // Apply dark mode preference
        if (this.darkMode) {
            document.body.classList.add("dark-mode");
            this.updateThemeButton();
        }

        // Get DOM elements
        const getJokeBtn = document.getElementById("get-joke-btn");
        const punchlineBtn = document.getElementById("punchline-btn");
        const jokeTypeSelect = document.getElementById("joke-type");
        const themeToggle = document.getElementById("theme-toggle");
        const favoritesBtn = document.getElementById("favorites-btn");
        const closeFavoritesBtn = document.getElementById("close-favorites");
        const copyBtn = document.getElementById("copy-btn");
        const favoriteBtn = document.getElementById("favorite-btn");
        const favoritesModal = document.getElementById("favorites-modal");

        // Event listeners
        if (getJokeBtn) {
            getJokeBtn.addEventListener("click", () => this.handleGetJoke());
            jokeTypeSelect.addEventListener("keypress", (e) => {
                if (e.key === "Enter") this.handleGetJoke();
            });
        }

        if (punchlineBtn) {
            punchlineBtn.addEventListener("click", () => this.showPunchline());
        }

        if (themeToggle) {
            themeToggle.addEventListener("click", () => this.toggleDarkMode());
        }

        if (favoritesBtn) {
            favoritesBtn.addEventListener("click", () => this.openFavoritesModal());
        }

        if (closeFavoritesBtn) {
            closeFavoritesBtn.addEventListener("click", () => this.closeFavoritesModal());
        }

        if (copyBtn) {
            copyBtn.addEventListener("click", () => this.copyJokeToClipboard());
        }

        if (favoriteBtn) {
            favoriteBtn.addEventListener("click", () => this.toggleFavorite());
        }

        // Close modal when clicking outside
        favoritesModal.addEventListener("click", (e) => {
            if (e.target === favoritesModal) {
                this.closeFavoritesModal();
            }
        });
    }

    /**
     * Toggle dark mode on/off
     */
    toggleDarkMode() {
        this.darkMode = !this.darkMode;
        document.body.classList.toggle("dark-mode");
        this.saveDarkMode();
        this.updateThemeButton();
    }

    /**
     * Update theme button appearance
     */
    updateThemeButton() {
        const themeToggle = document.getElementById("theme-toggle");
        if (this.darkMode) {
            themeToggle.textContent = "☀️";
            themeToggle.title = "Toggle light mode";
            themeToggle.classList.add("active");
        } else {
            themeToggle.textContent = "🌙";
            themeToggle.title = "Toggle dark mode";
            themeToggle.classList.remove("active");
        }
    }

    /**
     * Save dark mode preference to localStorage
     */
    saveDarkMode() {
        localStorage.setItem("joke-dark-mode", JSON.stringify(this.darkMode));
    }

    /**
     * Load dark mode preference from localStorage
     */
    loadDarkMode() {
        const saved = localStorage.getItem("joke-dark-mode");
        return saved ? JSON.parse(saved) : false;
    }

    /**
     * Add or remove joke from favorites
     */
    toggleFavorite() {
        if (!this.currentJoke) return;

        const jokeText = this.getJokeText();
        const favoriteBtn = document.getElementById("favorite-btn");
        const isFavorited = this.favorites.some((fav) => fav.text === jokeText);

        if (isFavorited) {
            this.favorites = this.favorites.filter((fav) => fav.text !== jokeText);
            favoriteBtn.classList.remove("favorited");
            favoriteBtn.textContent = "🤍 Add to Favorites";
        } else {
            this.favorites.push({
                text: jokeText,
                type: this.currentJoke.type,
                timestamp: new Date().toISOString(),
            });
            favoriteBtn.classList.add("favorited");
            favoriteBtn.textContent = "❤️ Remove from Favorites";
        }

        this.saveFavorites();
    }

    /**
     * Check if current joke is favorited
     */
    updateFavoriteButton() {
        if (!this.currentJoke) return;

        const jokeText = this.getJokeText();
        const favoriteBtn = document.getElementById("favorite-btn");
        const isFavorited = this.favorites.some((fav) => fav.text === jokeText);

        if (isFavorited) {
            favoriteBtn.classList.add("favorited");
            favoriteBtn.textContent = "❤️ Remove from Favorites";
        } else {
            favoriteBtn.classList.remove("favorited");
            favoriteBtn.textContent = "🤍 Add to Favorites";
        }
    }

    /**
     * Get the full joke text
     */
    getJokeText() {
        if (this.currentJoke.type === "single") {
            return this.currentJoke.joke;
        } else {
            return `${this.currentJoke.setup}\n\n${this.currentJoke.delivery}`;
        }
    }

    /**
     * Copy joke to clipboard
     */
    async copyJokeToClipboard() {
        if (!this.currentJoke) return;

        const jokeText = this.getJokeText();
        const copyBtn = document.getElementById("copy-btn");

        try {
            await navigator.clipboard.writeText(jokeText);
            
            // Visual feedback
            const originalText = copyBtn.textContent;
            copyBtn.textContent = "✓ Copied!";
            copyBtn.style.background = "#51cf66";
            
            setTimeout(() => {
                copyBtn.textContent = originalText;
                copyBtn.style.background = "";
            }, 2000);
        } catch (err) {
            console.error("Failed to copy:", err);
            alert("Failed to copy joke to clipboard");
        }
    }

    /**
     * Open favorites modal
     */
    openFavoritesModal() {
        const favoritesModal = document.getElementById("favorites-modal");
        favoritesModal.classList.add("active");
        this.renderFavorites();
    }

    /**
     * Close favorites modal
     */
    closeFavoritesModal() {
        const favoritesModal = document.getElementById("favorites-modal");
        favoritesModal.classList.remove("active");
    }

    /**
     * Render favorites list
     */
    renderFavorites() {
        const favoritesList = document.getElementById("favorites-list");

        if (this.favorites.length === 0) {
            favoritesList.innerHTML = `
                <div class="empty-favorites">
                    <p>📭 No favorite jokes yet!</p>
                    <p>Add jokes to your favorites to see them here.</p>
                </div>
            `;
            return;
        }

        favoritesList.innerHTML = this.favorites
            .map(
                (fav, index) => `
            <div class="favorite-item">
                <div class="favorite-item-text">${this.escapeHtml(fav.text)}</div>
                <div class="favorite-item-actions">
                    <button class="action-btn" onclick="window.jokeGenerator.copyFavorite('${index}')">📋</button>
                    <button class="action-btn" onclick="window.jokeGenerator.removeFavorite('${index}')">✕</button>
                </div>
            </div>
        `
            )
            .join("");
    }

    /**
     * Copy favorite joke to clipboard
     */
    async copyFavorite(index) {
        if (this.favorites[index]) {
            try {
                await navigator.clipboard.writeText(this.favorites[index].text);
                alert("✓ Joke copied to clipboard!");
            } catch (err) {
                console.error("Failed to copy:", err);
                alert("Failed to copy joke");
            }
        }
    }

    /**
     * Remove favorite joke
     */
    removeFavorite(index) {
        this.favorites.splice(index, 1);
        this.saveFavorites();
        this.renderFavorites();
        this.updateFavoriteButton();
    }

    /**
     * Save favorites to localStorage
     */
    saveFavorites() {
        localStorage.setItem("joke-favorites", JSON.stringify(this.favorites));
    }

    /**
     * Load favorites from localStorage
     */
    loadFavorites() {
        const saved = localStorage.getItem("joke-favorites");
        return saved ? JSON.parse(saved) : [];
    }

    /**
     * Escape HTML to prevent XSS attacks
     */
    escapeHtml(text) {
        const map = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
    }

    /**
     * Fetch a joke from the API
     */
    async fetchJoke(jokeType = "any", safeMode = true) {
        try {
            if (!this.jokeTypes.includes(jokeType.toLowerCase())) {
                console.error(`Invalid joke type: ${jokeType}`);
                return null;
            }

            const url = new URL(`${this.baseUrl}/${jokeType}`);
            url.searchParams.append("safe-mode", safeMode.toString().toLowerCase());

            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), this.timeout);

            const response = await fetch(url.toString(), {
                signal: controller.signal,
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                throw new Error(
                    `HTTP Error: ${response.status} ${response.statusText}`
                );
            }

            const data = await response.json();
            return data;
        } catch (error) {
            if (error.name === "AbortError") {
                console.error("Request timeout");
                this.showError("Request timed out. Please try again.");
            } else if (error instanceof TypeError) {
                console.error("Network error:", error);
                this.showError(
                    "Network error. Please check your internet connection."
                );
            } else {
                console.error("Error fetching joke:", error);
                this.showError("Failed to fetch joke. Please try again.");
            }
            return null;
        }
    }

    /**
     * Display the joke in the UI
     */
    displayJoke(jokeData) {
        if (!jokeData || jokeData.error) {
            this.showError("No joke received. Please try again.");
            return;
        }

        this.currentJoke = jokeData;
        const jokeContainer = document.getElementById("joke-container");
        const jokeText = document.getElementById("joke-text");
        const punchlineBtn = document.getElementById("punchline-btn");

        jokeContainer.style.display = "block";

        if (jokeData.type === "single") {
            jokeText.textContent = this.escapeHtml(jokeData.joke);
            punchlineBtn.style.display = "none";
        } else if (jokeData.type === "twopart") {
            jokeText.textContent = this.escapeHtml(jokeData.setup);
            punchlineBtn.style.display = "block";
            punchlineBtn.textContent = "Show Punchline 😂";
            punchlineBtn.dataset.punchline = this.escapeHtml(
                jokeData.delivery
            );
        }

        this.isLoading = false;
        this.updateButtonState();
        this.updateFavoriteButton();
    }

    /**
     * Show the punchline for two-part jokes
     */
    showPunchline() {
        const jokeText = document.getElementById("joke-text");
        const punchlineBtn = document.getElementById("punchline-btn");

        if (punchlineBtn.dataset.punchline) {
            jokeText.textContent = punchlineBtn.dataset.punchline;
            punchlineBtn.style.display = "none";
        }
    }

    /**
     * Show error message in the joke container
     */
    showError(message) {
        const jokeContainer = document.getElementById("joke-container");
        const jokeText = document.getElementById("joke-text");
        const punchlineBtn = document.getElementById("punchline-btn");

        jokeContainer.style.display = "block";
        jokeText.textContent = `❌ ${message}`;
        punchlineBtn.style.display = "none";

        this.isLoading = false;
        this.updateButtonState();
    }

    /**
     * Update button state based on loading status
     */
    updateButtonState() {
        const getJokeBtn = document.getElementById("get-joke-btn");
        if (getJokeBtn) {
            getJokeBtn.disabled = this.isLoading;
            getJokeBtn.textContent = this.isLoading ? "Loading... ⏳" : "Get a Joke! 😄";
        }
    }

    /**
     * Handle the "Get Joke" button click
     */
    async handleGetJoke() {
        if (this.isLoading) return;

        this.isLoading = true;
        this.updateButtonState();

        const jokeTypeSelect = document.getElementById("joke-type");
        const selectedType = jokeTypeSelect.value;

        const jokeData = await this.fetchJoke(selectedType, true);

        if (jokeData) {
            this.displayJoke(jokeData);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    const generator = new JokeGeneratorUI();
    window.jokeGenerator = generator; // Make globally accessible for inline events
    generator.init();
});
