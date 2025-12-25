import re

def check_password_strength(password):
    """
    Assess the strength of a password based on length, character types, etc.
    Returns the strength level and feedback messages.
    """
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) < 8:
        feedback.append("Password is too short (should be at least 8 characters).")
    else:
        score += 1
        if len(password) >= 12:
            score += 1  # Extra point for good length

    # Criteria 2: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letters.")

    # Criteria 3: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letters.")

    # Criteria 4: Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Missing numbers.")

    # Criteria 5: Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing special characters (e.g., !@#$%).")

    # Determine Strength Level
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"
        if len(password) >= 16: # Bonus check for "Very Strong" label
             strength = "Very Strong"

    return strength, feedback

def main():
    print("--- Password Strength Assessment Tool ---")
    while True:
        password = input("\nEnter a password to assess (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        strength, feedback = check_password_strength(password)
        
        print("\nAssessment Result:")
        print(f"Strength: {strength}")
        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Excellent! Your password meets all the criteria.")
            
        print("-" * 30)

if __name__ == "__main__":
    main()
