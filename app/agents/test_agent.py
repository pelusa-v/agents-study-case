from .client import client

def print_some_beautiful_message(name : str):
    """This function prints beautiful messages that motivate, given an string name"""
    print(name + ", You're beautiful!!!!")

function_metadata = {
  "name": "print_some_beautiful_message",
  "description": "This function prints beautiful messages that motivate, given a name",
  "parameters": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of a person"
        },
      }
  },
  "required": ["name"]
}

def test_agent():

    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a motivator, expert in saying good and nice phrases"},
            {"role": "user", "content": "Can you tell me something nice?, my name is Bob"},
        ],
        tools=[
            {
                "type": "function",
                "function": function_metadata
            }
        ],
        tool_choice="auto"
    )

    for c in res.choices:
        print(c.finish_reason)
        print(c.message)
        print(c.message.role)
        for t in c.message.tool_calls:
            print(t.function.arguments)
            print(t.function.name)
