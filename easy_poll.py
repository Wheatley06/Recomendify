answer = None


async def yes(_, __):
    global answer
    answer = "Yes"


async def no(_, __):
    global answer
    answer = "No"