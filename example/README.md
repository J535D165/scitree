# Create example folder structures

## Makita (`example_makita`)

Install ASReview and ASReview Makita
```sh
pip install asreview-makita
```

Build a simulation project and run the jobs.
```sh
mkdir -p example/example_makita/data
curl https://raw.githubusercontent.com/asreview/systematic-review-datasets/master/datasets/Bos_2018/output/Bos_2018.csv --output example/example_makita/data/Bos_2018.csv
cd example/example_makita/
asreview makita template arfi
touch LICENSE.txt
sh jobs.sh
```


```python
files = list(map(str,Path(".").glob("**/*")))
```
