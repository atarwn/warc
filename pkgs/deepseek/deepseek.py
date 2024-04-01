# python3
from openai import OpenAI
ProgramCycle = True

def deepseek_help():
    print("Deepseeek wishpy client v0.2")
    print("- Write any question to get answer")
    print("- Or write -exit to exit the program")
def deepseek_ver():
    print("v0.1")
def deepseek():
    global ProgramCycle
    print("| Deepseek wishpy client v0.1 \\")
    print("| Write -exit to exit         /")
    ProgramCycle = True

    client = OpenAI(api_key="sk-5845b49c08d944149457c1425cc3d2db", base_url="https://api.deepseek.com/v1")

    while ProgramCycle:
        prompt = input("You: ")

        if prompt[0] != '-':
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": f"{prompt}"},
                ]
            )
            print(f"deepseek: {response.choices[0].message.content}")
        elif prompt[0] == '-':
            if '-exit' in prompt:
                print('deepseek: Thank you for using me! If you need any assistance in the future, feel free to ask me anything.')
                ProgramCycle = False
                return
            else:
                print("System: Unknown operator")
