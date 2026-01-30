# At least 8 characters long :)
# At least one lower case :)
# At least one upper case :)
# At least one number :)
# At least one of these special digits: @?!#*£$=+-

approved_special = "@?!#*£$=+-"

def strong_password(password):
    if len(password) < 8:
        return "FAIL"
    
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    
    if not (lower and upper and digit):
        return "FAIL"
    
    contains_approved = False

    for c in password:
        if not c.isalnum():
            if c in approved_special:
                contains_approved = True
            else:
                return "FAIL"

    if contains_approved:
        return "PASS"
    else: "FAIL"
