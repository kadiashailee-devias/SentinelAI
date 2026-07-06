def validate_input(prompt: str):
    if not prompt.strip():
        return False, "Prompt cannot be empty."

    if len(prompt) > 5000:
        return False, "Prompt is too long."

    return True, ""