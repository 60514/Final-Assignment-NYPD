import re
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

def make_filename(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()

def save_similarity_charts(similarity_scores: pd.DataFrame, output_directory: Path) -> None: # save one chart for each work
    output_directory.mkdir(parents = True, exist_ok = True)

    for work_name in similarity_scores.index:
        scores_to_other_works = similarity_scores.loc[work_name].drop(work_name)

        figure, axis = plt.subplots(figsize = (10, 6))

        axis.bar(
            scores_to_other_works.index,
            scores_to_other_works.values,
            color = "steelblue",
        )

        axis.set_title(f"Similarity of {work_name} to other works")
        axis.set_xlabel("Compared work")
        axis.set_ylabel("Similarity score (0–100)")
        axis.set_ylim(0, 100)

        axis.tick_params(axis="x", rotation=30)
        figure.tight_layout()

        file_name = f"similarity_{make_filename(work_name)}.png"
        figure.savefig(output_directory / file_name)

        plt.close(figure)