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
| [`01_python_basics_tutorial.ipynb`](01-python-basics/01_python_basics_tutorial.ipynb) | Python refresher | before S2 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/01-python-basics/01_python_basics_tutorial.ipynb) |
| [`01_numpy_pandas_tutorial.ipynb`](02-data-science-stack/01_numpy_pandas_tutorial.ipynb) | NumPy & pandas | S3–S5 | **HW 1** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/01_numpy_pandas_tutorial.ipynb) |
| [`02_visualization_tutorial.ipynb`](02-data-science-stack/02_visualization_tutorial.ipynb) | Visualization & EDA | S6–S7 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/02-data-science-stack/02_visualization_tutorial.ipynb) |
| [`01_debugging_gradient_descent.ipynb`](03-classical-ml/01_debugging_gradient_descent.ipynb) | Debugging your own gradient descent | S8–S10 | **HW 2** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/03-classical-ml/01_debugging_gradient_descent.ipynb) |
| [`01_reading_unsupervised_results.ipynb`](04-unsupervised/01_reading_unsupervised_results.ipynb) | Reading an unsupervised result honestly | S15–S18 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/04-unsupervised/01_reading_unsupervised_results.ipynb) |
| [`00_autograd_oracle.ipynb`](05-deep-learning-pytorch/00_autograd_oracle.ipynb) | Checking a hand-built autograd | S19–S20 | **HW 3** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/00_autograd_oracle.ipynb) |
| [`01_pytorch_mlp.ipynb`](05-deep-learning-pytorch/01_pytorch_mlp.ipynb) | MLPs in PyTorch | S20–S21 | HW 3 Part B | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/01_pytorch_mlp.ipynb) |
| [`02_pytorch_cnn.ipynb`](05-deep-learning-pytorch/02_pytorch_cnn.ipynb) | CNNs and transfer learning | S22–S23 | **HW 4** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/02_pytorch_cnn.ipynb) |
| [`03_pytorch_rnn.ipynb`](05-deep-learning-pytorch/03_pytorch_rnn.ipynb) | Sequence models | S24 | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/05-deep-learning-pytorch/03_pytorch_rnn.ipynb) |
| [`llms_in_practice.ipynb`](08-llms/llms_in_practice.ipynb) | LLMs in practice | S28 | capstone | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Boyu-Zhang-UOI/pml-f2026-notebooks/blob/main/08-llms/llms_in_practice.ipynb) |

### What each one covers

- **Python refresher** — Types, loops, functions, a first class. **Below the level of Session 2** — this is the catch-up if Python itself is new.
- **NumPy & pandas** — Arrays, indexing, DataFrames, group-by, joins.
- **Visualization & EDA** — Matplotlib and Seaborn, and the order to look at a table in.
- **Debugging your own gradient descent** — The gradient check, reading a loss history, where a naive sigmoid overflows, and a leakage demo that manufactures 90% accuracy from pure noise. **Implements none of the HW 2 functions** — it gives you the tools to debug your own.
- **Reading an unsupervised result honestly** — Choosing PCA components, why scaling first is not optional, telling three real clusters from none, DBSCAN's `eps`, and running t-SNE twice.
- **Checking a hand-built autograd** — PyTorch as the oracle for your `Value` class: the eleven expressions worth testing, what a failing ratio means, and the four-line training step. **Implements no part of HW 3.**
- **MLPs in PyTorch** — Tensors, `nn.Module`, the training loop end to end.
- **CNNs and transfer learning** — Convolutions, pooling, and fine-tuning a pretrained backbone.
- **Sequence models** — RNNs and LSTMs on a sequence task.
- **LLMs in practice** — Prompting, retrieval, and LoRA. Needs `transformers`; run it in Colab.

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
