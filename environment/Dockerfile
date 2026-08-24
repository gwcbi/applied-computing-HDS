# Reference container for PUBH 6854 / 4201 (Applied/Practical Computing in HDS)
# Build:  docker build -t hds-computing -f environment/Dockerfile .
# Run:    docker run -it --rm -p 8888:8888 -v "$PWD":/workspace hds-computing

FROM condaforge/miniforge3:latest

WORKDIR /workspace

COPY environment/environment.yml /tmp/environment.yml
RUN mamba env create -f /tmp/environment.yml && \
    mamba clean -afy

# R (base + littler for scripting); students needing the full renv-managed
# package set should still run environment/renv-setup.md inside the container.
RUN mamba install -n hds-computing -y -c conda-forge r-base r-essentials && \
    mamba clean -afy

SHELL ["conda", "run", "-n", "hds-computing", "/bin/bash", "-c"]

EXPOSE 8888
CMD ["conda", "run", "--no-capture-output", "-n", "hds-computing", \
     "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# Open item: not yet built/tested (no Docker daemon available in this
# session). Validate `docker build` succeeds and the image size/build time
# are reasonable for students before Week 2.
