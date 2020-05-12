from tkinter import *
from tkinter.ttk import *
import sys, tweepy, csv, re
from textblob import TextBlob
import matplotlib.pyplot as plt

window = Tk()
window.title("Welcome to Multilingual Twitter Sentiment Analysis app")
window.configure(background="aqua")
window.geometry('1350x1200')
lbl = Label(window, text="Enter The search Term", font=("Arial", 20))
lbl.grid(column=0, row=0)
txt = Entry(window, width=35)
txt.grid(column=20, row=0)

lbl1 = Label(window, text="Enter Number of terms", font=("Arial", 20))
lbl1.grid(column=0, row=2)
txt1 = Entry(window, width=35)
txt1.grid(column=20, row=2)

lbl1 = Label(window, text="Select Language", font=("Arial", 20))
lbl1.grid(column=0, row=5)

combo = Combobox(window)
combo['values'] = ("English", "Hindi", "French", "Gujrati", "Bengali")
combo.current(1)  # set the selected item
combo.grid(column=20, row=5)


def clicked():
    # lbl.configure(text="Button was clicked !!")
    class SentimentAnalysis:

        def __init__(self):
            self.tweets = []
            self.tweetText = []

        def DownloadData(self):
            # authenticating
            consumerKey = 'J0vuqc7HWbRyykdXlL9FqhZPD'
            consumerSecret = 'tC2LkuieNUq1Flcth8FmpZTsn3GinQCCt40tym6d3eJytc3UhR'
            accessToken = '364792889-Iq0PboYQAkWCUy6cnPZT6m9Ol6YeTKew4aX9vQOJ'
            accessTokenSecret = 'nFj85l0E4ptD49PDjZuEsynZIa08JFc87r03UBdAoWuPl'
            auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            auth.set_access_token(accessToken, accessTokenSecret)
            api = tweepy.API(auth)

            searchTerm = txt.get()  # input("Enter Keyword/Tag to search about: ")
            NoOfTerms = int(txt1.get())  # int(input("Enter how many tweets to search: "))

            lang1 = combo.get()
            if (lang1 == 'English'):
                lang1 = 'en';
            if (lang1 == 'Hindi'):
                lang1 = 'hi';
            if (lang1 == 'French'):
                lang1 = 'fr';
            if (lang1 == 'Bengali'):
                lang1 = 'bn';
            if (lang1 == 'Gujrati'):
                lang1 = 'gu';
            print(lang1)
            self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang=lang1).items(NoOfTerms)

            polarity = 0
            positive = 0
            negative = 0
            neutral = 0

            for tweet in self.tweets:

                # print(tweet.text.encode("utf-16be"))#.decode("utf-16be"))
                en_blob = TextBlob(tweet.text)  # .encode("utf-16be").decode("utf-8"))
                print(str(en_blob))

                x = en_blob.translate(to='en')
                # print("***********"+str(x)+"*********")
                analysis = TextBlob(str(x))

                # print(analysis.sentiment)# print tweet's polarity
                polarity += analysis.sentiment.polarity

                if (analysis.sentiment.polarity == 0):
                    neutral += 1
                elif (analysis.sentiment.polarity > 0):
                    positive += 1
                elif (analysis.sentiment.polarity < 0):
                    negative += 1

            positive = self.percentage(positive, NoOfTerms)
            negative = self.percentage(negative, NoOfTerms)
            neutral = self.percentage(neutral, NoOfTerms)

            polarity = polarity / NoOfTerms

            print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
            print()
            print("General Report: ")

            if (polarity == 0):
                print("Neutral")
            elif (polarity > 0):
                print("Positive")
            elif (polarity < 0):
                print("Negative")

            print()
            print("Detailed Report: ")
            print(str(positive) + "% people thought it was positive")
            print(str(neutral) + "% people thought it was neutral")
            print(str(negative) + "% people thought it was negative")

            self.plotPieChart(positive, negative, neutral, searchTerm, NoOfTerms)

        def cleanTweet(self, tweet):
            # Remove Links, Special Characters etc from tweet
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

        def percentage(self, part, whole):
            temp = 100 * float(part) / float(whole)
            return format(temp, '.2f')

        def plotPieChart(self, positive, negative, neutral, searchTerm,
                         noOfSearchTerms):
            labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]',
                      'Negative [' + str(negative) + '%]']
            sizes = [positive, neutral, negative]
            colors = ['blue', 'lightgreen', 'red']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90)
            plt.legend(patches, labels, loc="best")
            plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
            plt.axis('equal')
            plt.tight_layout()
            plt.show()

    if __name__ == "__main__":
        sa = SentimentAnalysis()
        sa.DownloadData()


btn = Button(window, text="Fetch Tweets", command=clicked)
btn2 = Button(window, text="Analyze tweets")  # ,command=clicked)
btn3 = Button(window, text="Print Tweets")  # ,command=clicked)
btn.grid(column=10, row=10)
btn2.grid(column=30, row=10)
btn3.grid(column=50, row=10)
window.mainloop()
