import click
import numpy as np
import pandas as pd
from numpy import pi


# create a group to create different subcomments
@click.group()
def geometric_group():
    pass


@geometric_group.command()
# number is the number of steps between 0 and 2 pi
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@geometric_group.command()
# number is the number of steps between 0 and 2 pi
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    geometric_group()
