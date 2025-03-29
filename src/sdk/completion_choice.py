"""
completion_choice automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .completion_message import CompletionMessage
from .completion_message_developer import CompletionMessageDeveloper
from .completion_message_system import CompletionMessageSystem
from .completion_message_user import CompletionMessageUser
from .completion_message_assistant import CompletionMessageAssistant
from .completion_message_tool import CompletionMessageTool


class CompletionChoice(BaseModel):
    index: Optional[int] = Field(default=None, alias="index")
    message: Optional[Annotated[Union[Annotated[CompletionMessageDeveloper, Tag('developer')], Annotated[CompletionMessageSystem, Tag('system')], Annotated[CompletionMessageUser, Tag('user')], Annotated[CompletionMessageAssistant, Tag('assistant')], Annotated[CompletionMessageTool, Tag('tool')]], Field(discriminator='role')]] = Field(default=None, alias="message")
    finish_reason: Optional[str] = Field(default=None, alias="finish_reason")
    pass


