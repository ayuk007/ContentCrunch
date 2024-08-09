import validators
from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_core.output_parsers import StrOutputParser
import nltk
# nltk.download("averaged_perceptron_tagger")

load_dotenv()

class Summarizer:
    def __init__(self):
        self.model_name = "Gemma-7b-It"
        self.temperature = 0.7
        self.llm_model = ChatGroq(model = self.model_name, temperature = self.temperature)
        self.prompt = Prompt_And_Header.prompt
        self.header = Prompt_And_Header.header
        self.chain = self.prompt | self.llm_model | StrOutputParser()
        # self.chain = load_summarize_chain(llm = self.llm_model, chain_type = "stuff", prompt = self.prompt)
    def summarize(self, url, model: str = None, temperature: float = None):

        if model != self.model_name:
            self.model_name = model
            self.llm_model.model = self.model_name
        if temperature != self.temperature:
            self.temperature = temperature
            self.llm_model.temperature = self.temperature

        if "youtube.com" in url:
            summary = self.summarize_youtube_content(url)
        else:
            summary = self.summarize_web_content(url)

        return summary    
    def summarize_youtube_content(self, url):
        loader = YoutubeLoader.from_youtube_url(youtube_url=url, add_video_info = True)
        data = loader.load()
        print("Data: ", data)
        summary = self.chain.invoke({"content": data[0].page_content})
        return summary
    
    def summarize_web_content(self, url):
        loader = UnstructuredURLLoader(urls = [url], ssl_verify = False, headers = self.header)
        data = loader.load()
        summary = self.chain.invoke({"content": data})
        return summary
    

@dataclass
class Prompt_And_Header:
    template = """
    You are an expert content creator.
    Your task is to read and understand content inside <content> tag and then create a brief summary.
    Content: <content>{content}</content>
    """
    prompt = PromptTemplate.from_template(
        template = template,
    )

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }