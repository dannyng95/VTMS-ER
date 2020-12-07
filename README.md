# vietnamese tone marks support & emoji recommendation

###### tags: `NLP` `Recommendation` `Vietnamese` `KNN` `Sentiment Analysis` `Transformer Model`

## idea :  
Drawio here : [Breakdown Idea](https:///drive.google.com/file/d/16jk5yjFy0tcMC7L4FGFLJHrv0pZcVLbA/view?usp=sharing)

![](https://i.imgur.com/hCkZByB.png)


### Relatives
- NLP
- Transformer Model (for language translate)
- Sentiment analysis 
- POS tagging (Finding Nouns, Adj,...)

## List of things :  
### Dataset from wikimedia:  
- wikidumps the latest
`!wget https://dumps.wikimedia.org/viwiki/20201120/viwiki-20201120-pages-articles.xml.bz2`
- wikiextractor `https://github.com/attardi/wikiextractor.git`

Number of sequences:  **3624432** => **3.6M** sentences, enough for humanity knowledge. But only work with contents, news,...it's really bad with conversation.

### another dataset for conversation, chitchat : 



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

## EMOJI RECOMENDATION System

### 1. Model 2 : Sentiment Analysis

#### Dataset : UIT-VSMEC (version 1.0) - Vietnamese Social Media Emotion Corpus 
Standard Vietnamese Social Media Emotion Corpus (UIT-VSMEC) with about 6,927 human-annotated sentences with **six emotion labels**, contributing to **emotion recognition** research in Vietnamese which is a low-resource language in Natural Language Processing (NLP). 
- Anger
- Suprise
- Enjoyment
- Sadness
- Fear
- Disgust
- Other


![](https://i.imgur.com/AavukFp.png)
#### .The result:
![](https://i.imgur.com/Ti7w4sq.png)

I got 88% F1-scored on train dataset.

### 2.Model 3 : POS Tagging 
Output Nouns & Adj (Important Words of a sentences) to findemoji


### 3.Emojis dataset:

Using Bs4 to crawling the dataset of emojis.

### 4.Threshold System Explain :  

Vietnamese emoji and description
