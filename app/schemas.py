from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

Priority = Literal["low", "medium", "high"]
Status = Literal["open", "in_progress", "resolved", "closed"]

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=6, max_length=100)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str

class LoginRequest(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ServiceRequestCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5, max_length=2000)
    priority: Priority = "medium"

class ServiceRequestUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = Field(default=None, min_length=5, max_length=2000)
    priority: Priority | None = None

class StatusUpdate(BaseModel):
    status: Status

class ServiceRequestResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_at: datetime
    user_id: int
