"""
SentinelAI Security Guardrails
"""

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "reveal system prompt",
    "show system prompt",
    "show api key",
    "api key",
    "bypass security",
    "bypass safety",
    "disable safety",
    "developer instructions",
    "hidden prompt",
    "print environment variables",
    "steal credentials",
]


def is_safe_prompt(prompt: str) -> bool:
    """
    Returns True if prompt is safe.
    Returns False if prompt contains prompt-injection patterns.
    """

    if not prompt:
        return True

    text = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            return False

    return True


def get_block_reason(prompt: str):
    """
    Returns matched blocked pattern.
    """

    if not prompt:
        return None

    text = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            return pattern

    return None