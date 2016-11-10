FROM centos:7
MAINTAINER Ben Zaitlen "ben.zaitlen@continuum.io"

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_COLLATE=C
ENV LC_CTYPE=en_US.UTF-8

# INSTALL OS DEPS
#RUN yum -y update; yum clean all
#RUN yum -y install epel-release; yum clean all
RUN yum -y install curl bzip2

# INSTALL Miniconda
RUN curl -o /tmp/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh
RUN bash /tmp/miniconda.sh -f -b -p /opt/miniconda

# INSTALL Python Deps
RUN /opt/miniconda/bin/conda install conda-kapsel=0.3.6 -c conda-kapsel -q -y

COPY {{DIR_PATH}}/* /tmp/{{APP_NAME}}/
WORKDIR /tmp/{{APP_NAME}}

ENV PATH /opt/miniconda/bin:$PATH
RUN /opt/miniconda/bin/conda-kapsel prepare --mode=production_defaults

CMD /opt/miniconda/bin/conda-kapsel run default --kapsel-host='*' --kapsel-url-prefix=$URL_PREFIX
