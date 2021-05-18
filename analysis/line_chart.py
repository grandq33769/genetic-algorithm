# Third Party Library
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from loguru import logger

COLOR = [
    ('rgb(0,100,80)', 'rgba(0,100,80,0.3)'),
    ('rgb(0,176,246)', 'rgba(0,176,246,0.3)'),
    ('rgb(231,107,243)', 'rgba(231,107,243,0.3)'),
    ('rgb(0,0,0)', 'rgba(0,0,0,0.3)'),
]

TOTAL = 60
ROUND = 30


def line_chart(path, title, color_idx):
    line_color, fill_color = COLOR[color_idx]

    aggregated_df = pd.DataFrame()
    for x in range(1, TOTAL):
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

    df = aggregated_df.head(ROUND)

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


if __name__ == '__main__':
    lines = []
    alg_title = 'ga_float_min_m1'
    data_path = f'./performance/test_{alg_title}/fitnesses'
    lines.extend(line_chart(data_path, alg_title, 0))

    alg_title = 'ga_float_min_m2'
    data_path = f'./performance/test_{alg_title}/fitnesses'
    lines.extend(line_chart(data_path, alg_title, 1))

    alg_title = 'ga_float_min_m4'
    data_path = f'./performance/test_{alg_title}/fitnesses'
    lines.extend(line_chart(data_path, alg_title, 2))

    alg_title = 'ga_float_min_m8'
    data_path = f'./performance/test_{alg_title}/fitnesses'
    lines.extend(line_chart(data_path, alg_title, 3))

    fig = go.Figure(lines)
    fig.update_layout(
        yaxis_title='obj_func (x1,x2)',
        title="Convergence Performance (Min)",
        hovermode="x",
    )
    fig.show()
