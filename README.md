
# QRData
Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data
<a href="https://arxiv.org/abs/2402.17644">[Paper]</a> <a href="https://xxxiaol.github.io/QRData/">[Project Website]</a>

## Benchmark
We provide the questions of quantitative reasoning with data (QRData) in `benchmark/QRData.json`. It contains 411 questions with the following keys.
 - `data_description`
 - `question`
 - `answer`
 - `data_files`: a list of names of data files
 - `meta_data`: a dict contains `reference`, `keywords`, `question_type`, and `multiple_choices` (the possible choices if `question_type` is 'multiple_choice').

Data files related to the questions are in `benchmark/data.zip`.

~~Questions of quantitative reasoning with text (QRText) are in `benchmark/QRText.json`.~~ 
Some numerical questions in QRText encounter measurement errors. We will release the corrected version in the future.

The script for evaluation is in 'benchmark/eval.py'. 

## Citation
 Please cite our paper if this repository inspires your work.
```
@inproceedings{liu-etal-2024-llms,
    title = "Are {LLM}s Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data",
    author = "Liu, Xiao  and
      Wu, Zirui  and
      Wu, Xueqing  and
      Lu, Pan  and
      Chang, Kai-Wei  and
      Feng, Yansong",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-acl.548",
    pages = "9215--9235",
}
```