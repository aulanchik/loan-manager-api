import time
from collections import defaultdict

_requests = defaultdict(list)
MAX_REQUESTS_PER_SECOND = 3

def is_rate_limited(country_code: str) -> bool:
    now = time.time()
    window = 1.0

    timestamps = _requests[country_code]
    _requests[country_code] = [t for t in timestamps if now - t < window]
    
    print(f"[DEBUG] Requests for {country_code}: {len(_requests[country_code])}")

    if len(_requests[country_code]) >= MAX_REQUESTS_PER_SECOND:
        return True

    _requests[country_code].append(now)
    return False
