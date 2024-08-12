from openai import OpenAI
import prompts as p

def gpt_prompt(instruction,query, passage):
    prompt = f'{instruction}\nCONSULTA: "{query}"\nPASSAGEM: "{passage}\n"'
    return prompt

def gpt_answer(cli_gpt,prompt, max_tokens, model):
    response = cli_gpt.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def main():
    cli_gpt = OpenAI(api_key='chave openai')
    query = "do que é feita uma presa de narval"
    passage = "Alguns pesquisadores notaram os muitos túbulos e nervos que viajam através das presas do narval. Eles também notaram que a superfície de uma presa é muito sensível a estímulos. Os pesquisadores acreditam que as estruturas são usadas como órgãos dos sentidos."
    instruction = p.gpt_folha
    prompt = gpt_prompt(instruction,query,passage)
    response = gpt_answer(cli_gpt, prompt, 500, 'gpt-4o')
    print(response)


