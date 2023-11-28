import openai
import os
import yaml
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers.json import parse_json_markdown

with open('prompts/prompts.yaml', 'r') as file:
    prompts = yaml.safe_load(file)


def create_model(key):
    os.environ['OPENAI_API_KEY'] = key

    llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
    prompt = PromptTemplate.from_template(prompts['template'])
    chain = LLMChain(prompt=prompt, llm=llm)

    return chain


def generate_summary(article_list, model):
  summaries = []
  for article in article_list:
    prompt_arguments = {"articleA": prompts['articleA'], "summarizationA": prompts['summarizationA'],
                        "articleB": prompts['articleB'], "summarizationB" : prompts['summarizationB'],
                        "summarizeMe": article}
    full_response = model.run(prompt_arguments)
    summary = parse_json_markdown(full_response)
    summaries.append(summary['3'])
  return summaries
