from memory import Memory
from planner import run_planner
from executer import run_tool

# ----------------------------------------

# MEMORY INIT

# ----------------------------------------

memory = Memory()

print("AI Agent Started")
print("Type 'exit' to quit")

# ----------------------------------------

# MAIN CHAT LOOP

# ----------------------------------------

while True:

    # ----------------------------------------
    # USER INPUT
    # ----------------------------------------

    user_input = input("\nUser: ")

    # exit command
    if user_input.lower() == "exit":
        break

    # save user message
    memory.add(
        "user",
        user_input
    )

    # ----------------------------------------
    # AGENT REASONING LOOP
    # ----------------------------------------

    while True:

        # planner decides next step
        result = run_planner(
            memory.get()
        )

        print("\nPLANNER RESULT:")
        print(result)

        # safe extraction
        step = result.get("step")

        # ----------------------------------------
        # TOOL EXECUTION
        # ----------------------------------------

        if step == "TOOL":

            tool_name = result.get("tool")

            tool_input = result.get("content")

            print(f"\nRUNNING TOOL: {tool_name}")

            # execute tool
            tool_result = run_tool(
                tool_name,
                tool_input
            )

            print("\nTOOL RESULT:")
            print(tool_result)

            # save tool result to memory
            memory.add(
                "tool",
                tool_result
            )

        # ----------------------------------------
        # FINAL OUTPUT
        # ----------------------------------------

        elif step == "OUTPUT":

            final_answer = result.get(
                "content",
                "No response generated"
            )

            print("\nASSISTANT:")
            print(final_answer)

            # save assistant response
            memory.add(
                "assistant",
                final_answer
            )

            break

        # ----------------------------------------
        # INVALID STEP HANDLING
        # ----------------------------------------

        else:

            print("\nINVALID STEP RECEIVED")

            print(result)

            memory.add(
                "assistant",
                str(result)
            )

            break

