{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPAy3zmi+bQBzvgaIVxW1/t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AlfredoV3g4/Practica_1/blob/main/Untitled1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Practica_1"
      ],
      "metadata": {
        "id": "0qWpyqyUEpXJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "tEGn3V-GEt2o"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "celcius = np.array([-15, -5, 0, 5, 15], dtype=float)\n",
        "fahrenheit = np.array([5, 23, 32, 41, 59], dtype=float)"
      ],
      "metadata": {
        "id": "H5JLMNWRExNZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "capa = tf.keras.layers.Dense(units=1, input_shape=[1])\n",
        "modelo = tf.keras.Sequential([capa])"
      ],
      "metadata": {
        "id": "OguEsEP6Ezsr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.compile(\n",
        "    optimizer = tf.keras.optimizers.Adam(0.1),\n",
        "    loss='mean_squared_error'\n",
        ")"
      ],
      "metadata": {
        "id": "twB1BByPE1jq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"comenzando entrenamiento\")\n",
        "historial=modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)\n",
        "print(\"modelo entrenado!!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BXTtkmVOE3Y5",
        "outputId": "b69205e8-6b77-4f58-80a4-f85a883ef4d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "comenzando entrenamiento\n",
            "modelo entrenado!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.xlabel(\"# Epoca\")\n",
        "plt.ylabel(\"Magnitud de perdida\")\n",
        "plt.plot(historial.history[\"loss\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "yOmMbYDwE8bK",
        "outputId": "d84f5acb-bb7b-47fc-f05c-c395138d2554"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7c4fb1f3f4f0>]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"realizar una prediccion!!!\")\n",
        "resultado = modelo.predict([100.0])\n",
        "print (\"el resultado es\" + str(resultado) + \"galones!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uHvDd-VOE_vh",
        "outputId": "ae7c5f93-bf95-4cdb-cd7a-27af675df9be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "realizar una prediccion!!!\n",
            "1/1 [==============================] - 0s 88ms/step\n",
            "el resultado es[[211.9783]]galones!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.save('celsuis_a_fahrenheit.h5')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "egGNqu6oFm2Q",
        "outputId": "1f6fd2ec-9ba4-4544-df0a-68410a3f051e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3079: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.\n",
            "  saving_api.save_model(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "liKsfG-lF-Cp",
        "outputId": "6b514b98-abfc-481b-a0f2-2cc691b4dc53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "celsuis_a_fahrenheit.h5  sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflowjs"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "XLhSm_tqGAfk",
        "outputId": "33524b2f-045f-42f3-b746-0231c47c64d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting tensorflowjs\n",
            "  Downloading tensorflowjs-4.13.0-py3-none-any.whl (89 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/89.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m89.2/89.2 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: flax>=0.7.2 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.7.5)\n",
            "Requirement already satisfied: importlib_resources>=5.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (6.1.1)\n",
            "Requirement already satisfied: jax>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20)\n",
            "Requirement already satisfied: jaxlib>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20+cuda11.cudnn86)\n",
            "Requirement already satisfied: tensorflow<3,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (2.14.0)\n",
            "Collecting tensorflow-decision-forests>=1.5.0 (from tensorflowjs)\n",
            "  Downloading tensorflow_decision_forests-1.8.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (15.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.3/15.3 MB\u001b[0m \u001b[31m63.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: six<2,>=1.16.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (1.16.0)\n",
            "Requirement already satisfied: tensorflow-hub>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.15.0)\n",
            "Requirement already satisfied: packaging~=23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (23.2)\n",
            "Requirement already satisfied: numpy>=1.22 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.23.5)\n",
            "Requirement already satisfied: msgpack in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.0.7)\n",
            "Requirement already satisfied: optax in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: orbax-checkpoint in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.4.2)\n",
            "Requirement already satisfied: tensorstore in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.45)\n",
            "Requirement already satisfied: rich>=11.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (13.7.0)\n",
            "Requirement already satisfied: typing-extensions>=4.2 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (4.5.0)\n",
            "Requirement already satisfied: PyYAML>=5.4.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (6.0.1)\n",
            "Requirement already satisfied: ml-dtypes>=0.2.0 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: opt-einsum in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (3.3.0)\n",
            "Requirement already satisfied: scipy>=1.9 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (1.11.3)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=23.5.26 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (23.5.26)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.5.4)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.9.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (16.0.6)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.20.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (67.7.2)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.3.0)\n",
            "Requirement already satisfied: wrapt<1.15,>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.14.1)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.34.0)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.59.2)\n",
            "Requirement already satisfied: tensorboard<2.15,>=2.14 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.1)\n",
            "Requirement already satisfied: tensorflow-estimator<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: keras<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (1.5.3)\n",
            "Collecting tensorflow<3,>=2.13.0 (from tensorflowjs)\n",
            "  Downloading tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.2 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m475.2/475.2 MB\u001b[0m \u001b[31m3.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: wheel in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (0.41.3)\n",
            "Collecting wurlitzer (from tensorflow-decision-forests>=1.5.0->tensorflowjs)\n",
            "  Downloading wurlitzer-3.0.3-py3-none-any.whl (7.3 kB)\n",
            "Collecting tensorboard<2.16,>=2.15 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorboard-2.15.1-py3-none-any.whl (5.5 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.5/5.5 MB\u001b[0m \u001b[31m101.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting tensorflow-estimator<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl (441 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m442.0/442.0 kB\u001b[0m \u001b[31m43.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting keras<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading keras-2.15.0-py3-none-any.whl (1.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m91.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (2.16.1)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.17.3)\n",
            "Requirement already satisfied: google-auth-oauthlib<2,>=0.5 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.0.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.5.1)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.31.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.0.1)\n",
            "Requirement already satisfied: chex>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from optax->flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: etils[epath,epy] in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.2)\n",
            "Requirement already satisfied: nest_asyncio in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.8)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2023.3.post1)\n",
            "Requirement already satisfied: dm-tree>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.1.8)\n",
            "Requirement already satisfied: toolz>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.12.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (4.9)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.3.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=11.1->flax>=0.7.2->tensorflowjs) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2023.7.22)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/dist-packages (from werkzeug>=1.0.1->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.1.3)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (2023.6.0)\n",
            "Requirement already satisfied: zipp in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (3.17.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.5.0)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.2.2)\n",
            "Installing collected packages: wurlitzer, tensorflow-estimator, keras, tensorboard, tensorflow, tensorflow-decision-forests, tensorflowjs\n",
            "  Attempting uninstall: tensorflow-estimator\n",
            "    Found existing installation: tensorflow-estimator 2.14.0\n",
            "    Uninstalling tensorflow-estimator-2.14.0:\n",
            "      Successfully uninstalled tensorflow-estimator-2.14.0\n",
            "  Attempting uninstall: keras\n",
            "    Found existing installation: keras 2.14.0\n",
            "    Uninstalling keras-2.14.0:\n",
            "      Successfully uninstalled keras-2.14.0\n",
            "  Attempting uninstall: tensorboard\n",
            "    Found existing installation: tensorboard 2.14.1\n",
            "    Uninstalling tensorboard-2.14.1:\n",
            "      Successfully uninstalled tensorboard-2.14.1\n",
            "  Attempting uninstall: tensorflow\n",
            "    Found existing installation: tensorflow 2.14.0\n",
            "    Uninstalling tensorflow-2.14.0:\n",
            "      Successfully uninstalled tensorflow-2.14.0\n",
            "Successfully installed keras-2.15.0 tensorboard-2.15.1 tensorflow-2.15.0 tensorflow-decision-forests-1.8.1 tensorflow-estimator-2.15.0 tensorflowjs-4.13.0 wurlitzer-3.0.3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "keras",
                  "tensorboard",
                  "tensorflow"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!mkdir temperatura"
      ],
      "metadata": {
        "id": "DyxP_EyJGd4c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!tensorflowjs_converter --input_format keras celsuis_a_fahrenheit.h5 temperatura"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Kiyvdl-Gi9W",
        "outputId": "531a2ece-7221-4bd5-e7b5-c5de4ed69a94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2023-11-23 21:34:13.216015: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "2023-11-23 21:34:13.216111: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "2023-11-23 21:34:13.217653: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "2023-11-23 21:34:14.506671: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls temperatura"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "36wN9MwgG9s5",
        "outputId": "43c48a66-d777-43ce-bf05-920cea1ed565"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "group1-shard1of1.bin  model.json\n"
          ]
        }
      ]
    }
  ]
}