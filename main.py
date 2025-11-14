from models import load_llm


if __name__ == "__main__":
    llm = load_llm()
    response = llm.invoke("Why do parrots talk?")
    print(response)