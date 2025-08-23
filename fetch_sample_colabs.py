import os
import requests
from pathlib import Path

# Local folder
LOCAL_DIR = Path.home() / "my-colab-notebooks"
LOCAL_DIR.mkdir(exist_ok=True, parents=True)

README_FILE = LOCAL_DIR / "README.md"

# Extended verified sample notebooks
SAMPLE_NOTEBOOKS = {
    "ML": [
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/03_classification.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/04_training_linear_models.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/05_support_vector_machines.ipynb"
    ],
    "NLP": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/token_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_generation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/translation.ipynb"
    ],
    "CV": [
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/cnn.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/data_augmentation.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/segmentation.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/mnist.ipynb"
    ],
    "DL": [  # Deep Learning
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/conv_lstm_seq2seq.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/autoencoder.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/cnn_transformer.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/gan.ipynb"
    ],
    "DS": [  # Data Science
        "https://colab.research.google.com/github/justmarkham/pandas-videos/blob/master/pandas.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.00-Data-Loading-and-Storage.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-NumPy-Arrays.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.02-DataFrame.ipynb"
    ],
    "RL": [  # Reinforcement Learning
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/DP/DP.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Monte%20Carlo/MC-Blackjack.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Temporal-Difference/TD.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/QLearning/QLearning.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Sarsa/Sarsa.ipynb"
    ]
}

def download_notebooks_and_generate_readme(sample_dict):
    md_lines = ["# My Colab Notebooks\n"]
    for category, urls in sample_dict.items():
        folder_dir = LOCAL_DIR / category
        folder_dir.mkdir(exist_ok=True)
        # Collapsible section
        md_lines.append(f"<details>")
        md_lines.append(f"<summary>📂 {category}</summary>\n")
        for url in urls:
            filename = url.split("/")[-1]
            local_file = folder_dir / filename
            if not local_file.exists():
                # Convert Colab URL to raw GitHub URL
                raw_url = url.replace("https://colab.research.google.com/github/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
                print(f"Downloading {filename} into {folder_dir}")
                r = requests.get(raw_url)
                if r.status_code == 200:
                    with open(local_file, "wb") as f:
                        f.write(r.content)
                else:
                    print(f"Failed to download {filename} (status {r.status_code})")
            else:
                print(f"Skipping existing file: {filename}")
            # Add Markdown link
            md_lines.append(f"- [{filename}]({url})")
        md_lines.append("</details>\n")  # End collapsible
    # Write README.md
    with open(README_FILE, "w") as f:
        f.write("\n".join(md_lines))
    print(f"✅ Markdown README with collapsible categories generated at {README_FILE}")

if __name__ == "__main__":
    download_notebooks_and_generate_readme(SAMPLE_NOTEBOOKS)
