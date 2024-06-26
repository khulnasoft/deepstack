import pytest

from deepstack.components.builders.prompt_builder import PromptBuilder


def test_init():
    builder = PromptBuilder(template="This is a {{ variable }}")
    assert builder._template_string == "This is a {{ variable }}"


def test_to_dict():
    builder = PromptBuilder(template="This is a {{ variable }}")
    res = builder.to_dict()
    assert res == {
        "type": "deepstack.components.builders.prompt_builder.PromptBuilder",
        "init_parameters": {"template": "This is a {{ variable }}"},
    }


def test_run():
    builder = PromptBuilder(template="This is a {{ variable }}")
    res = builder.run(variable="test")
    assert res == {"prompt": "This is a test"}


def test_run_without_input():
    builder = PromptBuilder(template="This is a template without input")
    res = builder.run()
    assert res == {"prompt": "This is a template without input"}


def test_run_with_missing_input():
    builder = PromptBuilder(template="This is a {{ variable }}")
    res = builder.run()
    assert res == {"prompt": "This is a "}


def test_run_with_missing_required_input():
    builder = PromptBuilder(template="This is a {{ foo }}, not a {{ bar }}", required_variables=["foo", "bar"])
    with pytest.raises(ValueError, match="foo"):
        builder.run(bar="bar")
    with pytest.raises(ValueError, match="bar"):
        builder.run(foo="foo")
    with pytest.raises(ValueError, match="foo, bar"):
        builder.run()
