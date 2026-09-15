import json
import sys
import urllib.request
import argparse
from pathlib import Path

DEFAULT_PIN = Path(__file__).resolve().parent / "pin.json"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8000/health", help="Health check URL")
    parser.add_argument("--pin", type=Path, default=DEFAULT_PIN, help="Prompt pin JSON file")
    args = parser.parse_args()

    # TODO 1: load expected prompt_version + prompt_sha256 from pin.json
    try:
        with args.pin.open(encoding="utf-8") as f:
            pin = json.load(f)
            expected_version = pin.get("prompt_version")
            expected_hash = pin.get("prompt_sha256")
    except Exception as e:
        print(f"❌ Could not load pin.json: {e}")
        sys.exit(1)

    # TODO 2: GET health endpoint
    try:
        with urllib.request.urlopen(args.url) as resp:
            if resp.status != 200:
                print(f"❌ Health check failed: HTTP {resp.status}")
                sys.exit(1)
            health_data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"❌ Could not reach health endpoint: {e}")
        sys.exit(1)

    # TODO 3: compare version AND hash
    health_version = health_data.get("prompt_version")
    health_hash = health_data.get("prompt_sha256")

    if health_version == expected_version and health_hash == expected_hash:
        print("✅ Match: version and hash are correct")
        sys.exit(0)
    else:
        print("❌ Mismatch detected:")
        print(f"   Expected version={expected_version}, hash={expected_hash}")
        print(f"   Got version={health_version}, hash={health_hash}")
        sys.exit(1)

if __name__ == "__main__":
    main()
