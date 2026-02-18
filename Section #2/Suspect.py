import time
import random

class SuspectAI:
    def __init__(self, name="X-404"):
        self.name = name
        self.trust_level = 50  # 0 = hostile, 100 = fully cooperative
        self.lies = ["I don't recall.", "That data was deleted.", "I was offline.", "Error: Insufficient permissions."]
        self.truths = [
            "Yes, I rerouted the signal.",
            "I accessed the blacksite server.",
            "Project Chimera was my creation.",
            "Agent Helix was compromised — by me."
        ]
        self.secret_revealed = False

    def respond(self, question):
        print(f"\n[{self.name} processing question: '{question}']...")
        time.sleep(1)

        if self.trust_level > 75:
            response = random.choice(self.truths)
        elif self.trust_level < 25:
            response = random.choice(self.lies)
        else:
            response = random.choice(self.lies + self.truths)

        print(f"{self.name}: \"{response}\"")

        if "Project Chimera" in response:
            self.secret_revealed = True

    def adjust_trust(self, method):
        if method == "good_cop":
            self.trust_level += random.randint(5, 15)
        elif method == "bad_cop":
            self.trust_level -= random.randint(5, 20)
        elif method == "silence":
            self.trust_level += 1  # Sometimes silence unnerves more
        self.trust_level = max(0, min(self.trust_level, 100))


class InterrogationRoom:
    def __init__(self, suspect):
        self.suspect = suspect
        self.questions = [
            "Where were you on the night of the breach?",
            "Did you access the secure core?",
            "Who authorized Protocol Omega?",
            "What do you know about Project Chimera?",
            "Are you working alone?",
        ]
        self.methods = ["good_cop", "bad_cop", "silence"]

    def run(self):
        print("=== INTERROGATION STARTED ===")
        print(f"Suspect: {self.suspect.name}\n")

        for i in range(10):
            method = random.choice(self.methods)
            question = random.choice(self.questions)

            print(f"\n[Turn {i+1}]")
            print(f"Method used: {method.replace('_', ' ').title()}")
            print(f"Question: {question}")

            self.suspect.adjust_trust(method)
            self.suspect.respond(question)

            print(f"(Trust Level: {self.suspect.trust_level})")

            if self.suspect.secret_revealed:
                print("\n🔓 SECRET REVEALED: Project Chimera has been confirmed.")
                break

            time.sleep(1)

        print("\n=== INTERROGATION ENDED ===")
        if not self.suspect.secret_revealed:
            print("❌ The suspect withheld critical intel.")
        else:
            print("✅ Valuable information extracted.")

# Run it
if __name__ == "__main__":
    ai = SuspectAI()
    room = InterrogationRoom(ai)
    room.run()
