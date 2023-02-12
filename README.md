# Calmap-Visualize-MyTraining

- Calmap使って自分のトレーニングのログをgithubの草っぽくするレポジトリ

## 使い方

- 筋トレ用

```
python src/main.py --data ./data/power-training.csv --single --output output/power-training.png
```

![power-training.png](output/power-training.png)

![power-training-2023.png](output/power-training-2023.png)


- ジョギング用

```
python src/main.py --data ./data/jogging.csv --output output/jogging.png
```

![jogging.png](output/jogging.png)

![jogging-2023.png](output/jogging-2023.png)


- 山登り（累積和）

![hill-jogging](output/hill-jogging.png)