FROM jupyter/datascience-notebook:82b978b3ceeb

MAINTAINER Rion Dooley <deardooley@gmail.com>

ARG BUILD_DATE
ARG SINGULARITY_VERSION
ARG VERSION

#LABEL architecture="x86_64"                                \
#      build-date="$BUILD_DATE"                             \
#      license="BSD 3-clause"                               \
#      name="agaveplatform/jupyter-datascience-notebook" \
#      summary="Jupyter datascience notebook server with Agave Python 2 SDK and CLI " \
#      version="$VERSION"                                   \
#      vcs-type="git"                                       \
#      vcs-url="https://github.com/agaveplatform/jupyter-datascience-notebook" \
#      singularity.version="$SINGULARITY_VERSION" \
#      jupyter.version="5.0.x" \



# Install agave python sdk and bash kernel
USER root
RUN cd /usr/local && \
    wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \
    mv /usr/local/jq-linux64 /usr/local/bin/jq && \
    chmod +x /usr/local/bin/jq

RUN apt-get update ;\
    apt-get -y install sshpass ;\
    apt-get clean
USER jovyan
RUN /bin/bash -c "source activate python2" && \
    pip2 install -e "git+https://github.com/TACC/agavepy.git#egg=agavepy" && \
    pip2 install bash_kernel && \
    /bin/bash -c "source activate python2 && python -m bash_kernel.install"

# Install agave bash cli
#RUN  git clone https://github.com/agaveplatform/agave-cli.git src/cli
#ENV PATH=$PATH:/usr/local/jq/bin:$HOME/src/cli/bin
#ENV AGAVE_JSON_PARSER=jq
#ENV AGAVE_CLI_COMPLETION_SHOW_FILES=no
#ENV AGAVE_CLI_COMPLETION_SHOW_FILE_PATHS=no
#ENV AGAVE_CLI_COMPLETION_CACHE_LIFETIME=0
#RUN tenants-init -t agave.prod -v
ADD  examples examples
USER root
RUN chown jovyan examples
USER jovyan
