from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stopWords = set(stopwords.words("english"))
text ='Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly.Some machine learning methods. Machine learning algorithms are often categorized as supervised or unsupervised.Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able to provide targets for any new input after sufficient training. The learning algorithm can also compare its output with the correct, intended output and find errors in order to modify the model accordingly. In contrast, unsupervised machine learning algorithms are used when the information used to train is neither classified nor labeled. Unsupervised learning studies how systems can infer a function to describe a hidden structure from unlabeled data. The system doesn’t figure out the right output, but it explores the data and can draw inferences from datasets to describe hidden structures from unlabeled data. Semi-supervised machine learning algorithms fall somewhere in between supervised and unsupervised learning, since they use both labeled and unlabeled data for training – typically a small amount of labeled data and a large amount of unlabeled data. The systems that use this method are able to considerably improve learning accuracy. Usually, semi-supervised learning is chosen when the acquired labeled data requires skilled and relevant resources in order to train it / learn from it. Otherwise, acquiringunlabeled data generally doesn’t require additional resources. Reinforcement machine learning algorithms is a learning method that interacts with its environment by producing actions and discovers errors or rewards. Trial and error search and delayed reward are the most relevant characteristics of reinforcement learning. This method allows machines and software agents to automatically determine the ideal behavior within a specific context in order to maximize its performance. Simple reward feedback is required for the agent to learn which action is best; this is known as the reinforcement signal. Machine learning enables analysis of massive quantities of data. While it generally delivers faster, more accurate results in order to identify profitable opportunities or dangerous risks, it may also require additional time and resources to train it properly. Combining machine learning with AI and cognitive technologies can make it even more effective in processing large volumes of information.'
words = word_tokenize(text)
sentences = sent_tokenize(text)
sentenceValue = list(())
for i in range(len(sentences)):
    sentenceValue.append(0)
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
#print(freqTable)
#print(sentenceValue)
'''print(sentences,"\n")
x = len(sentences)
print(x)
word_arr = list(())
for i in range(0,21):
    #word[i] = len(word_tokenize(sentences[i]))
    #print(word)
    word_arr.append(len(word_tokenize(sentences[i])))
print(word_arr,"\n")
'''
i=0
for sentence in sentences:
    for wordValue in freqTable:
        if wordValue in sentence.lower():
            if(len(word_tokenize(sentence))>10):
                sentenceValue[i] += freqTable[wordValue]
            else:
                sentenceValue[i] += 0
    i = i+1
sumValues = 0
#print(sentenceValue)
i=0
for i in range(len(sentences)):
    sumValues += sentenceValue[i]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))
#print(average)
summary = ''
i=0
for sentence in sentences:
        if sentenceValue[i] > (1.5 * average):
            summary +=  " " + sentence
        i = i+1
print(summary)