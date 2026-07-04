"""
Data validation models using Pydantic.
"""

from pydantic import BaseModel, Field, field_validator

from backend.arena.captcha import verify_altcha_token
from backend.arena.legal_tools.mcp_servers import AVAILABLE_MCP_SERVERS
from backend.arena.legal_tools.skills import AVAILABLE_SKILLS
from backend.arena.spam_detection import is_spam
from backend.config import (
    BLIND_MODE_INPUT_CHAR_LEN_LIMIT,
    DEFAULT_SELECTION_MODE,
    CustomModelsSelection,
    SelectionMode,
    settings,
)

# Request/Response models for FastAPI endpoints
PromptField = Field(min_length=1, max_length=BLIND_MODE_INPUT_CHAR_LEN_LIMIT)


class AddFirstTextBody(BaseModel):
    """Request body for add_first_text endpoint."""

    prompt_value: str = PromptField
    mode: SelectionMode = DEFAULT_SELECTION_MODE
    custom_models_selection: CustomModelsSelection = None
    # We force cohorts not to be None to make sure cohorts detection has been called on frontend
    cohorts: str
    altcha_token: str
    web_search: bool = False
    enabled_skills: tuple[str, ...] = ()
    enabled_mcp_servers: tuple[str, ...] = ()

    @field_validator("prompt_value")
    @classmethod
    def check_spam(cls, v: str) -> str:
        if is_spam(v):
            raise ValueError(
                "This prompt format is not allowed. Please use natural language."
            )
        return v

    @field_validator("altcha_token")
    @classmethod
    def check_altcha(cls, v: str) -> str:
        ok, error = verify_altcha_token(v)
        if not ok:
            raise ValueError(f"Vérification anti-robot échouée : {error}")
        return v

    @field_validator("enabled_skills", "enabled_mcp_servers")
    @classmethod
    def check_legal_tools_brand(cls, v: tuple[str, ...]) -> tuple[str, ...]:
        if v and settings.PUBLIC_BRAND != "juridique":
            raise ValueError("Skills/MCP servers are only available on this instance.")
        return v

    @field_validator("enabled_skills")
    @classmethod
    def check_known_skills(cls, v: tuple[str, ...]) -> tuple[str, ...]:
        if unknown := set(v) - AVAILABLE_SKILLS.keys():
            raise ValueError(f"Unknown skill id(s): {unknown}")
        return v

    @field_validator("enabled_mcp_servers")
    @classmethod
    def check_known_mcp_servers(cls, v: tuple[str, ...]) -> tuple[str, ...]:
        if unknown := set(v) - AVAILABLE_MCP_SERVERS.keys():
            raise ValueError(f"Unknown MCP server id(s): {unknown}")
        return v


class AddTextBody(BaseModel):
    """Request body for add_text endpoint."""

    message: str = PromptField
    altcha_token: str

    @field_validator("message")
    @classmethod
    def check_spam(cls, v: str) -> str:
        if is_spam(v):
            raise ValueError(
                "This prompt format is not allowed. Please use natural language."
            )
        return v

    @field_validator("altcha_token")
    @classmethod
    def check_altcha(cls, v: str) -> str:
        ok, error = verify_altcha_token(v)
        if not ok:
            raise ValueError(f"Vérification anti-robot échouée : {error}")
        return v
