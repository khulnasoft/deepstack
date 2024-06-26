import sys
from unittest.mock import Mock

import pytest

from deepstack.core.pipeline import Pipeline
from deepstack.core.component import component
from deepstack.core.errors import DeserializationError
from deepstack.testing import factory
from deepstack.core.serialization import default_to_dict, default_from_dict, generate_qualified_class_name


def test_default_component_to_dict():
    MyComponent = factory.component_class("MyComponent")
    comp = MyComponent()
    res = default_to_dict(comp)
    assert res == {"type": "deepstack.testing.factory.MyComponent", "init_parameters": {}}


def test_default_component_to_dict_with_init_parameters():
    MyComponent = factory.component_class("MyComponent")
    comp = MyComponent()
    res = default_to_dict(comp, some_key="some_value")
    assert res == {"type": "deepstack.testing.factory.MyComponent", "init_parameters": {"some_key": "some_value"}}


def test_default_component_from_dict():
    def custom_init(self, some_param):
        self.some_param = some_param

    extra_fields = {"__init__": custom_init}
    MyComponent = factory.component_class("MyComponent", extra_fields=extra_fields)
    comp = default_from_dict(
        MyComponent, {"type": "deepstack.testing.factory.MyComponent", "init_parameters": {"some_param": 10}}
    )
    assert isinstance(comp, MyComponent)
    assert comp.some_param == 10


def test_default_component_from_dict_without_type():
    with pytest.raises(DeserializationError, match="Missing 'type' in serialization data"):
        default_from_dict(Mock, {})


def test_default_component_from_dict_unregistered_component(request):
    # We use the test function name as component name to make sure it's not registered.
    # Since the registry is global we risk to have a component with the same name registered in another test.
    component_name = request.node.name

    with pytest.raises(DeserializationError, match=f"Class '{component_name}' can't be deserialized as 'Mock'"):
        default_from_dict(Mock, {"type": component_name})


def test_from_dict_import_type():
    pipeline_dict = {
        "metadata": {},
        "max_loops_allowed": 100,
        "components": {
            "greeter": {
                "type": "deepstack.testing.sample_components.greet.Greet",
                "init_parameters": {
                    "message": "\nGreeting component says: Hi! The value is {value}\n",
                    "log_level": "INFO",
                },
            }
        },
        "connections": [],
    }

    # remove the target component from the registry if already there
    component.registry.pop("deepstack.testing.sample_components.greet.Greet", None)
    # remove the module from sys.modules if already there
    sys.modules.pop("deepstack.testing.sample_components.greet", None)

    p = Pipeline.from_dict(pipeline_dict)

    from deepstack.testing.sample_components.greet import Greet

    assert type(p.get_component("greeter")) == Greet


def test_get_qualified_class_name():
    MyComponent = factory.component_class("MyComponent")
    comp = MyComponent()
    res = generate_qualified_class_name(type(comp))
    assert res == "deepstack.testing.factory.MyComponent"
