FROM robotlocomotion/drake:1.35.0
LABEL Aditya Kamireddypalli "kamireddypalliaditya@gmail.com"

ENV WORKSPACE /root/workspace

# build essentials
RUN apt update && \
    apt install -y curl gcc build-essential cmake git && \
    apt install -y software-properties-common libtbb-dev && \
    apt install -y liblcm-dev libeigen3-dev python3.10-venv ffmpeg \
    clangd-12 wget lsb-release cmake libboost-all-dev gdb python3-dbg && \
    update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-12 100

# build osqp
RUN git clone --recurse-submodules https://github.com/osqp/osqp-python.git && \
    cd osqp-python && \
    pip3 install ninja && \
    python3 install .

# python management just in case
RUN git clone https://github.com/pyenv/pyenv.git /pyenv
ENV PYENV_ROOT /pyenv

RUN pip3 install jupyterlab && \
    pip3 install jupyterlab-vim && \
    pip3 install neopyter && \
    pip3 install nbdev && \
    # pip3 install open3d && \
    echo "export PATH="/opt/drake/bin${PATH:+:${PATH}}"" >> ~/.bashrc && \
    echo "export PYTHONPATH="/opt/drake/lib/python$(python3 -c 'import sys; \
    print("{0}.{1}".format(*sys.version_info))')/site-packages${PYTHONPATH:+:${PYTHONPATH}}"" >> ~/.bashrc


WORKDIR $WORKSPACE
