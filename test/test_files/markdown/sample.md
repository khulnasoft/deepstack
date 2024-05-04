---
type: intro
date: 1.1.2023
---
```bash
pip install farm-deepstack
```
## What to build with Deepstack

- **Ask questions in natural language** and find granular answers in your own documents.
- Perform **semantic search** and retrieve documents according to meaning not keywords
- Use **off-the-shelf models** or **fine-tune** them to your own domain.
- Use **user feedback** to evaluate, benchmark and continuously improve your live models.
- Leverage existing **knowledge bases** and better handle the long tail of queries that **chatbots** receive.
- **Automate processes** by automatically applying a list of questions to new documents and using the extracted answers.

![Logo](https://raw.githubusercontent.com/khulnasoft/deepstack/main/docs/img/logo.png)


## Core Features

-   **Latest models**: Utilize all latest transformer based models (e.g. BERT, RoBERTa, MiniLM) for extractive QA, generative QA and document retrieval.
-   **Modular**: Multiple choices to fit your tech stack and use case. Pick your favorite database, file converter or modeling framework.
-   **Open**: 100% compatible with HuggingFace's model hub. Tight interfaces to other frameworks (e.g. Transformers, FARM, sentence-transformers)
-   **Scalable**: Scale to millions of docs via retrievers, production-ready backends like Elasticsearch / FAISS and a fastAPI REST API
-   **End-to-End**: All tooling in one place: file conversion, cleaning, splitting, training, eval, inference, labeling ...
-   **Developer friendly**: Easy to debug, extend and modify.
-   **Customizable**: Fine-tune models to your own domain or implement your custom DocumentStore.
-   **Continuous Learning**: Collect new training data via user feedback in production & improve your models continuously

|  |  |
|-|-|
| :ledger: [Docs](https://deepstack.khulnasoft.com/overview/intro) | Usage, Guides, API documentation ...|
| :beginner: [Quick Demo](https://github.com/khulnasoft/deepstack/#quick-demo) | Quickly see what Deepstack offers |
| :floppy_disk: [Installation](https://github.com/khulnasoft/deepstack/#installation) | How to install Deepstack |
| :art: [Key Components](https://github.com/khulnasoft/deepstack/#key-components) | Overview of core concepts |
| :mortar_board: [Tutorials](https://github.com/khulnasoft/deepstack/#tutorials) | Jupyter/Colab Notebooks & Scripts |
| :eyes: [How to use Deepstack](https://github.com/khulnasoft/deepstack/#how-to-use-deepstack) | Basic explanation of concepts, options and usage |
| :heart: [Contributing](https://github.com/khulnasoft/deepstack/#heart-contributing) | We welcome all contributions! |
| :bar_chart: [Benchmarks](https://deepstack.khulnasoft.com/benchmarks/v0.9.0) | Speed & Accuracy of Retriever, Readers and DocumentStores |
| :telescope: [Roadmap](https://deepstack.khulnasoft.com/overview/roadmap) | Public roadmap of Deepstack |
| :pray: [Slack](https://deepstack.khulnasoft.com/community/join) | Join our community on Slack |
| :bird: [Twitter](https://twitter.com/khulnasoft.com) | Follow us on Twitter for news and updates |
| :newspaper: [Blog](https://medium.com/khulnasoft) | Read our articles on Medium |


## Quick Demo

The quickest way to see what Deepstack offers is to start a [Docker Compose](https://docs.docker.com/compose/) demo application:

**1. Update/install Docker and Docker Compose, then launch Docker**

```
    # apt-get update && apt-get install docker && apt-get install docker-compose
    # service docker start
```

**2. Clone Deepstack repository**

```
    # git clone https://github.com/khulnasoft/deepstack.git
```

### 2nd level headline for testing purposes
#### 3rd level headline for testing purposes
