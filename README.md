# doct5

连接分段的预测问题       

```text
!sh 1.sh
```

完整性检查：

输出结果应该是  8841823 2253863941 12517353325 predicted_queries_topk.txt-1004000

```text
!cd /data/students/nieyj/code/docT5query/passage-predictions
!wc predicted_queries_topk.txt-1004000
```

将预测查询附加到原始段落集合中：

```text
!python /data/students/nieyj/code/docT5query/convert_msmarco_passage_to_anserini.py \   --collection_path=/data/students/nieyj/code/docT5query/data/collection.tsv \    predictions/predicted_queries_topk.txt-1004000 \   --output_folder=/data/students/nieyj/code/docT5query/output/msmarco-passage-expanded
```

在扩展的段落上使用 Anserini 创建一个索引：

```text
!sh /data/students/nieyj/code/docT5query/anserini/target/appassembler/bin/IndexCollection \  -collection JsonCollection -generator DefaultLuceneDocumentGenerator \   -threads 9 -input /data/students/nieyj/code/docT5query/output/msmarco-passage-expanded -index lucene-index-msmarco-passage-expanded
```

数据集中的每个查询检索 1000 个段落：

```text
!sh /data/students/nieyj/code/docT5query/anserini/target/appassembler/bin/SearchCollection \   -index /data/students/nieyj/code/docT5query/data/lucene-index-msmarco-passage-expanded -topics /data/students/nieyj/code/docT5query/data/queries.dev.small.tsv \   -topicreader TsvInt \    -output /data/students/nieyj/code/docT5query/anserini/runs/run.msmarco-passage-expanded.dev.small.txt \   -bm25 \   -hits 1000 -threads 8
```

eval 脚本评估结果

```text
!python /data/students/nieyj/code/docT5query/anserini/tools/scripts/msmarco/msmarco_doc_eval.py --judgments /data/students/nieyj/code/docT5query/data/qrels.dev.small.tsv --run /data/students/nieyj/code/docT5query/anserini/runs/run.msmarco-passage-expanded.dev.small.txt
```

使用dureader的数据集放进T5模型进行训练

```text
!python check0.py
```
