import copy
import typing
from typing import List, Dict

from deepstack.dataclasses import ChatMessage
from deepstack.components.routers.conditional_router import serialize_type, deserialize_type


def test_output_type_serialization():
    assert serialize_type(str) == "str"
    assert serialize_type(List[int]) == "typing.List[int]"
    assert serialize_type(List[Dict[str, int]]) == "typing.List[typing.Dict[str, int]]"
    assert serialize_type(ChatMessage) == "deepstack.dataclasses.chat_message.ChatMessage"
    assert serialize_type(typing.List[Dict[str, int]]) == "typing.List[typing.Dict[str, int]]"
    assert serialize_type(List[ChatMessage]) == "typing.List[deepstack.dataclasses.chat_message.ChatMessage]"
    assert (
        serialize_type(typing.Dict[int, ChatMessage])
        == "typing.Dict[int, deepstack.dataclasses.chat_message.ChatMessage]"
    )
    assert serialize_type(int) == "int"
    assert serialize_type(ChatMessage.from_user("ciao")) == "deepstack.dataclasses.chat_message.ChatMessage"


def test_output_type_deserialization():
    assert deserialize_type("str") == str
    assert deserialize_type("typing.List[int]") == typing.List[int]
    assert deserialize_type("typing.List[typing.Dict[str, int]]") == typing.List[Dict[str, int]]
    assert deserialize_type("typing.Dict[str, int]") == Dict[str, int]
    assert deserialize_type("typing.Dict[str, typing.List[int]]") == Dict[str, List[int]]
    assert deserialize_type("typing.List[typing.Dict[str, typing.List[int]]]") == List[Dict[str, List[int]]]
    assert deserialize_type("typing.List[deepstack.dataclasses.chat_message.ChatMessage]") == typing.List[ChatMessage]
    assert (
        deserialize_type("typing.Dict[int, deepstack.dataclasses.chat_message.ChatMessage]")
        == typing.Dict[int, ChatMessage]
    )
    assert deserialize_type("deepstack.dataclasses.chat_message.ChatMessage") == ChatMessage
    assert deserialize_type("int") == int
