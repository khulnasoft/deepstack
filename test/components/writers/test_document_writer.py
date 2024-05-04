import pytest

from deepstack import Document, DeserializationError
from deepstack.testing.factory import document_store_class
from deepstack.components.writers.document_writer import DocumentWriter
from deepstack.document_stores.types import DuplicatePolicy
from deepstack.document_stores.in_memory import InMemoryDocumentStore


class TestDocumentWriter:
    def test_to_dict(self):
        mocked_docstore_class = document_store_class("MockedDocumentStore")
        component = DocumentWriter(document_store=mocked_docstore_class())
        data = component.to_dict()
        assert data == {
            "type": "deepstack.components.writers.document_writer.DocumentWriter",
            "init_parameters": {
                "document_store": {"type": "deepstack.testing.factory.MockedDocumentStore", "init_parameters": {}},
                "policy": "NONE",
            },
        }

    def test_to_dict_with_custom_init_parameters(self):
        mocked_docstore_class = document_store_class("MockedDocumentStore")
        component = DocumentWriter(document_store=mocked_docstore_class(), policy=DuplicatePolicy.SKIP)
        data = component.to_dict()
        assert data == {
            "type": "deepstack.components.writers.document_writer.DocumentWriter",
            "init_parameters": {
                "document_store": {"type": "deepstack.testing.factory.MockedDocumentStore", "init_parameters": {}},
                "policy": "SKIP",
            },
        }

    def test_from_dict(self):
        data = {
            "type": "deepstack.components.writers.document_writer.DocumentWriter",
            "init_parameters": {
                "document_store": {
                    "type": "deepstack.document_stores.in_memory.document_store.InMemoryDocumentStore",
                    "init_parameters": {},
                },
                "policy": "SKIP",
            },
        }
        component = DocumentWriter.from_dict(data)
        assert isinstance(component.document_store, InMemoryDocumentStore)
        assert component.policy == DuplicatePolicy.SKIP

    def test_from_dict_without_docstore(self):
        data = {"type": "DocumentWriter", "init_parameters": {}}
        with pytest.raises(DeserializationError, match="Missing 'document_store' in serialization data"):
            DocumentWriter.from_dict(data)

    def test_from_dict_without_docstore_type(self):
        data = {"type": "DocumentWriter", "init_parameters": {"document_store": {"init_parameters": {}}}}
        with pytest.raises(DeserializationError, match="Missing 'type' in document store's serialization data"):
            DocumentWriter.from_dict(data)

    def test_from_dict_nonexisting_docstore(self):
        data = {
            "type": "DocumentWriter",
            "init_parameters": {"document_store": {"type": "Nonexisting.DocumentStore", "init_parameters": {}}},
        }
        with pytest.raises(DeserializationError):
            DocumentWriter.from_dict(data)

    def test_run(self):
        document_store = InMemoryDocumentStore()
        writer = DocumentWriter(document_store)
        documents = [
            Document(content="This is the text of a document."),
            Document(content="This is the text of another document."),
        ]

        result = writer.run(documents=documents)
        assert result["documents_written"] == 2

    def test_run_skip_policy(self):
        document_store = InMemoryDocumentStore()
        writer = DocumentWriter(document_store, policy=DuplicatePolicy.SKIP)
        documents = [
            Document(content="This is the text of a document."),
            Document(content="This is the text of another document."),
        ]

        result = writer.run(documents=documents)
        assert result["documents_written"] == 2

        result = writer.run(documents=documents)
        assert result["documents_written"] == 0
