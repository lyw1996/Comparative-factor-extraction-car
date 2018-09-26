# Comparative-factor-extraction-car
刘雨薇，南京理工大学，2014级本科

## Table of Contents

- Introduction
- Datasets
- Usage
- Examples
- Note
- Citation

## Introduction

这是我的本科毕业设计(基于机器学习的商品评论要素抽取方法)的一部分代码。

## Datasets

- 比较句语料:COAE2013（第五届中文倾向性评测大会）任务二评测数据中汽车领域比较句
- 比较词候选词典:学姐自己整理的554个比较词候选


## Usage

1.数据预处理

   ```latex
   Usage: python firsttxt.py  
	(用于任务2.1中将比较句抽取，由于测试集基本答案不对，靠人工标注)
	然后自己将比较句进行五元组标注
   ```

2.特征抽取(包括测试数据和训练数据)

   ```latex
   Usage: python train2txt[num].py  [num] 
          python test2txt[num].py  [num] 
   num:  从1到6分别对应论文中的模版1到6
   ```

3.特征工程实现

   ```latex
   Usage: python template.py 
	对论文中的特征模版使用CRF++工具所需要的格式实现
   ```

4.模型训练与学习

   ```latex
   Usage:
	① 训练程序
	命令行: % crf_learn template_file train_file model_file
	有四个主要的参数可以调整：
	-a algotithm：表示两种算法的选择。
	-c float：用于设置条件随机场模型的hyper-parameter。当c数值变大，条件随机场拟合数据程度也随之变高。由此看来，该参数用于更改数据使得模型在不拟合和过度拟中能够获得平衡。
	-f NUM：用于设置特征的cut-off threshold参数。有些训练数据特征次数太少，会有噪声，影响实验数据。该数值默认值为1。当训练和测试数据非常庞大之后，可以将该数值NUM设置大于1，过滤掉只出现一次的特征，减少噪声。
	-p NUM：该数据用于合理使用线程，当电脑有多个CPU，设置该数值NUM，将线程统筹到各个CPU上，提高计算效率。
	② 测试程序
	命令行：% crf_test -m model_file test_files
	有两个主要的参数可以调整：
	-v：表示预测标签的概率值。
	-n：表示不同可能序列的概率值。
	(本篇论文均采用默认值，在CRF++文件夹的命令行实现)
   ```

5.评估结果

   ```latex
   Usage: python AllEvaluation.py 
	对文中六个模版训练出的结果一起进行评估
   ```
## Examples

1.模型训练与学习

   ```latex
   e.g. crf_learn template1.txt trainT1.txt model1
	(根据T1训练数据，训练出了model1模型)
	e.g. crf_test -m model1 testT1.txt >> outputT1.txt
	(根据T1训练好的模型，使用测试集进行测试，并将结果输出到outputT1.txt中)
   ```

## Note

论文中将我的最好数据和COAE2013最大值做了比较，下面是COAE2013任务2.2最大值的数据。

| **比较要素**  | **精准评测准确率** | **精准评测召回率** | **精准评测F1值** | **覆盖评测准确率** |  **覆盖评测准确率**  |**覆盖评测F1值**  |
| :----------: | :--------------: | :--------------: | :-------------: | :--------------: | :----------------: | :-------------: |
|      PROD    |       67.77      |       66.05      |      64.30      |       82.67      |        73.58       |      71.58      |
|      ATTR    |       66.05      |       62.52      |      60.78      |       77.94      |        67.51       |      65.69      |


## Citation

如果您使用此代码，请引用以下文章：

[1] 刘雨薇. 基于机器学习的商品评论要素抽取方法[D]. 南京理工大学, 2018.

更多问题，联系369310624@qq.com
