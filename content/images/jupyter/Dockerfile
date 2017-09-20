FROM jupyter/datascience-notebook:82b978b3ceeb

MAINTAINER Rion Dooley <deardooley@gmail.com>

# Install agave python sdk and bash kernel
USER root
RUN cd /usr/local && \
    wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \
    mv /usr/local/jq-linux64 /usr/local/bin/jq && \
    chmod +x /usr/local/bin/jq ;\

    # add sshpass for importing password without displaying in console
    apt-get update ;\
    apt-get -y install sshpass ;\
    apt-get clean

USER jovyan
RUN /bin/bash -c "source activate python2" && \
    pip2 install -e "git+https://github.com/TACC/agavepy.git#egg=agavepy" && \

    pip2 install bash_kernel && \
    /bin/bash -c "source activate python2 && python -m bash_kernel.install"

# install jypter widgets for html form generation
RUN pip2 install ipywidgets && \
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

# Install agave bash cli
RUN  git clone https://github.com/agaveplatform/agave-cli.git src/cli
ENV PATH $PATH:/usr/local/jq/bin:$HOME/src/cli/bin
ENV AGAVE_JSON_PARSER jq
ENV AGAVE_CLI_COMPLETION_SHOW_FILES no
ENV AGAVE_CLI_COMPLETION_SHOW_FILE_PATHS no
ENV AGAVE_CLI_COMPLETION_CACHE_LIFETIME 0
RUN tenants-init -t agave.prod -v

ADD examples examples
COPY start.sh /usr/local/bin
USER jovyan
RUN mkdir .jupyter
COPY jupyter_notebook_config.py .jupyter/
RUN chmod 700 .jupyter

ARG BUILD_DATE
ARG VERSION

LABEL org.agaveplatform.devops.architecture="x86_64"                                \
      org.agaveplatform.devops.build-date="$BUILD_DATE"                             \
      org.agaveplatform.devops.license="BSD 3-clause"                               \
      org.agaveplatform.devops.name="agaveplatform/jupyter-datascience-notebook"    \
      org.agaveplatform.devops.summary="Jupyter datascience notebook server with Agave Python 2 SDK and CLI " \
      org.agaveplatform.devops.version="$VERSION"                                   \
      org.agaveplatform.devops.vcs-type="git"                                       \
      org.agaveplatform.devops.vcs-url="https://github.com/agaveplatform/jupyter-datascience-notebook" \
      org.agaveplatform.devops.jupyter.version="5.0.x"                              \
      org.agaveplatform.devops.environment="training"                               \
      org.agaveplatform.training="jupyter"

ENV VM_MACHINE sandbox
ENV VM_IPADDRESS 204.90.47.30
ENV USE_TUNNEL false
RUN mkdir -p /home/jovyan/.ssh
RUN chmod 700 .ssh
COPY keys/tutorial .ssh/id_rsa
COPY keys/tutorial.pub .ssh/id_rsa.pub
USER root
RUN find /home/jovyan | xargs chown jovyan