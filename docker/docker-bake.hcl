variable "DEEPSTACK_VERSION" {
  default = "main"
}

variable "GITHUB_REF" {
  default = ""
}

variable "IMAGE_NAME" {
  default = "khulnasoft/deepstack"
}

variable "IMAGE_TAG_SUFFIX" {
  default = "local"
}

variable "BASE_IMAGE_TAG_SUFFIX" {
  default = "local"
}

variable "DEEPSTACK_EXTRAS" {
  default = ""
}

target "base" {
  dockerfile = "Dockerfile.base"
  tags = ["${IMAGE_NAME}:base-${IMAGE_TAG_SUFFIX}"]
  args = {
    build_image = "python:3.12-slim"
    base_image = "python:3.12-slim"
    deepstack_version = "${DEEPSTACK_VERSION}"
  }
  platforms = ["linux/amd64", "linux/arm64"]
}
