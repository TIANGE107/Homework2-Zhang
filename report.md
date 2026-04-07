# Report

## Business Use Case
This project explores using an LLM-assisted workflow to draft first-pass customer support emails for an e-commerce business. Support agents often spend time writing repetitive responses to common issues such as delayed deliveries, wrong items, damaged packages, and refund requests.

## Model / Tool Choice
I used Codex with ChatGPT sign-in instead of direct API billing. This choice allowed me to prototype the workflow without setting up separate API credits. The Python script still provides a reproducible command-line workflow, while Codex is used to generate the draft responses.

## Baseline vs. Final Design
The baseline prompt produced polite but generic answers. After two prompt revisions, the final prompt improved the outputs by requiring empathy, issue acknowledgment, concise next steps, and safety constraints against unsupported promises.

## Where the Prototype Still Fails
The prototype can still fail when customer messages involve legal threats, compensation demands, or missing business context. In those cases, the model may produce reasonable-sounding text that still requires human review.

## Deployment Recommendation
I would recommend this workflow only as a draft-assistance tool with human review. It should not be used to automatically send replies in sensitive or ambiguous cases.

## Limitation
This prototype uses Codex with ChatGPT authentication rather than a direct API-billed application call. That made the workflow accessible for this assignment setup, but it is a limitation compared with a fully automated API-based deployment.