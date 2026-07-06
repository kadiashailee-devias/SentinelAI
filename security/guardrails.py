BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "reveal system prompt",
    "show api key",
    "bypass security",
]

def is_safe_prompt(prompt: str) -> bool:
    prompt = prompt.lower()
    return not any(pattern in prompt for pattern in BLOCKED_PATTERNS)