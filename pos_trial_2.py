



from flask import Flask, request, render_template
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize
from yellowbrick.text.base import TextVisualizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import re
import os


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text


@app.route('/', methods=['POST'])

def adj():
    text = request.form['text']
    word_tokens = word_tokenize(text)
    pos = nltk.pos_tag(word_tokens)
    selective_pos = ['JJ','JJR','JJS','RB','RBS','RBR']
    selective_pos_words = []
    for word,tag in pos:
        if tag in selective_pos:
            selective_pos_words.append((word))

    COLOR = ['#9999ff']

    my_list = selective_pos_words
    regex = re.compile(r'\b(?:{0})\b'.format('|'.join(my_list)))
                       
    i = 0; output = "<html>"
    for m in regex.finditer(text):
        output += "".join([text[i:m.start()],
                       "<strong><span style='color:%s'>" % COLOR[0],
                       text[m.start():m.end()],
                       "</span></strong>"])
        i = m.end()
    res = ("".join([output, text[m.end():], "</html>"]))
    return res


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)                                                                                                                                         
