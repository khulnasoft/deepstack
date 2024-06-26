<p align="center">
  <a href="https://deepstack.khulnasoft.com/"><img src="https://raw.githubusercontent.com/khulnasoft/.github/main/deepstack-logo-colored.png" alt="Deepstack by khulnasoft"></a>
</p>

[Deepstack](https://github.com/khulnasoft/deepstack) is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Whether you want to perform retrieval-augmented generation (RAG), document search, question answering or answer generation, Deepstack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case.

## Deepstack 2.0

For the latest version of Deepstack there's only one image available:

- `deepstack:base-<version>` contains a working Python environment with Deepstack preinstalled. This image is expected to
  be derived `FROM`.

## Deepstack 1.x image variants

The Docker image for Deepstack 1.x comes in six variants:
- `deepstack:gpu-<version>` contains Deepstack dependencies as well as what's needed to run the REST API and UI. It comes with the CUDA runtime and is capable of running on GPUs.
- `deepstack:cpu-remote-inference-<version>` is a slimmed down version of the CPU image with the REST API and UI. It is specifically designed for PromptNode inferencing using remotely hosted models, such as Hugging Face Inference, OpenAI, Cohere, Anthropic, and similar.
- `deepstack:cpu-<version>` contains Deepstack dependencies as well as what's needed to run the REST API and UI. It has no support for GPU so must be run on CPU.
- `deepstack:base-gpu-<version>` only contains the Deepstack dependencies. It comes with the CUDA runtime and can run on GPUs.
- `deepstack:base-cpu-remote-inference-<version>` is a slimmed down version of the CPU image, specifically designed for PromptNode inferencing using remotely hosted models, such as Hugging Face Inference, OpenAI, Cohere, Anthropic, and similar.
- `deepstack:base-cpu-<version>` only contains the Deepstack dependencies. It has no support for GPU so must be run on CPU.

## Image Development

Images are built with BuildKit and we use `bake` to orchestrate the process.
You can build a specific image by running:
```sh
docker buildx bake gpu
```

You can override any `variable` defined in the `docker-bake.hcl` file and build custom
images, for example if you want to use a branch from the Deepstack repo, run:
```sh
DEEPSTACK_VERSION=mybranch_or_tag BASE_IMAGE_TAG_SUFFIX=latest docker buildx bake gpu --no-cache
```

### Multi-Platform Builds

Deepstack images support multiple architectures. But depending on your operating system and Docker
environment, you might not be able to build all of them locally.

You may encounter the following error when trying to build the image:

```
multiple platforms feature is currently not supported for docker driver. Please switch to a different driver
(eg. “docker buildx create --use”)
```

To get around this, you need to override the `platform` option and limit local builds to the same architecture as
your computer's. For example, on an Apple M1 you can limit the builds to ARM only by invoking `bake` like this:

```sh
docker buildx bake base-cpu --set "*.platform=linux/arm64"
```

# License

View [license information](https://github.com/khulnasoft/deepstack/blob/main/LICENSE) for
the software contained in this image.

As with all Docker images, these likely also contain other software which may be under
other licenses (such as Bash, etc from the base distribution, along with any direct or
indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any
use of this image complies with any relevant licenses for all software contained within.
