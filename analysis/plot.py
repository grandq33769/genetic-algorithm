# Standard Library
from random import randint

# Third Party Library
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from loguru import logger

COLOR = [
    ('rgb(0,100,80)', 'rgba(0,100,80,0.3)'),
    ('rgb(0,176,246)', 'rgba(0,176,246,0.3)'),
    ('rgb(231,107,243)', 'rgba(231,107,243,0.3)'),
]

EPISODE = 50
SHOW_ROUND = 50


def line_chart(path, title):
    rand_idx = randint(0, len(COLOR) - 1)
    line_color, fill_color = COLOR[rand_idx]

    aggregated_df = pd.DataFrame()
    for x in range(1, EPISODE):
        df = pd.read_csv(f'{path}/{x}.csv', header=None)
        aggregated_df[str(x)] = df.mean(axis=1)
        # lines.append(go.Scatter(
        #     x=df['idx'].head(25),
        #     y=df['mean'].head(25),
        #     mode='lines'
        # ))
    aggregated_df['mean'] = aggregated_df.mean(axis=1)
    aggregated_df['std'] = aggregated_df.std(axis=1)
    aggregated_df['round'] = np.arange(len(aggregated_df))
    logger.debug(aggregated_df)

    df = aggregated_df.head(SHOW_ROUND)

    return [
        go.Scatter(
            name=title,
            x=df['round'],
            y=df['mean'],
            mode='lines',
            line_color=line_color,
            line=dict(
                width=4,
            ),
        ),
        go.Scatter(
            name=f'{title} Upper Bound',
            x=df['round'],
            y=df['mean'] + df['std'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False,
        ),
        go.Scatter(
            name=f'{title} Lower Bound',
            x=df['round'],
            y=df['mean'] - df['std'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor=fill_color,
            fill='tonexty',
            showlegend=False,
        ),
    ]


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
                y=x2.loc[x + 1],
                mode="markers",
                marker=dict(size=12),
                name=f"Gen {x}",
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title="x1",
        yaxis_title="x2",
    )

    fig.show()


if __name__ == '__main__':
    lines = []
    ga_title = 'annealling_float_min'
    ga_path = f'./performance/test_{ga_title}/fitnesses'
    lines.extend(line_chart(ga_path, ga_title))

    ga_title = 'ga_float_min'
    ga_path = f'./performance/test_{ga_title}/fitnesses'
    lines.extend(line_chart(ga_path, ga_title))

    ga_title = 'hillclimbing_float_min'
    ga_path = f'./performance/test_{ga_title}/fitnesses'
    lines.extend(line_chart(ga_path, ga_title))

    ga_fig = go.Figure(lines)
    ga_fig.update_layout(
        yaxis_title='obj_func (x1,x2)',
        title="Convergence Performance (Min)",
        hovermode="x",
    )
    ga_fig.show()

    targets = [
        ('annealling_float_min', '16.csv', 20),
        ('hillclimbing_float_min', '60.csv', 7),
        ('ga_float_min', '30.csv', 30, 4),
    ]

    for t in targets:
        dot_plot(*t)
