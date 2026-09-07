"""OpenAI-compatible Markdown translation service."""

from openai import OpenAI
import yaml


class TranslationService:
    """Translate Markdown while asking the model to preserve its syntax."""

    def __init__(self, client: OpenAI, model: str):
        self.client = client
        self.model = model

    def translate(self, title: str, body: str, source_language: str, target_language: str) -> tuple[str, str]:
        """Translate title and body without changing fences, links, or formulas."""
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Translate Markdown faithfully. Preserve front-matter-free Markdown, code fences, links, Mermaid fences, and LaTex formulas. Return JSON keys title and body."},
                {"role": "user", "content": f"Translate {source_language} to {target_language}.\n\nTitle:\n{title}\n\nMarkdown:\n{body}"},
            ],
        )
        payload = yaml.safe_load(response.choices[0].message.content or "") or {}
        return str(payload.get("title", title)), str(payload.get("body", body))
