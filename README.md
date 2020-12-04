# VTMS-ER
Vietnamese tone mark support &amp; Emojis recommendation
###### tags: `NLP` `Recommendation` `Vietnamese` `KNN` `Sentiment Analysis` `Transformer Model`

## idea :  
Drawio here : [Breakdown Idea](https:///drive.google.com/file/d/16jk5yjFy0tcMC7L4FGFLJHrv0pZcVLbA/view?usp=sharing)

![](https://i.imgur.com/wMX3vOM.png)

### Relatives
- NLP
- Transformer model
- KNN (for recommend)
- Sentiment analysis 
- POS tagging (Finding Nouns, Adj,...)

## List of things :  
### Dataset from wikimedia:  
- wikidumps the latest
`!wget https://dumps.wikimedia.org/viwiki/20201120/viwiki-20201120-pages-articles.xml.bz2`
- wikiextractor `https://github.com/attardi/wikiextractor.git`

Number of sequences:  **3624432** => **3.6M** sentences, enough for humanity knowledge. But only work with contents, news,...it's really bad with conversation.

For another one who need a clean file :
``install gdown 
using !gdown --id 14gEebiiRN_IHM65cb6pd-YM02FH8rUiV``  #to get the clean dataset from wikimedia (3.6M sentences)

### another dataset for conversation, chitchat : 
Loading / 3-12-2020



### Preprocess data: 

#### Make dataset : 
List "**có dấu**"
```
    intab_l = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
    intab_u = "ẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
```
List "**khong dau**"

```
    intab_l = "aaaaaaaaaaaaaaaaaoooooooooooooooooeeeeeeeeeeeuuuuuuuuuuuiiiiiyyyyyd"
    intab_u = "AAAAAAAAAAAAAAAAAOOOOOOOOOOOOOOOOOEEEEEEEEEEEUUUUUUUUUUUIIIIIYYYYYD"
```
**=> Looping & replace every single alphabet in every single word of  sentences.**

### TRANSFORMER MODEL
it is the same with this tutorials : [translate Portuguese to English](https://www.tensorflow.org/tutorials/text/transformer)


### Tune Model
![](https://i.imgur.com/Rc7tIsC.png)
The original paper working on Germany to English :https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
![](https://i.imgur.com/2NncMU0.png)


### Step to go : 

1. Finish 1st model
2. Turn checkpoint, function, preprocess to ONE => mean for running the next model without train.
3. Emoji idea, dataset, recommend system (1 or 2 model maybe)
4. Finish the picepline of project
5. Optimizer the model
- another dataset
- Tuning for better acuracy
6. Building Flask for Demo


## PART 2 : EMOJI RECOMMENDATION
### 1. Data crawling : Using BS_4 and crawl html parse from emojiall
### 2. Data label for Pos_tagging using pandas
### 3. Building a threshold system for :
- Pos_tagging Noun/Adj...words from sentences
- Sentiment Analysis for a whole sentence without Noun or Adj.

## PART 3 : FLASK, PIPEPLINE CONNECTION

### LOADING....