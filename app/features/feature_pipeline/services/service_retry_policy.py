# Bounded retry and rate-limit handling — one service with a single bounded responsibility.
# A deterministic 429 simulation: only retry the known transient response once.
def service_retry_policy(state: dict) -> dict:
    attempts = 0
    for status in (429, 200):
        attempts += 1
        if status == 200:
            break
    state["request_attempts"] = attempts
    state["retry_exhausted"] = status != 200
    return state
