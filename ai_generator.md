---
layout: default
title: AI Recipe Generator
---

# 🍳 Yumlog Recipe Generator

Turn your cooking idea into a custom recipe — the Yumlog way.  
Type your idea into the assistant below, get 3 recipe options, and pick your favourite.

<div id="ai-generator" style="margin-top: 2rem;">
  <label for="idea"><strong>Enter a recipe idea:</strong></label><br>
  <input
    type="text"
    id="idea"
    placeholder="e.g. spicy chickpea curry"
    style="
      width: 100%;
      padding: 0.5rem;
      margin-top: 0.5rem;
      border: 1px solid var(--color-highlight);
      border-radius: 6px;
      background-color: var(--card-bg-light);
      color: var(--text-light);
      font-size: 1rem;
      font-family: inherit;"
  />
  <button
    onclick="getRecipe()"
    style="
      margin-top: 1rem;
      padding: 0.5rem 1rem;
      border: none;
      background-color: var(--color-primary);
      color: white;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
    ">
    Generate Recipe
  </button>
  <pre
    id="recipe-response"
    style="
      margin-top: 1.5rem;
      background: var(--card-bg-light);
      padding: 1rem;
      border-radius: 6px;
      white-space: pre-wrap;
      color: var(--text-light);
    ">
  </pre>
</div>

<script>
  async function getRecipe() {
    const input = document.getElementById('idea').value.trim();
    const output = document.getElementById('recipe-response');

    if (!input) {
      output.textContent = 'Please enter a recipe idea.';
      return;
    }

    output.textContent = 'Thinking...';

    try {
      const response = await fetch('https://yumlog.netlify.app/.netlify/functions/hello-world', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: input })
      });

      const data = await response.json();

      if (response.ok) {
        output.textContent = data.response;
      } else {
        output.textContent = data.error || 'Something went wrong.';
      }
    } catch (err) {
      output.textContent = 'Something went wrong.';
      console.error(err);
    }
  }
</script>

_Powered by AI. No login required. Free for anyone to use._