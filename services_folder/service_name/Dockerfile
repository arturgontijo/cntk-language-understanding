FROM ubuntu:18.04

ENV SINGNET_REPOS=/opt/singnet
ENV GH_REPO_NAME=nlp-services
ENV SERVICE_FOLDER=${SINGNET_REPOS}/${GH_REPO_NAME}/cntk-language-understanding
ENV SERVICE_NAME=cntk-language-understanding
ENV SNETD_PORT=7075
ENV SNETD_CONFIG=snetd.config.json

RUN mkdir -p ${SINGNET_REPOS}

RUN apt-get update && \
    apt-get install -y \
    git \
    wget \
    nano \
    libudev-dev \
    libusb-1.0-0-dev

RUN apt-get install -y python3 python3-pip
RUN apt-get install -y nodejs npm

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/singnet/snet-cli && \
    cd snet-cli && \
    ./scripts/blockchain install && \
    pip3.6 install -e .

RUN cd ${SINGNET_REPOS} && \
    mkdir snet-daemon && \
    cd snet-daemon && \
    wget https://github.com/singnet/snet-daemon/releases/download/v0.1.3/snetd-0.1.3.tar.gz && \
    tar -xvf snetd-0.1.3.tar.gz && \
    mv linux-amd64/snetd /usr/bin/snetd

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/singnet/nlp-services.git

RUN cd ${SERVICE_FOLDER}/${SERVICE_NAME} && \
    sh -c "echo '{ \"DAEMON_END_POINT\": \"http://54.203.198.53:${SNETD_PORT}\", \
                   \"ETHEREUM_JSON_RPC_ENDPOINT\": \"https://kovan.infura.io\", \
                   \"IPFS_END_POINT\": \"http://ipfs.singularitynet.io:80\", \
                   \"REGISTRY_ADDRESS_KEY\": \"0x2e4b2f2b72402b9b2d6a7851e37c856c329afe38\", \
                   \"PASSTHROUGH_ENABLED\": true, \
                   \"PASSTHROUGH_ENDPOINT\": \"http://localhost:7003\", \
                   \"ORGANIZATION_NAME\": \"snet\", \
                   \"SERVICE_NAME\": \"${SERVICE_NAME}\", \
                   \"LOG\": { \
                   \"LEVEL\": \"debug\", \
                   \"OUTPUT\": { \
                       \"TYPE\": \"stdout\" \
                       } \
                   } \
                }'" > ${SNETD_CONFIG}

RUN cd ${SERVICE_FOLDER}/${SERVICE_NAME} && \
    pip3 install -r requirements.txt && \
    sh buildproto.sh

WORKDIR ${SERVICE_FOLDER}/${SERVICE_NAME}