---
title: Prompt Engineering 101
linkTitle: Prompt Engineering 101
date: '2025-05-06T14:19:00Z'
weight: 1
description: Learn effective prompt engineering techniques for ChatGPT, focusing on
  context, role assignment, examples, constraints, and iteration to improve outputs
  across various use cases in development and non-development tasks.
draft: false
---


## 🎯 Goal

Learn how to write better prompts to get the most out of ChatGPT and similar tools — for all kinds of tasks, not just coding.

<!-- Unsupported block type: divider -->

## 🚀 Why This Matters

Most people write prompts like this:

> “Explain X”

That’s the equivalent of Googling "stuff".

Let’s go pro.

<!-- Unsupported block type: divider -->

## 📦 Core Concepts of Prompting

### 1. Context is King

LLMs love context. The more you give, the better the output.

> ❌ “Write a blog post about AI.”

> ✅ “You're a senior backend dev at MarsBased. Given this GitHub issue, propose 3 implementation options with tradeoffs.”

<!-- Unsupported block type: divider -->

### 2. Role Assignment

> “You're a senior full-stack dev.”

Roles change everything. Try it.

<!-- Unsupported block type: divider -->

### 3. Examples > Explanations

Few-shot prompting is powerful.

> ❌ “Write me an error message.”

<!-- Unsupported block type: divider -->

### 4. Constraints Help

> “Explain this like I’m five.”

Constraints = better outputs.

<!-- Unsupported block type: divider -->

### 5. Iterate, Don’t Expect Magic

You’re allowed to keep going:

> “That’s too long. Can you shorten it?”

LLMs love feedback.

<!-- Unsupported block type: divider -->

## 🔧 Dev Use Cases

- 🔍 Debugging:

- 📄 PR Summaries:

- 🧠 Naming things:

- 📜 Commit messages:

- 🤖 GitHub Copilot prompts:

<!-- Unsupported block type: divider -->

## 💼 Non-Dev Use Cases

- ✍️ Docs:

- 📣 Marketing:

- 📅 Planning:

- 🧑‍🏫 Hiring:

<!-- Unsupported block type: divider -->

## ⚙️ Bonus: API-Level Prompting (1 Minute)

If using OpenAI's API:

```json
{
  "model": "gpt-4",
  "temperature": 0.7,
  "messages": [
    { "role": "system", "content": "You are a senior Rails developer." },
    { "role": "user", "content": "Explain the pros and cons of Hotwire." }
  ]
}

```

- system: Sets the role/persona

- user: The actual prompt

- temperature: 0 = deterministic, 1 = creative/random

## 🎁 Cheat Code: Prompt Structure

- [Persona or role]

- [Clear task]

- [Context]

- [Constraints]

- [Optional: examples]

- [Optional: output formatting]

🔥