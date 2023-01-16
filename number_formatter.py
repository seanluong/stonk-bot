UP = "🚀"
DOWN = "🔻"

MONEY_BAG = "💰"
MONEY_FLIES = "💸"


def format_price(price):
    return "${:,.5f}".format(price)

def format_growth_rate(growth):
    direction, reaction = "", ""
    growth_pc = growth * 100
    coef = int(1 + abs(growth_pc) / 5)
    if growth > 0:
        direction = UP
        reaction = "{}".format(MONEY_BAG * coef)
    else:
        direction = DOWN
        reaction = "{}".format(MONEY_FLIES * coef)
    return " | {:,.2f}% {}{}".format(growth_pc, direction, reaction)
