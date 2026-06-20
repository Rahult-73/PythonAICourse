from Tools.GetWeather import getweather

def run_tool(tool_name, tool_input):

    # ----------------------------------------
    # WEATHER TOOL
    # ----------------------------------------

    if tool_name == "weather":

        return getweather(
            tool_input
        )
    return "Unknown tool"