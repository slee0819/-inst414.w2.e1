import argparse
from nltk.tokenize import TweetTokenizer
import nltk
import string 
nltk.download('punkt')

def counts(Testfile):
    tknzr = TweetTokenizer(preserve_case = False)
    counts = dict()

    with open(Testfile, 'r', encoding = 'utf-8') as TF:
        for sentence in TF:
            words = tknzr.tokenize(sentence)
            for word in words:
                if word in string.punctuation:
                    continue
                else:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1

parser = argparse.ArgumentParser()
parser.add_argument('Testfile', help=" The name of the TXT file that can count words.")
args = parser.parse_args()

if __name__ == "__ main__":
    for i in range(10):
        print(f'{counts(args.Testfile)[i][0]}\t{counts(args.Testfile)[i][1]}')