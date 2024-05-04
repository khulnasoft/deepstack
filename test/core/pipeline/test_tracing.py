from test.tracing.utils import SpyingSpan, SpyingTracer
from typing import Optional
from unittest.mock import ANY

import pytest
from _pytest.monkeypatch import MonkeyPatch

from deepstack import Pipeline, component
from deepstack.tracing.tracer import tracer


@component
class Hello:
    @component.output_types(output=str)
    def run(self, word: Optional[str]):  # use optional to spice up the typing tags
        """
        Takes a string in input and returns "Hello, <string>!"
        in output.
        """
        return {"output": f"Hello, {word}!"}


@pytest.fixture()
def pipeline() -> Pipeline:
    pipeline = Pipeline()
    pipeline.add_component("hello", Hello())
    pipeline.add_component("hello2", Hello())
    pipeline.connect("hello.output", "hello2.word")
    return pipeline


class TestTracing:
    def test_with_enabled_tracing(self, pipeline: Pipeline, spying_tracer: SpyingTracer) -> None:
        pipeline.run(data={"word": "world"})

        assert len(spying_tracer.spans) == 3

        assert spying_tracer.spans == [
            SpyingSpan(
                operation_name="deepstack.pipeline.run",
                tags={
                    "deepstack.pipeline.input_data": {"hello": {"word": "world"}},
                    "deepstack.pipeline.output_data": {"hello2": {"output": "Hello, Hello, world!!"}},
                    "deepstack.pipeline.debug": False,
                    "deepstack.pipeline.metadata": {},
                    "deepstack.pipeline.max_loops_allowed": 100,
                },
                trace_id=ANY,
                span_id=ANY,
            ),
            SpyingSpan(
                operation_name="deepstack.component.run",
                tags={
                    "deepstack.component.name": "hello",
                    "deepstack.component.type": "Hello",
                    "deepstack.component.input_types": {"word": "str"},
                    "deepstack.component.input_spec": {"word": {"type": ANY, "senders": []}},
                    "deepstack.component.output_spec": {"output": {"type": "str", "senders": ["hello2"]}},
                    "deepstack.component.visits": 1,
                },
                trace_id=ANY,
                span_id=ANY,
            ),
            SpyingSpan(
                operation_name="deepstack.component.run",
                tags={
                    "deepstack.component.name": "hello2",
                    "deepstack.component.type": "Hello",
                    "deepstack.component.input_types": {"word": "str"},
                    "deepstack.component.input_spec": {"word": {"type": ANY, "senders": ["hello"]}},
                    "deepstack.component.output_spec": {"output": {"type": "str", "senders": []}},
                    "deepstack.component.visits": 1,
                },
                trace_id=ANY,
                span_id=ANY,
            ),
        ]

        # We need to check the type of the input_spec because it can be rendered differently
        # depending on the Python version 🫠
        assert spying_tracer.spans[1].tags["deepstack.component.input_spec"]["word"]["type"] in [
            "typing.Union[str, NoneType]",
            "typing.Optional[str]",
        ]

    def test_with_enabled_content_tracing(
        self, spying_tracer: SpyingTracer, monkeypatch: MonkeyPatch, pipeline: Pipeline
    ) -> None:
        # Monkeypatch to avoid impact on other tests
        monkeypatch.setattr(tracer, "is_content_tracing_enabled", True)

        pipeline.run(data={"word": "world"})

        assert len(spying_tracer.spans) == 3
        assert spying_tracer.spans == [
            SpyingSpan(
                operation_name="deepstack.pipeline.run",
                tags={
                    "deepstack.pipeline.debug": False,
                    "deepstack.pipeline.metadata": {},
                    "deepstack.pipeline.max_loops_allowed": 100,
                    "deepstack.pipeline.input_data": {"hello": {"word": "world"}},
                    "deepstack.pipeline.output_data": {"hello2": {"output": "Hello, Hello, world!!"}},
                },
                trace_id=ANY,
                span_id=ANY,
            ),
            SpyingSpan(
                operation_name="deepstack.component.run",
                tags={
                    "deepstack.component.name": "hello",
                    "deepstack.component.type": "Hello",
                    "deepstack.component.input_types": {"word": "str"},
                    "deepstack.component.input_spec": {"word": {"type": ANY, "senders": []}},
                    "deepstack.component.output_spec": {"output": {"type": "str", "senders": ["hello2"]}},
                    "deepstack.component.input": {"word": "world"},
                    "deepstack.component.visits": 1,
                    "deepstack.component.output": {"output": "Hello, world!"},
                },
                trace_id=ANY,
                span_id=ANY,
            ),
            SpyingSpan(
                operation_name="deepstack.component.run",
                tags={
                    "deepstack.component.name": "hello2",
                    "deepstack.component.type": "Hello",
                    "deepstack.component.input_types": {"word": "str"},
                    "deepstack.component.input_spec": {"word": {"type": ANY, "senders": ["hello"]}},
                    "deepstack.component.output_spec": {"output": {"type": "str", "senders": []}},
                    "deepstack.component.input": {"word": "Hello, world!"},
                    "deepstack.component.visits": 1,
                    "deepstack.component.output": {"output": "Hello, Hello, world!!"},
                },
                trace_id=ANY,
                span_id=ANY,
            ),
        ]
