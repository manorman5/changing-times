FROM continuumio/miniconda3:4.8.2

# Options for common setup script
ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="false"
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
COPY .devcontainer/library-scripts/*.sh /tmp/library-scripts/
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# set up conda environment
RUN mkdir /opt/conda/specs
COPY environment.yml /opt/conda/specs
RUN conda config --add channels conda-forge/label/dev && \
  conda config --add channels conda-forge && \
  conda update -n base conda && \
  conda env update -f /opt/conda/specs/environment.yml && \
  conda clean --all -f