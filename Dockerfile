FROM themattrix/tox
MAINTAINER Ryan Rigdon <mr.rigdon@gmail.com>

RUN pip install -U pip setuptools ipython ipdb wheel \
    -r requirements.txt -r requirements_test.txt -r requirements_static_analysis.txt \
    -r requirements_test_runner.txt
