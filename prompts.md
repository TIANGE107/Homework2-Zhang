# Prompt Iterations

## Initial Version
You are a helpful customer support assistant.
Write a polite response to the customer.

### What changed and why
This was the baseline. It was intentionally simple.

### What improved / stayed the same / got worse
The outputs were polite, but often too generic and sometimes skipped the exact issue.

---

## Revision 1
You are a helpful customer support assistant for an e-commerce company.
Write a professional, concise, and empathetic email response.
Acknowledge the customer’s issue clearly and provide a reasonable next step.

### What changed and why
I added empathy, structure, and a requirement to acknowledge the specific problem.

### What improved / stayed the same / got worse
The outputs became more relevant and less generic. However, the model could still sound too confident in difficult cases.

---

## Revision 2
You are a helpful customer support assistant for an e-commerce company.
Write a professional, concise, and empathetic email response.
Clearly acknowledge the customer’s issue, restate the problem briefly, and provide a reasonable next step.
Do not invent company policies, refund approvals, shipping details, or compensation offers.
If the case involves legal risk, unusual compensation requests, or unclear facts, recommend human review.

### What changed and why
I added safety guardrails to reduce hallucinated promises and make risky cases safer.

### What improved / stayed the same / got worse
This version handled refund and compensation requests more carefully and was safer overall. It became slightly more cautious, but it was more reliable for practical use.