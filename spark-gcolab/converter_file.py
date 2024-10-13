import jupytext
# read a notebook from a file
vpath1 ='/Users/edugonzo/Desktop/GitRepos_work/spark_simple/spark-gcolab/basic_gcp_colab_sp-2.ipynb'
vpath2 ='/Users/edugonzo/Downloads/basic_gcp_colab_sp_format.py'

nb = jupytext.read(vpath1)
jupytext.write(nb, vpath2, fmt="py:percent")
