from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from key import openrouter_key
import os

# Setup
os.environ['OPENAI_API_KEY'] = openrouter_key
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    model="deepseek/deepseek-r1:free",
    temperature=0.6
)

# Chain 1: Restaurant name
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open {cuisine} restaurant. Suggest only one fancy name for this.suggest only name of 3 words do not include any extra contents"
)
#name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

# Chain 2: Menu items
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest 10 menu items for {restaurant_name}, return it as a comma separated string do not return extra contents"
)
#food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

name_chain = prompt_template_name | llm
food_items_chain = prompt_template_items | llm

def generate_rst_food_items(cuisine):

    restaurant_name=name_chain.invoke({'cuisine':cuisine}).content

    menu_items=food_items_chain.invoke({"restaurant_name":restaurant_name}).content

    return {"restaurant_name":restaurant_name, "menu_items":menu_items}

if __name__=="__main__":
    result=generate_rst_food_items("Indian")
    print(result)




# Sequential chain needs input + output variables defined
# chain = SequentialChain(
#     chains=[name_chain, food_items_chain],
#     input_variables=['cuisine'],
#     output_variables=['restaurant_name', 'menu_items']
# )

# # Run
# response = chain({'cuisine': 'Indian'})
# print(response)
