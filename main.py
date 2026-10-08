
from datetime import datetime

AGENTS = {
    "nova": "AI Intelligence & Research",
    "oscar": "DevSecOps & Cloud Automation",
    "cipher": "Crypto & Blockchain Intelligence",
    "gtm": "Revenue & Sales Intelligence",
}


def main():
    print("=" * 45)
    print("H.E.L.I.O.S. | AI Orchestration Prototype")
    print("=" * 45)
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}")

    print("\nRegistered agents:")
    for name, description in AGENTS.items():
        print(f"  {name.upper()}: {description}")

    print("\nSystem status: Prototype initialised")
    print("Note: Agent execution is not yet implemented.")


if __name__ == "__main__":
    main()
