"""
Random Joke Generator using JokeAPI - Enhanced Edition
Features: Favorites system with persistence
A simple yet powerful joke generator that fetches jokes from an external API.
Supports multiple joke types and provides a clean, interactive CLI experience.
"""

import requests
import json
import os
from typing import Dict, Optional, List
import sys


class JokeGenerator:
    """
    A class to generate random jokes using the JokeAPI.
    Provides methods to fetch, display, and save favorite jokes.
    """

    BASE_URL = "https://v2.jokeapi.dev/joke"
    JOKE_TYPES = {
        "any": "Any",
        "general": "General",
        "programming": "Programming",
        "knock-knock": "Knock-Knock"
    }
    FAVORITES_FILE = "joke_favorites.json"

    def __init__(self, timeout: int = 10):
        """
        Initialize the JokeGenerator.

        Args:
            timeout (int): Request timeout in seconds. Default is 10.
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.favorites = self.load_favorites()

    def get_joke(self, joke_type: str = "any", safe_mode: bool = True) -> Optional[Dict]:
        """
        Fetch a random joke from JokeAPI.

        Args:
            joke_type (str): Type of joke ('any', 'general', 'programming', 'knock-knock')
            safe_mode (bool): If True, filters out offensive jokes

        Returns:
            Optional[Dict]: Joke data dictionary or None if request fails
        """
        try:
            # Validate joke type
            if joke_type.lower() not in self.JOKE_TYPES:
                print(f"Invalid joke type: {joke_type}")
                print(f"Available types: {', '.join(self.JOKE_TYPES.keys())}")
                return None

            # Build API URL
            url = f"{self.BASE_URL}/{joke_type}"
            params = {"safe-mode": str(safe_mode).lower()}

            # Make request
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            print("Error: Request timed out. Please try again.")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Failed to connect to JokeAPI. Check your internet connection.")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP {e.response.status_code} - {e.response.reason}")
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred - {str(e)}")
            return None

    def display_joke(self, joke_data: Dict) -> None:
        """
        Display a joke in a formatted manner.

        Args:
            joke_data (Dict): Joke data from the API
        """
        if not joke_data or joke_data.get("error"):
            print("No joke received. Please try again.")
            return

        print("\n" + "=" * 60)
        print("🎭 JOKE TIME! 🎭")
        print("=" * 60)

        if joke_data["type"] == "single":
            # Single-part joke
            print(f"\n{joke_data['joke']}\n")
        else:
            # Two-part joke
            print(f"\n{joke_data['setup']}\n")
            input("Press Enter to reveal the punchline...\n")
            print(f"{joke_data['delivery']}\n")

        print("=" * 60 + "\n")

    def get_joke_text(self, joke_data: Dict) -> str:
        """
        Get the full joke text as a string.

        Args:
            joke_data (Dict): Joke data from the API

        Returns:
            str: The complete joke text
        """
        if joke_data["type"] == "single":
            return joke_data["joke"]
        else:
            return f"{joke_data['setup']}\n{joke_data['delivery']}"

    def add_favorite(self, joke_data: Dict) -> None:
        """
        Add a joke to favorites.

        Args:
            joke_data (Dict): Joke data to add
        """
        joke_text = self.get_joke_text(joke_data)
        
        # Check if already in favorites
        if any(fav["text"] == joke_text for fav in self.favorites):
            print("✓ Already in favorites!")
            return

        self.favorites.append({
            "text": joke_text,
            "type": joke_data.get("type", "unknown")
        })
        self.save_favorites()
        print("⭐ Added to favorites!")

    def load_favorites(self) -> List[Dict]:
        """
        Load favorites from JSON file.

        Returns:
            List[Dict]: List of favorite jokes
        """
        if os.path.exists(self.FAVORITES_FILE):
            try:
                with open(self.FAVORITES_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def save_favorites(self) -> None:
        """Save favorites to JSON file."""
        try:
            with open(self.FAVORITES_FILE, "w", encoding="utf-8") as f:
                json.dump(self.favorites, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving favorites: {e}")

    def view_favorites(self) -> None:
        """Display all favorite jokes."""
        if not self.favorites:
            print("\n" + "=" * 60)
            print("📭 No Favorites Yet!")
            print("=" * 60)
            print("\nStart adding jokes to your favorites to see them here.\n")
            return

        print("\n" + "=" * 60)
        print("⭐ MY FAVORITE JOKES ⭐")
        print("=" * 60)

        for idx, favorite in enumerate(self.favorites, 1):
            print(f"\n{idx}. {favorite['text']}\n")
            print("-" * 60)

    def clear_favorites(self) -> None:
        """Clear all favorite jokes with confirmation."""
        if not self.favorites:
            print("No favorites to clear.")
            return

        confirm = input("⚠️  Are you sure? This will delete all favorites. (yes/no): ").strip().lower()
        if confirm == "yes":
            self.favorites = []
            self.save_favorites()
            print("✓ All favorites cleared!")
        else:
            print("Cancelled.")

    def interactive_menu(self) -> None:
        """Display an interactive menu for selecting and fetching jokes."""
        while True:
            print("\n🎪 RANDOM JOKE GENERATOR 🎪")
            print("-" * 40)
            print("Select an option:")
            print()
            print("  1. Get a Joke")
            print("  2. View Favorites")
            print("  3. Clear Favorites")
            print("  4. Exit")
            print()

            try:
                choice = input("Enter your choice (1-4): ").strip()

                if choice == "1":
                    self.get_joke_menu()
                elif choice == "2":
                    self.view_favorites()
                elif choice == "3":
                    self.clear_favorites()
                elif choice == "4":
                    print("\n👋 Thanks for laughing with us! Goodbye!\n")
                    break
                else:
                    print("Invalid choice. Please try again.")

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_joke_menu(self) -> None:
        """Display menu for getting a joke."""
        print("\nSelect a joke type:")
        print()

        for idx, (key, display_name) in enumerate(self.JOKE_TYPES.items(), 1):
            print(f"  {idx}. {display_name}")

        print()

        try:
            choice = input("Enter your choice (1-4): ").strip()

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please try again.")
                return

            joke_type_list = list(self.JOKE_TYPES.keys())
            selected_type = joke_type_list[int(choice) - 1]

            print("\n📡 Fetching your joke...")
            joke_data = self.get_joke(selected_type, safe_mode=True)

            if joke_data:
                self.display_joke(joke_data)

                # Ask to save to favorites
                save = input("Would you like to save this to favorites? (y/n): ").strip().lower()
                if save == "y":
                    self.add_favorite(joke_data)

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """Main entry point for the joke generator."""
    try:
        generator = JokeGenerator()
        generator.interactive_menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
