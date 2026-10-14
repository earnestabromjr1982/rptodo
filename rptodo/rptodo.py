"""This module provides the RP To-Do model-controller."""

# rptodo/rptodo.py

from typing import Any, NamedTuple


class CurrentTodo(NamedTuple):
    todo: dict[str, Any]
    error: int
