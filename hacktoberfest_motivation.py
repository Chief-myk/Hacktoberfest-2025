import random
import time

tips = [
    "🚀 Fork → Branch → Commit → Pull Request — that’s the open-source flow!",
    "💡 Every small contribution counts. Even fixing a typo helps the community!",
    "🌱 Learn, contribute, and grow — Hacktoberfest is your start to open source.",
    "🧩 Don’t wait for perfect code — share, improve, and collaborate!",
    "💜 You’re not just coding — you’re building the future of open source.",
    "🔥 Keep pushing commits, your PRs shape real projects!"
]

def hacktoberfest_motivation():
    print("\n🌍 Welcome to Hacktoberfest 2025 – Beginner’s Guide 🌍\n")
    time.sleep(1)
    print("🎉 Generating your motivation tip...\n")
    time.sleep(1)
    print(f"💬 {random.choice(tips)}\n")
    print("🎯 Keep contributing with curiosity & respect ❤")

if __name__ == "__main__":
    hacktoberfest_motivation()
