FROM continuumio/miniconda3:4.8.2

# set up conda environment
RUN mkdir /opt/conda/specs
COPY environment.yml /opt/conda/specs
RUN conda config --add channels conda-forge/label/dev && \
  conda config --add channels conda-forge && \
  conda update -n base conda && \
  conda env update -f /opt/conda/specs/environment.yml && \
  conda clean --all -f

# run app
COPY . /changing-times
CMD python /changing-times/app.py
