
"""
H.E.L.I.O.S. - Agent Task Router
Prototype: keyword-based task classification.
"""

AGENT_KEYWORDS = {
    "CIPHER": [
        "crypto", "solana", "token", "wallet",
        "blockchain", "memecoin", "trading"
    ],
    "OSCAR": [
        "docker", "linux", "aws", "cloud",
        "terraform", "devops", "kubernetes"
    ],
    "GTM": [
        "sales", "prospect", "revenue", "lead",
        "customer", "pipeline", "outreach"
    ],
    "NOVA": [
        "research", "analyse", "analyze",
        "intelligence", "cybersecurity", "ai"
    ],
}


def route_task(task):
    """Select an agent based on keyword matches."""
    task = task.lower()

    scores = {
        agent: sum(
            keyword in task
            for keyword in keywords
        )
        for agent, keywords in AGENT_KEYWORDS.items()
    }

    best_agent = max(scores, key=scores.get)

    if scores[best_agent] == 0:
        return "NOVA"

    return best_agent


if __name__ == "__main__":
    print("H.E.L.I.O.S. Task Router")
    print("Type 'exit' to quit.")

    while True:
        task = input("\nEnter a task: ").strip()

        if task.lower() == "exit":
            break

        if not task:
            continue

        agent = route_task(task)
        print(f"Assigned agent: {agent}")
