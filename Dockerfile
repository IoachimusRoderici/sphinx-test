FROM sphinxdoc/sphinx
WORKDIR /docs

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies:
RUN --mount=source=pip_requirements.txt,target=pip_requirements.txt \
    pip install -r pip_requirements.txt
