#!/bin/bash
#SBATCH --job-name=uni-sentencepiece
#SBATCH --output=logs/uni_sentencepiece_train_%j.out
#SBATCH --error=logs/uni_sentencepiece_train_%j.err
#SBATCH --nodes=1                 # Number of nodes (adjust as needed)
#SBATCH --ntasks-per-node=1         # Number of tasks per node
#SBATCH --cpus-per-task=50         # CPUs per task
#SBATCH --time=48:00:00             # Job time limit
#SBATCH --mem=250G                  # Memory per node

# Activate your Conda environment
source /opt/local/conda/etc/profile.d/conda.sh
conda activate /home/soumya/.conda/envs/YaraLLM

# Run your Python script
srun python -u /home/soumya/yarasentencepiece/YaraTextTok/tokenization.py