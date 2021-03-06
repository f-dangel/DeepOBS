# DeepOBS - A Deep Learning Optimizer Benchmark Suite

![DeepOBS](docs/deepobs_banner.png "DeepOBS")

[![License: MIT](https://img.shields.io/github/license/fsschneider/deepobs?style=flat-square)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/deepobs?style=flat-square)
[![PyPI version](https://img.shields.io/pypi/v/deepobs.svg?style=flat-square)](https://pypi.org/project/deepobs)
![PyPI - Downloads](https://img.shields.io/pypi/dm/deepobs?style=flat-square)
[![Documentation Status](https://readthedocs.org/projects/deepobs/badge/?version=v1.2.0-beta0_a&style=flat-square)](https://deepobs.readthedocs.io/en/v1.2.0-beta0_a/?badge=v1.2.0-beta0_a)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
<!---![Codacy branch grade](https://img.shields.io/codacy/grade/0b6cb61af02745af8ed9126c7d0779e6/develop?logo=codacy&style=flat-square). Add in later.-->

> :warning: **This branch contains the beta of version 1.2.0**
>
> It contains the latest changes planed for the release of DeepOBS 1.2.0, including support for **PyTorch**. Not all features are implemented and most notably we currently don't provide baselines for this version. We continuously make changes to this version, so things can break if you update. If you want a more stable preview, checkout our pre-releases.

**DeepOBS** is a benchmarking suite that drastically simplifies, automates and
improves the evaluation of deep learning optimizers.

It can evaluate the performance of new optimizers on a variety of
**real-world test problems** and automatically compare them with
**realistic baselines**.

DeepOBS automates several steps when benchmarking deep learning optimizers:

- Downloading and preparing data sets.
- Setting up test problems consisting of contemporary data sets and realistic deep learning architectures.
- Running the optimizers on multiple test problems and logging relevant metrics.
- Reporting and visualization the results of the optimizer benchmark.

![DeepOBS Output](docs/deepobs.jpg "DeepOBS_output")

The code for the current implementation working with **TensorFlow** can be found
on [Github](https://github.com/fsschneider/DeepOBS).
A PyTorch version is currently developed (see News section below).

The documentation of the beta version is available on [readthedocs](https://deepobs.readthedocs.io/en/v1.2.0-beta0/).

The [paper describing DeepOBS](https://openreview.net/forum?id=rJg6ssC5Y7) has been accepted for ICLR 2019.

**If you find any bugs in DeepOBS, or find it hard to use, please let us know.
We are always interested in feedback and ways to improve DeepOBS.**

## News

We are currently working on a new and improved version of DeepOBS, version 1.2.0.
It will support **PyTorch** in addition to TensorFlow, has an easier interface, and
many bugs ironed out. You can find the latest version of it in [this branch](https://github.com/fsschneider/DeepOBS/tree/v1.2.0-beta0).

A pre-release, version 1.2.0-beta0, will be available shortly and a full release is expected in a few weeks.

Many thanks to [Aaron Bahde](https://github.com/abahde) for spearheading the developement of DeepOBS 1.2.0.

## Installation

    pip install deepobs

We tested the package with Python 3.6, TensorFlow version 1.12, Torch version 1.1.0 and Torchvision version 0.3.0.
Other versions of Python and TensorFlow (>= 1.4.0) might work, and we plan to expand compatibility in the future.

If you want to create a local and modifiable version of DeepOBS, you can do this directly from this repo via

    pip install -e git+https://github.com/fsschneider/DeepOBS.git#egg=DeepOBS

for the latest stable version, or

    pip install -e git+https://github.com/fsschneider/DeepOBS.git@v1.2.0-beta0#egg=DeepOBS

to get the preview of DeepOBS 1.2.0.

Further tutorials and a suggested protocol for benchmarking deep learning
optimizers can be found in the [documentation](https://deepobs.readthedocs.io/).
