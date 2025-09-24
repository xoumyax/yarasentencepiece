import sentencepiece as spm

# --- Train the SentencePiece model ---
# The input is the text file we created in the previous step.
# model_prefix is the base name for the output model and vocab files.
# vocab_size is a hyperparameter you choose. 500 is just an example.
spm.SentencePieceTrainer.train(
    f'--input={"./synthetic250k_placeholder.txt"} --model_prefix=yaratexttokenizer_bart --vocab_size=52000 --model_type=unigram --character_coverage=1.0 --pad_id=0 --unk_id=1 --bos_id=2 --eos_id=3 --train_extremely_large_corpus=true'
)

print("Tokenizer training complete!")
print("Created files: yaratexttokenizer_bart_uni.model and yaratexttokenizer_bart_uni.vocab")