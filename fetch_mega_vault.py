import os
import requests
from pathlib import Path

# Base folder for your Colab vault
LOCAL_DIR = Path.home() / "my-colab-notebooks"
LOCAL_DIR.mkdir(exist_ok=True, parents=True)

README_FILE = LOCAL_DIR / "README.md"

# Combined categories with 5 sample notebooks each
SAMPLE_NOTEBOOKS = {
    # Existing categories
    "ML": [
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/03_classification.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/04_training_linear_models.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/05_support_vector_machines.ipynb"
    ],
    "DL": [
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/conv_lstm_seq2seq.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/autoencoder.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/cnn_transformer.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/gan.ipynb"
    ],
    "CV": [
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/cnn.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/data_augmentation.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/segmentation.ipynb",
        "https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/mnist.ipynb"
    ],
    "DS": [
        "https://colab.research.google.com/github/justmarkham/pandas-videos/blob/master/pandas.ipynb",
        "https://colab.research.google.com/github/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.00-Data-Loading-and-Storage.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-NumPy-Arrays.ipynb",
        "https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.02-DataFrame.ipynb"
    ],
    "RL": [
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/DP/DP.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Monte%20Carlo/MC-Blackjack.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Temporal-Difference/TD.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/QLearning/QLearning.ipynb",
        "https://colab.research.google.com/github/dennybritz/reinforcement-learning/blob/master/Sarsa/Sarsa.ipynb"
    ],

    # LLM/NLP-focused categories
    "LLM-Basics": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/transformers_intro.ipynb",
        "https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/transformer.ipynb",
        "https://colab.research.google.com/github/fastai/fastbook/blob/master/11_nlp.ipynb",
        "https://colab.research.google.com/github/fastai/fastbook/blob/master/12_attention.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/token_classification.ipynb"
    ],
    "GPT-Style": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_generation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/gpt2_generation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/gpt_fine_tuning.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/chatbot_gpt.ipynb",
        "https://colab.research.google.com/github/minimaxir/gpt-2-simple/blob/master/gpt_2_simple.ipynb"
    ],
    "BERT-Style": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/token_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/ner.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/sentence_similarity.ipynb"
    ],
    "Fine-Tuning": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/finetune_text_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/finetune_question_answering.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/finetune_translation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/finetune_summarization.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/finetune_text_generation.ipynb"
    ],
    "Prompt-Engineering": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/prompting.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/few_shot_prompting.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/chain_of_thought.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/prompt_tuning.ipynb",
        "https://colab.research.google.com/github/minimaxir/prompt_engineering_examples/blob/main/prompt_examples.ipynb"
    ],
    "RLHF": [
        "https://colab.research.google.com/github/CarperAI/trl/blob/main/examples/ppo_training.ipynb",
        "https://colab.research.google.com/github/CarperAI/trl/blob/main/examples/reward_model.ipynb",
        "https://colab.research.google.com/github/CarperAI/trl/blob/main/examples/ppo_text_generation.ipynb",
        "https://colab.research.google.com/github/CarperAI/trl/blob/main/examples/rlhf_summary.ipynb",
        "https://colab.research.google.com/github/CarperAI/trl/blob/main/examples/rlhf_chatbot.ipynb"
    ],
    "Tokenization": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/tokenization.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/tokenizer_training.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/subword_tokenizer.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/bytepair_encoding.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/sentencepiece_tokenizer.ipynb"
    ],
    "Evaluation": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/evaluate_text_classification.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/evaluate_translation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/evaluate_summarization.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/evaluate_generation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/perplexity_evaluation.ipynb"
   ],

    "Applications": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/chatbot.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/summarization.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/question_answering.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/code_generation.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/reasoning_tasks.ipynb"
    ],
    "Utilities": [
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/dataset_utils.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/preprocessing.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/visualization.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/helper_functions.ipynb",
        "https://colab.research.google.com/github/huggingface/notebooks/blob/main/tokenizer_utils.ipynb"
    ]
}

def download_notebooks_and_generate_readme(sample_dict):
    md_lines = ["# My Mega Colab Vault\n"]
    for category, urls in sample_dict.items():
        folder_dir = LOCAL_DIR / category
        folder_dir.mkdir(exist_ok=True)
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
            md_lines.append(f"- [{filename}]({url})")
        md_lines.append("</details>\n")
    # Write README.md
    with open(README_FILE, "w") as f:
        f.write("\n".join(md_lines))
    print(f"✅ README.md generated with all categories at {README_FILE}")

if __name__ == "__main__":
    download_notebooks_and_generate_readme(SAMPLE_NOTEBOOKS)
