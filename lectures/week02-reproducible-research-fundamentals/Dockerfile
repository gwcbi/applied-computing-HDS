FROM condaforge/miniforge3
WORKDIR /workspace
COPY live-demo1.yml environment.yml
COPY analyze.py .
RUN mamba env create -f environment.yml
