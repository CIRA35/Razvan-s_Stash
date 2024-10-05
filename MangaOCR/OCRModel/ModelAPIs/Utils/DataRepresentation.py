from dataclasses import dataclass


@dataclass
class TextPrediction():
    boundary: tuple[float, float, float, float]
    predicted_text: list[str]

