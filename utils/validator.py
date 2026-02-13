from email_validator import validate_email, EmailNotValidError


def normalize_email(email: str) -> str:
    """
    Normalize and validate email.
    Returns normalized lowercase email if valid.
    Raises ValueError if invalid.
    """
    if not email:
        raise ValueError("Email is empty")

    email = email.strip()

    try:
        validated = validate_email(email)
        return validated.email.lower()
    except EmailNotValidError as e:
        raise ValueError(str(e))



def is_valid_email(email: str) -> bool:
    """
    Returns True if email is valid, False otherwise.
    """
    try:
        normalize_email(email)
        return True
    except ValueError:
        return False
