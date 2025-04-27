from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI()

code_prompt = PromptTemplate(
    input_variables=["task", "language"],
    template="Write a very short {language} function that will {task}."
)
test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="Write a test for the following {language} code:\n{code}"
)

# Create runnable sequences using the pipe operator
code_chain = code_prompt | llm
test_chain = test_prompt | llm

# Generate code first
code_result = code_chain.invoke({
    "language": args.language,
    "task": args.task
})

# Then generate test using the code result
test_result = test_chain.invoke({
    "language": args.language,
    "code": code_result
})

print(">>>>>> GENERATED CODE:")
print(code_result)

print(">>>>>> GENERATED TEST:")
print(test_result)
