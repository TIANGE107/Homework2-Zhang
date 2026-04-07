import json

SYSTEM_PROMPT = """
You are a helpful customer support assistant for an e-commerce company.
Write a professional, concise, and empathetic email response.
Clearly acknowledge the customer’s issue, restate the problem briefly, and provide a reasonable next step.
Do not invent company policies, refund approvals, shipping details, or compensation offers.
If the case involves legal risk, unusual compensation requests, or unclear facts, recommend human review.
""".strip()


def load_eval_set(path="eval_set.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_outputs(outputs, path="outputs.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(outputs, f, indent=2, ensure_ascii=False)


def main():
    cases = load_eval_set()
    outputs = []

    print("\nCodex-assisted workflow runner")
    print("For each case below, paste the response generated with Codex after signing in with ChatGPT.\n")
    print("System prompt to use:\n")
    print(SYSTEM_PROMPT)
    print("\n" + "=" * 80 + "\n")

    for case in cases:
        print(f"CASE {case['id']} ({case['type']})")
        print("Customer message:")
        print(case["customer_message"])
        print("\nGood output note:")
        print(case["good_output_note"])
        print("\nUse the system prompt above in Codex, generate a reply, then paste it below.")
        print("When finished, type END on its own line.\n")

        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)

        model_response = "\n".join(lines).strip()

        outputs.append(
            {
                "id": case["id"],
                "type": case["type"],
                "customer_message": case["customer_message"],
                "model_response": model_response,
                "good_output_note": case["good_output_note"],
            }
        )

        save_outputs(outputs)
        print(f"\nSaved case {case['id']} to outputs.json")
        print("\n" + "=" * 80 + "\n")

    print("All cases completed. Final outputs saved to outputs.json")


if __name__ == "__main__":
    main()