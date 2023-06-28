import sacrebleu

ref_file = r"C:\Users\Liyia\Desktop\唐老师信息技术\期末论文\material\reference.txt"
mt_file = r"C:\Users\Liyia\Desktop\唐老师信息技术\期末论文\material\Baidu.txt"

with open(ref_file, encoding='utf-8') as f:
    ref = f.readlines()

with open(mt_file, encoding='utf-8') as f:
    mt = f.readlines()

# Calculate BLEU score using SacreBLEU
score1 = sacrebleu.corpus_bleu(mt, [ref])
print("BLEU score:", score1.score)

score2 = sacrebleu.corpus_ter(mt, [ref])
print("TER score:", score2.score)
