from pydantic import BaseModel
from typing import Optional


class _Message(BaseModel):
    text: str
    ts: str


class _View(BaseModel):
    callback_id: str


class _Channel(BaseModel):
    id: str


class _User(BaseModel):
    id: str


class _Team(BaseModel):
    id: str


class Payload(BaseModel):
    type: str
    action_ts: str
    team: _Team
    user: _User
    channel: _Channel
    callback_id: Optional[str]
    view: Optional[_View]
    trigger_id: str
    response_url: str
    message_ts: str
    message: _Message
