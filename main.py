
from datetime import datetime
from router import route_task

AGENTS = {
    "NOVA": "AI Intelligence & Research",
    "OSCAR": "DevSecOps & Cloud Automation",
    "CIPHER": "Crypto & Blockchain Intelligence",
    "GTM": "Revenue & Sales Intelligence",
}


def main():
    print("=" * 45)
    print("H.E.L.I.O.S. | AI Orchestration Prototype")
    print("=" * 45)
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}")

    print("\nRegistered agents:")
    for name, description in AGENTS.items():
        print(f"  {name}: {description}")

    print("\nTask routing system ready.")
    print("Type 'exit' to quit.")

    while True:
        task = input("\nEnter your task: ").strip()

        if task.lower() == "exit":
            print("H.E.L.I.O.S. shutting down.")
            break

        if not task:
            continue

        agent = route_task(task)

        print(f"\nSelected agent: {agent}")
        print(f"Specialisation: {AGENTS[agent]}")
        print("Status: Task classified (execution not implemented)")


if __name__ == "__main__":
    main()

