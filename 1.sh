cd /data/students/nieyj/code/docT5query/passage-predictions

for i in $(seq -f "%03g" 0 17); do
    echo "Processing chunk $i"
    paste -d" " predicted_queries_topk_sample0[0-3]?.txt${i}-1004000 \
    > predicted_queries_topk.txt${i}-1004000
done

cat predicted_queries_topk.txt???-1004000 > predicted_queries_topk.txt-1004000