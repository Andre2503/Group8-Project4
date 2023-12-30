# FND app meaning of Fake News Detector app
import gradio as gr
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")


# the news_analyzer function is the main function of the app.
# it takes the news tittle and body as input and return the
# result as output.
def news_analyzer(news_tittle, news_body):
    transformed_data = data_normalization(news_tittle, news_body)
    answer = transformed_data
    # answer = our_model_name.predict(transformed_data)

    return f"The news is {answer}"


# the data_normalization function clean and normalize the data as
# our model requires.
def data_normalization(news_title, news_body):
    clean_title = delete_special_characters(news_title)
    clean_body_text = delete_special_characters(news_body)
    final_clean_title = delete_stop_words(clean_title)
    final_clean_body_text = delete_stop_words(clean_body_text)
    standardized_data = f"{final_clean_title} {final_clean_body_text}"
    return standardized_data


# the delete_special_characters function delete all the
# special characters in the text.
def delete_special_characters(text):
    special_characters_deleted = re.sub(r"[^\w\s]|[\d]", "", text)
    return special_characters_deleted


# the delete_stop_words function delete all the insignificant words (stop words)
# The default list of English stop words includes:
# a, an, and, are, as, at, be, but, by, for, if, in, into, is, it, no, not, of, on, or, such,
# that, the, their, then, there, these, they, this, to, was, will and with.
def delete_stop_words(text):
    # create a list
    list_significant_words = []
    # stop_words get a list of common English stop words provided by nltk
    stop_words = set(stopwords.words("english"))
    # word_tokens is a list of all words in the text.
    # word_tokenize is a function provided by nltk
    # to split the text into words.
    word_tokens = word_tokenize(text)
    # significant_word is a variable of  non-stop word in the text.
    significant_word = [word for word in word_tokens if not word in stop_words]
    # list_significant_words is a string of all significant words in the text. 
    list_significant_words = "".join(significant_word)
    return list_significant_words


with gr.Blocks() as FND_app:
    tittle_news = gr.Textbox(label="Tittle_news")
    body_news = gr.Textbox(label="Body_news", max_lines=10)
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Analyze")
    greet_btn.click(
        fn=news_analyzer,
        inputs=[tittle_news, body_news],
        outputs=output,
        api_name="FND_API",
    )

FND_app.launch()

# **************************************************************
# import gradio as gr


# def greet(name, is_morning, temperature):
#     salutation = "Good morning" if is_morning else "Good evening"
#     greeting = f"{salutation} {name}. It is {temperature} degrees today"
#     celsius = (temperature - 32) * 5 / 9
#     return greeting, round(celsius, 2)


# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     outputs=["text", "number"],
# )
# demo.launch()
