# Python for Machine Learning — Course Notebooks

**University of Idaho — CS 4771/5771, Fall 2026**

Companion notebooks for the course. Open any of them in Google Colab (the free
tier is enough), or clone and run locally with the course environment.

Course site: <https://boyu-zhang-uoi.github.io/pml-f2026/>

---

## How these relate to the course

**The assigned reading is the PDF in Canvas, one per session.** These notebooks
are not a substitute for it and not a summary of it — they are the parts worth
*running*, and they open in Colab when a laptop is fighting its install.

The notebooks marked **HW** are companions to an assignment. Note what they
deliberately are not: none of them implements a function the homework asks you
to write. They give you the checks — a numeric gradient, an autograd oracle, a
loss-history reading — that let you find your own bugs.

Every notebook here **ships with its outputs**, so you can read one without
running it, and so a broken cell is caught before class rather than during it.

| Notebook | Topic | Sessions | Homework | Open |
|---|---|---|---|---|
| [`00_environment_smoke_test.ipynb`](00-setup/00_environment_smoke_test.ipynb) | Does your machine work? | S1 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/00-setup/00_environment_smoke_test.ipynb) |
| [`01_session01_taste_demo.ipynb`](00-setup/01_session01_taste_demo.ipynb) | A whole ML system, end to end — the Session 1 in-class demo | S1 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/00-setup/01_session01_taste_demo.ipynb) |
| [`01_python_basics_tutorial.ipynb`](01-python-basics/01_python_basics_tutorial.ipynb) | Python refresher | before S2 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/01-python-basics/01_python_basics_tutorial.ipynb) |
| [`02_python_for_ml_idioms.ipynb`](01-python-basics/02_python_for_ml_idioms.ipynb) | Python idioms an ML course assumes | S2 | HW 1 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/01-python-basics/02_python_for_ml_idioms.ipynb) |
| [`01_numpy_pandas_tutorial.ipynb`](02-data-science-stack/01_numpy_pandas_tutorial.ipynb) | NumPy & pandas | S3–S4 | **HW 1** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/01_numpy_pandas_tutorial.ipynb) |
| [`02_visualization_tutorial.ipynb`](02-data-science-stack/02_visualization_tutorial.ipynb) | Visualization mechanics | S6 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/02_visualization_tutorial.ipynb) |
| [`03_pandas_wrangling_and_missing_data.ipynb`](02-data-science-stack/03_pandas_wrangling_and_missing_data.ipynb) | One dirty table, all the way through | S5 | HW 1 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/03_pandas_wrangling_and_missing_data.ipynb) |
| [`04_eda_methodology.ipynb`](02-data-science-stack/04_eda_methodology.ipynb) | One table, four EDA phases | S6 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/04_eda_methodology.ipynb) |
| [`05_sklearn_pipeline_and_leakage.ipynb`](02-data-science-stack/05_sklearn_pipeline_and_leakage.ipynb) | The leaky run and the honest run | S7 | HW 1, HW 2 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/05_sklearn_pipeline_and_leakage.ipynb) |
| [`01_debugging_gradient_descent.ipynb`](03-classical-ml/01_debugging_gradient_descent.ipynb) | Debugging your own gradient descent | S8, S10 | **HW 2** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/01_debugging_gradient_descent.ipynb) |
| [`02_regularization_bias_variance.ipynb`](03-classical-ml/02_regularization_bias_variance.ipynb) | Capacity, curves, and two penalties | S9 | HW 2 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/02_regularization_bias_variance.ipynb) |
| [`03_logistic_multiclass.ipynb`](03-classical-ml/03_logistic_multiclass.ipynb) | From one probability to several | S10 | HW 2 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/03_logistic_multiclass.ipynb) |
| [`04_model_evaluation.ipynb`](03-classical-ml/04_model_evaluation.ipynb) | What the score is not telling you | S11 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/04_model_evaluation.ipynb) |
| [`05_knn_svm_tuning.ipynb`](03-classical-ml/05_knn_svm_tuning.ipynb) | Distance, margins, and a search that terminates | S12 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/05_knn_svm_tuning.ipynb) |
| [`06_trees_random_forests.ipynb`](03-classical-ml/06_trees_random_forests.ipynb) | Splits, variance, and an importance that lies | S13 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/06_trees_random_forests.ipynb) |
| [`07_boosting_synthesis.ipynb`](03-classical-ml/07_boosting_synthesis.ipynb) | Four families, one split | S14 | Quiz 2, capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/07_boosting_synthesis.ipynb) |
| [`01_reading_unsupervised_results.ipynb`](04-unsupervised/01_reading_unsupervised_results.ipynb) | Reading an unsupervised result honestly | S15, S17, S18 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/04-unsupervised/01_reading_unsupervised_results.ipynb) |
| [`02_umap_and_neighbor_embeddings.ipynb`](04-unsupervised/02_umap_and_neighbor_embeddings.ipynb) | Three maps of the same data | S16 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/04-unsupervised/02_umap_and_neighbor_embeddings.ipynb) |
| [`03_gaussian_mixtures_and_bic.ipynb`](04-unsupervised/03_gaussian_mixtures_and_bic.ipynb) | Two definitions of a cluster | S18 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/04-unsupervised/03_gaussian_mixtures_and_bic.ipynb) |
| [`00_autograd_oracle.ipynb`](05-deep-learning-pytorch/00_autograd_oracle.ipynb) | Checking a hand-built autograd | S19–S20 | **HW 3** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/00_autograd_oracle.ipynb) |
| [`01_pytorch_mlp.ipynb`](05-deep-learning-pytorch/01_pytorch_mlp.ipynb) | MLPs in PyTorch | S20–S21 | HW 3 Part B | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/01_pytorch_mlp.ipynb) |
| [`02_pytorch_cnn.ipynb`](05-deep-learning-pytorch/02_pytorch_cnn.ipynb) | CNNs and transfer learning | S22–S23 | **HW 4** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/02_pytorch_cnn.ipynb) |
| [`03_pytorch_rnn.ipynb`](05-deep-learning-pytorch/03_pytorch_rnn.ipynb) | Sequence models | S24 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/03_pytorch_rnn.ipynb) |
| [`04_training_in_practice.ipynb`](05-deep-learning-pytorch/04_training_in_practice.ipynb) | Optimizers, regularizers, and a run table | S21 | HW 3 Part B | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/04_training_in_practice.ipynb) |
| [`05_lightning_same_model.ipynb`](05-deep-learning-pytorch/05_lightning_same_model.ipynb) | The same model, written twice | S23 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/05_lightning_same_model.ipynb) |
| [`01_attention_from_scratch.ipynb`](06-transformers/01_attention_from_scratch.ipynb) | Attention, checked against PyTorch | S25 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/06-transformers/01_attention_from_scratch.ipynb) |
| [`02_huggingface_finetuning.ipynb`](06-transformers/02_huggingface_finetuning.ipynb) | Fine-tuning something somebody else pretrained | S26 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/06-transformers/02_huggingface_finetuning.ipynb) |
| [`01_vae_and_diffusion.ipynb`](07-generative/01_vae_and_diffusion.ipynb) | Compression, a latent with a shape, and learned denoising | S27 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/07-generative/01_vae_and_diffusion.ipynb) |
| [`01_service_and_monitoring.ipynb`](07-mlops/01_service_and_monitoring.ipynb) | A model somebody else can call | S29 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/07-mlops/01_service_and_monitoring.ipynb) |
| [`01_fairness_and_explainability.ipynb`](07-responsible-ml/01_fairness_and_explainability.ipynb) | Auditing a model you did not intend to be unfair | S30 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/07-responsible-ml/01_fairness_and_explainability.ipynb) |
| [`llms_in_practice.ipynb`](08-llms/llms_in_practice.ipynb) | LLMs in practice | S28 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/08-llms/llms_in_practice.ipynb) |

### What each one covers

**Getting started**

- **Does your machine work?** — Not a lesson: a receipt. Versions, one
  split/fit/predict/score, a figure, a CSV. Run it before Session 2.
- **A whole ML system, end to end** — The Session 1 in-class demo: ten lines
  that load 569 tumours, hold a quarter back, fit, and score honestly against
  the do-nothing baseline. Slides 20–22 carry the same three cells.
- **Python refresher** — Types, loops, functions, a first class. **Below the
  level of Session 2** — this is the catch-up if Python itself is new.
- **Python idioms an ML course assumes** — Aliasing, the mutable default,
  comprehensions and generators, an estimator-shaped class, EAFP, `pathlib`.

**The data stack**

- **NumPy & pandas** — Arrays, indexing, DataFrames, group-by, joins.
- **One dirty table, all the way through** — A missingness audit that shows why
  group-mean imputation cannot move a group mean, `agg` versus `transform`, a
  merge that fails under `validate=`, one pytest, and the same query in Polars
  and DuckDB.
- **Visualization mechanics** — Matplotlib and Seaborn: Figure, Axes, subplots.
- **One table, four EDA phases** — The order to look at a table in, plus
  Simpson's paradox halving a slope and two wrong-versus-right figure pairs.
- **The leaky run and the honest run** — Three leaks in order of severity: an
  ordering leak worth *nothing* on this data (measured over forty subsamples),
  a feature-selection leak that reports 0.71 accuracy on random labels, and a
  leaky column no pipeline can save you from.

**Classical machine learning**

- **Debugging your own gradient descent** — The gradient check, reading a loss
  history, where a naive sigmoid overflows. **Implements none of the HW 2
  functions.**
- **Capacity, curves, and two penalties** — Degree sweeps, learning curves that
  answer "more data or a better model?", ridge and lasso coefficient paths, and
  what happens to a penalty when you forget to scale.
- **From one probability to several** — Both closed forms of the sigmoid
  overflowing, multinomial versus one-vs-rest disagreeing on real rows, and the
  threshold as a policy.
- **What the score is not telling you** — Six metrics disagreeing about the same
  model, a reliability diagram, and `GroupKFold` removing twenty points of AUC
  that a random split had invented.
- **Distance, margins, and a search that terminates** — Scaling as the
  experiment, `C` and `gamma`, and a grid search that took 84x its own estimate
  because one corner of the grid was pathological.
- **Splits, variance, and an importance that lies** — One split by hand, pruning
  with `ccp_alpha`, OOB against held-out, and a pure-noise column taking thirty
  percent of the impurity importance until permutation importance corrects it.
- **Four families, one split** — Logistic regression, random forest,
  HistGradientBoosting and XGBoost under one split, one metric, one budget, with
  wall-clock times and early stopping.

**Unsupervised**

- **Reading an unsupervised result honestly** — Choosing PCA components, why
  scaling first is not optional, telling three real clusters from none, DBSCAN's
  `eps`, and running t-SNE twice.
- **Three maps of the same data** — PCA, t-SNE and UMAP with trustworthiness
  numbers, UMAP placing held-out points, and the same data under four seeds.
- **Two definitions of a cluster** — Soft responsibilities, covariance types,
  BIC across K, and where DBSCAN beats a mixture and where it does not.

**Deep learning**

- **Checking a hand-built autograd** — PyTorch as the oracle for your `Value`
  class. **Implements no part of HW 3.**
- **MLPs in PyTorch** — Tensors, `nn.Module`, the training loop end to end.
- **Optimizers, regularizers, and a run table** — Ablations with everything else
  pinned, five seeds showing a single-seed ranking was a coin flip, `eval()`
  mode costing accuracy when forgotten, and the run table itself.
- **CNNs and transfer learning** — Convolutions, pooling, and fine-tuning a
  pretrained backbone.
- **The same model, written twice** — Raw PyTorch and Lightning, same seed, same
  result, and the eight pieces of protocol Lightning removes.
- **Sequence models** — RNNs and LSTMs on a sequence task.

**Transformers, generative models, and practice**

- **Attention, checked against PyTorch** — Attention in NumPy with the
  assertions worth keeping, a causal mask, multi-head split/merge, and a
  measurement of what `/ sqrt(d_k)` is for.
- **Fine-tuning something somebody else pretrained** — A pinned checkpoint on
  CPU in eighty seconds, the same architecture from scratch scoring chance, and
  a TF-IDF baseline within a few points of both.
- **Compression, a latent with a shape, and learned denoising** — An
  autoencoder that cannot generate, a VAE that can, posterior collapse at high
  beta, and diffusion turning noise into a spiral on a laptop.
- **LLMs in practice** — Prompting, retrieval with and without a download, and
  LoRA. Needs `transformers`; the model downloads are marked.
- **A model somebody else can call** — A FastAPI service with a schema that
  rejects five kinds of malformed request, an artifact that matches the notebook
  bit for bit, tests, a non-root Dockerfile, and a PSI drift monitor.
- **Auditing a model you did not intend to be unfair** — Group-wise rates with
  intervals, the incompatibility of fairness criteria, a threshold fix that
  moves the harm, and SHAP and LIME read as statements about the model.

---

## Optional reference — TensorFlow / Keras

Deep learning in this course is taught in PyTorch. These Keras equivalents are
optional self-study; Keras 3 is multi-backend and will run on PyTorch.

| Notebook | Open |
|---|---|
| [`01_keras_mlp.ipynb`](optional-tensorflow/01_keras_mlp.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/optional-tensorflow/01_keras_mlp.ipynb) |
| [`02_keras_cnn.ipynb`](optional-tensorflow/02_keras_cnn.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/optional-tensorflow/02_keras_cnn.ipynb) |
| [`03_keras_rnn.ipynb`](optional-tensorflow/03_keras_rnn.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/optional-tensorflow/03_keras_rnn.ipynb) |

These three carry no saved outputs: they need TensorFlow, which the course
environment does not install. Run them in Colab.

---

## How these notebooks were prepared

Generative AI assistants were used in drafting these notebooks, the same as for
the rest of the course materials, and the same standard applies here that the
syllabus asks of you: **every cell was executed while writing it**, the saved
outputs are real runs, and where a demonstration did not show what the text
claimed, the demonstration was rebuilt rather than the claim softened.

Responsibility for the content rests with the instructor. If a notebook breaks,
or a result looks wrong, please report it.

## Running locally

```bash
git clone https://github.com/Boyu-Zhang-UOI/pml-f2026-notebooks.git
cd pml-f2026-notebooks
pip install -r https://raw.githubusercontent.com/Boyu-Zhang-UOI/pml-f2026/main/requirements-pytorch.txt
jupyter lab
```

The [environment setup guide](https://boyu-zhang-uoi.github.io/pml-f2026/docs/setup/)
has the full instructions, including which requirements file each part of the
course needs.
