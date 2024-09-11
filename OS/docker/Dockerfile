FROM voidlinux/voidlinux:latest
RUN xbps-install -Suy && \
    xbps-install -y base-devel \
                   git \
                   wget \
                   vim \
                   bison \
                   gawk \
                   texinfo \
                   gmp-devel \
                   mpfr-devel \
                   libmpc-devel \
                   perl \
                   python3 \
                   ncurses-devel \
                   bash \
                   file \
                   patch \
                   coreutils \
                   make \
                   tar \
                   gcc \
                   grep \
                   findutils \
                   sed \
                   xz \
                   flex \
                   m4 \
                   diffutils \
                   util-linux \
                   man-db \
                   bzip2

RUN useradd -m -s /bin/bash lfs && \
    echo "lfs ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER lfs

WORKDIR /home/lfs

COPY ../sources /home/lfs/sources
COPY ../tools /home/lfs/tools
COPY ../scripts /home/lfs/scripts
COPY ../configs /home/lfs/configs

RUN wget https://www.linuxfromscratch.org/lfs/downloads/stable/wget-list -O /home/lfs/wget-list && \
    wget https://www.linuxfromscratch.org/lfs/downloads/stable/md5sums -O /home/lfs/md5sums

RUN wget --input-file=/home/lfs/wget-list --continue --directory-prefix=/home/lfs/sources

RUN cd /home/lfs/sources && \
    md5sum -c /home/lfs/md5sums

USER root
WORKDIR /home/lfs
