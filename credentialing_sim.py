import random
from datetime import datetime

def credentialing_game():
    # 1. Provider Database
    # Standard: Every provider must have an active License, DEA, and Board Cert.
    providers = [
        {"name": "Dr. Smith", "specialty": "Surgery", "license": True, "dea": True, "board_cert": True},
        {"name": "Dr. Jones", "specialty": "Internal Med", "license": False, "dea": True, "board_cert": True},
        {"name": "Dr. Miller", "specialty": "Pediatrics", "license": True, "dea": False, "board_cert": True},
        {"name": "Dr. Davis", "specialty": "Family Med", "license": True, "dea": True, "board_cert": False}
    ]

    score = 0
    active_privileges = []
    
    print("--- 📄 THE CREDENTIALING CRUCIBLE 📄 ---")
    print("Mission: Verify provider credentials to grant Hospital Privileges.")
    print("Rule: A doctor MUST have an active License AND DEA AND Board Cert to practice.")
    print("Granting privileges to an unverified doctor results in a 'Negligent Credentialing' lawsuit!")

    # 2. Game Loop
    for p in providers:
        print(f"\n--- 🔎 AUDITING: {p['name']} ({p['specialty']}) ---")
        print(f"1. State Medical License: {'[VALID]' if p['license'] else '[EXPIRED]'}")
        print(f"2. DEA Registration:     {'[VALID]' if p['dea'] else '[EXPIRED]'}")
        print(f"3. Board Certification:  {'[VALID]' if p['board_cert'] else '[EXPIRED]'}")
        
        decision = input("\nDo you grant 'Full Privileges' to this provider? (Y/N): ").strip().upper()

        # 3. Credentialing Logic
        # All three must be True for a safe 'Y'
        is_actually_valid = p['license'] and p['dea'] and p['board_cert']

        if decision == 'Y':
            if is_actually_valid:
                print(f"✅ SUCCESS: {p['name']} is now active in the directory.")
                active_privileges.append(p['name'])
                score += 10
            else:
                print(f"❌ NEGLIGENT CREDENTIALING: {p['name']} had an expired document!")
                print("The hospital is now liable for legal damages.")
                score -= 20
        elif decision == 'N':
            if not is_actually_valid:
                print(f"✅ CORRECT: You blocked {p['name']} until they update their documents.")
                score += 5
            else:
                print(f"❌ REVENUE LOSS: {p['name']} was fully qualified! You delayed their start date.")
                score -= 5

    # 4. Final Review
    print(f"\n--- 🏁 AUDIT COMPLETE ---")
    print(f"Final Compliance Score: {score}")
    print(f"Active Medical Staff: {', '.join(active_privileges) if active_privileges else 'None'}")
    
    if score >= 30:
        print("🏆 TOP COORDINATOR: Your medical staff directory is 100% compliant!")
    else:
        print("📋 RE-TRAINING REQUIRED: Your verification process has critical gaps.")

credentialing_game()
