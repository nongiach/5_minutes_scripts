#!/usr/bin/env python3
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import clize
from wordcloud import WordCloud, STOPWORDS
import collections

# subfinder -d [domain_name_here] > /tmp/domains
# rg -N '[^.]*\.[^.]*\.[^.]*$' /tmp/domains -o > /tmp/top_domains

## give this script a text of one line per word and a random image
## the text will be counted and show in a wordcloud by frequency
## the image will be used as a mask for display
def generate_wordcloud(file_text, file_mask):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, file_text)).read()

    # read the mask image
    image_mask = np.array(Image.open(path.join(d, file_mask)))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(width=780, height=480, background_color="white", max_words=2000, mask=image_mask,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    word_counts = collections.Counter(text.split('\n'))
    for word, value in word_counts.items():
        word_counts[word] = min(20, value)
    print(word_counts)
    wc.generate_from_frequencies(word_counts)

    # store to file
    wc.to_file(path.join(d, "generated.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    clize.run(generate_wordcloud)
