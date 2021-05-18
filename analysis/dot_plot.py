# Third Party Library
import pandas as pd
import plotly.graph_objs as go
from loguru import logger


def dot_plot(title, filename, gen_num, step=1):
    path = f'./performance/test_{title}/populations/{filename}'
    df = pd.read_csv(path, header=None)
    x1 = df.iloc[::, ::2]
    x2 = df.iloc[::, 1::2]
    logger.debug(f'{x1} {x2}')
    fig = go.Figure()

    for x in range(0, gen_num, step):
        # logger.debug(f'{len(df.columns)=} {x=}')
        fig.add_trace(
            go.Scatter(
                x=x1.loc[x],
                y=x2.loc[x],
                mode="markers",
                marker=dict(size=12),
                name=f"Gen {x}",
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title="x",
        yaxis_title="y",
    )

    fig.show()


if __name__ == '__main__':
    targets = [
        # ('annealling_float_min', '16.csv', 30),
        # ('hillclimbing_float_min', '60.csv', 30),
        # ('ga_float_min', '30.csv', 30),
        ('niching_float_max_pow15', f'{x+1}.csv', 100, 10)
        for x in range(20)
    ]

    for t in targets:
        dot_plot(*t)
