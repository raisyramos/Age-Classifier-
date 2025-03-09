def classify_age(age):
    if age < 0:
        print("Invalid age entered.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

classify_age(17)
classify_age(23)
classify_age(10)
classify_age(51)