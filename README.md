# QRData
Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data
<!-- [<a href="https://arxiv.org/abs/"> Paper </a>] --><a href="https://xxxiaol.github.io/QRData/">[Project Website]</a>

## Benchmark
We provide the questions of quantitative reasoning with data (QRData) in `benchmark/QRData.json`. It contains 411 questions with the following keys.
 - `data_description`
 - `question`
 - `answer`
 - `data_files`: a list of names of data files
 - `meta_data`: a dict contains `reference`, `keywords`, `question_type`, and `multiple_choices` (the possible choices if `question_type` is 'multiple_choice').

Data files related to the questions are in `benchmark/data.zip`.

Questions of quantitative reasoning with text (QRText) are in `benchmark/QRText.json`. It contains 290 questions with the following keys.
 - `data_description`
 - `question`
 - `answer`
 - `meta_data`: a dict contains `reference`, `keywords`, `question_type`, and `multiple_choices` (the possible choices if `question_type` is 'multiple_choice').

The script for evaluation is in 'benchmark/eval.py'. 

## Citation
 Please cite our paper if this repository inspires your work.
```
TBD
```