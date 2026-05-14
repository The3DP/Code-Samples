/**
 * Random Joke Generator - JavaScript Implementation
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
    }

    /**
     * Initialize event listeners
     */
    init() {
        const getJokeBtn = document.getElementById("get-joke-btn");
        const punchlineBtn = document.getElementById("punchline-btn");
        const jokeTypeSelect = document.getElementById("joke-type");

        if (getJokeBtn) {
            getJokeBtn.addEventListener("click", () => this.handleGetJoke());
            if (jokeTypeSelect) {
                jokeTypeSelect.addEventListener("keypress", (e) => {
                    if (e.key === "Enter") this.handleGetJoke();
                });
            }
        }

        if (punchlineBtn) {
            punchlineBtn.addEventListener("click", () => this.showPunchline());
        }
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
                this.showError("Request timed out. Please try again.");
            } else if (error instanceof TypeError) {
                this.showError(
                    "Network error. Please check your internet connection."
                );
            } else {
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
        jokeText.textContent = `Error: ${message}`;
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
            getJokeBtn.textContent = this.isLoading ? "Loading..." : "Get a Joke!";
        }
    }

    /**
     * Handle the Get Joke button click
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
    generator.init();
});
