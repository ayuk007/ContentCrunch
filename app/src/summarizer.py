import nltk
import validators
from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
# nltk.download("averaged_perceptron_tagger")

load_dotenv()

class Summarizer:
    def __init__(self):
        self.model_name = "Gemma-7b-It"
        self.temperature = 0.7
        self.llm_model = ChatGroq(model = self.model_name, temperature = self.temperature)
        self.prompt = Prompt_And_Header.prompt
        self.header = Prompt_And_Header.header
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap = 0)
        # self.chain = self.prompt | self.llm_model | StrOutputParser()
        question_prompt_template = """
                  Please provide a summary of the following text.
                  TEXT: {text}
                  SUMMARY:
                  """

        question_prompt = PromptTemplate(
            template=question_prompt_template, input_variable=["text"]
        )
        self.chain = load_summarize_chain(llm = self.llm_model, chain_type = "refine", 
                                          refine_prompt = self.prompt, verbose = True,
                                          question_prompt = question_prompt, return_intermediate_steps = True)
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
        print("Loading documents----")
        loader = YoutubeLoader.from_youtube_url(youtube_url=url, add_video_info = True)
        data = loader.load()
        docs = self.text_splitter.split_documents(data)
        print("Splitting documents-----")

        summary = self.chain({"input_documents": docs})
        
        combined_summary = self.get_combined_summary(summary["intermediate_steps"])
        return combined_summary
    
    def summarize_web_content(self, url):
        loader = UnstructuredURLLoader(urls = [url], ssl_verify = False, headers = self.header)
        data = loader.load()
        docs = self.text_splitter.split_documents(data)
        # print("Docs: ", docs)

        summary = self.chain.run(docs)
        combined_summary = self.get_combined_summary(summary["intermediate_steps"])
        return combined_summary
    
    def get_combined_summary(self, summary_docs):
        combined_summary = "\n\n".join([doc.split("Summary:")[-1] for doc in summary_docs])
        return combined_summary
@dataclass
class Prompt_And_Header:
    template = """
    You are an expert content creator.
    Your task is to read and understand content inside <content> tag and then create a brief summary.
    Content: <content>{text}</content>
    """
    prompt = PromptTemplate.from_template(
        template = template,
        input_variable = ['text'],
    )

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

@dataclass
class Get_Max_Tokens:
    """
    This data class denotes to the total number of tokens that'll be used by models,
    i.e., input and output tokens
    """

    "llama-3.1-70b-versatile" = 8000 # 8192 allowed, has limit of 131K
    "llama-3.1-8b-instant" = 8000 # 8192 allowed, has limit of 131K
    "llama3-70b-8192" = 8000  # 8192
    "llama3-8b-8192" = 8000  # 8192
    "llama-guard-3-8b" = 8000 # 8192
    "mixtral-8x7b-32768" = 32000 # 32768
    "gemma-7b-it" = 8000 # 8192
    "gemma2-9b-it" = 8000 # 8192