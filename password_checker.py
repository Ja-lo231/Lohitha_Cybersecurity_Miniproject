#!/usr/bin/env python3
import re
import string

def check_password_strength(password):
    """Check the strength of a password and provide feedback"""
    score = 0
    feedback = []
    
    # Common weak passwords to check against
    common_passwords = [
        "password", "123456", "12345678", "1234", "qwerty", "letmein", "admin", "welcome", "monkey", "password1"
    ]
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Check for symbols
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password):
        score += 1
    else:
        feedback.append("❌ Add symbols (!@#$% etc.)")
    
    # Check against common passwords
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a very common password - choose something more unique")
    
    # Check for sequential characters
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("❌ Avoid repeating characters (aaa, 111 etc.)")
    
    # Determine strength level
    if score <= 2:
        strength = "Weak"
        color = "\033[91m"  # Red
    elif score == 3:
        strength = "Medium"
        color = "\033[93m"  # Yellow
    elif score == 4:
        strength = "Strong"
        color = "\033[92m"  # Green
    else:
        strength = "Very Strong"
        color = "\033[94m"  # Blue
    
    return strength, color, feedback, score

def main():
    """Main function to run the password strength checker"""
    print("\033[95m" + "=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50 + "\033[0m")
    print()
    
    while True:
        password = input("🔒 Enter your password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        if not password:
            print("⚠️  Please enter a password\n")
            continue
        
        # Check password strength
        strength, color, feedback, score = check_password_strength(password)
        
        # Display results
        print(f"\n📊 Password Analysis:")
        print(f"   Length: {len(password)} characters")
        print(f"   Strength: {color}{strength}\033[0m")
        print(f"   Score: {score}/5")
        
        # Show feedback
        if feedback:
            print(f"\n💡 Suggestions to improve:")
            for suggestion in feedback:
                print(f"   {suggestion}")
        else:
            print(f"\n✅ Excellent! Your password meets all security criteria!")
        
        # Additional tips for weak passwords
        if strength == "Weak":
            print(f"\n🔒 Tips for creating strong passwords:")
            print(f"   • Use at least 12 characters")
            print(f"   • Mix different character types")
            print(f"   • Avoid dictionary words and personal information")
            print(f"   • Consider using a passphrase")
        
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
