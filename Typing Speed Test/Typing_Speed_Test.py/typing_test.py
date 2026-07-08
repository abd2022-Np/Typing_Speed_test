import random
import time

sentences = [
    "Python is one of the most popular programming languages.",
    "Practice every day to improve your typing speed.",
    "Artificial intelligence is changing the world rapidly.",
    "Coding is fun when you understand the concepts.",
    "Success comes from continuous learning and practice."
]

sentence = random.choice(sentences)

print("===================================")
print("      Typing Speed Test")
print("===================================")

print("\nType the following sentence:\n")
print(sentence)

input("\nPress Enter to start...")

start_time = time.time()

typed_text = input("\nStart typing:\n")

end_time = time.time()

time_taken = end_time - start_time

word_count = len(typed_text.split())
wpm = (word_count / time_taken) * 60

correct_chars = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

print("\n========== RESULT ==========")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Typing Speed : {wpm:.2f} WPM")
print(f"Accuracy : {accuracy:.2f}%")
print("============================")
