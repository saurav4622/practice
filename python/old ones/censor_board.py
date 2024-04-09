from better_profanity import profanity
text=input("enter text here: ")
censored_text=profanity.censor(text)
print(f"censored_text: {censored_text}")