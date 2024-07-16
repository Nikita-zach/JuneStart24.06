rep_words=input("Enter repeated text>>>")
for i in range(1,len(rep_words) // 2 + 1):
    candidate=rep_words[:i]
    if candidate*(len(rep_words)//len(candidate))==rep_words:
        word=candidate
        break

print(f"Your word is - {word}")
