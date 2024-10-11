from abc import ABC
from numpy.typing import NDArray
from python.OCRModel.ModelAPIs.Utils.DataRepresentation import TextPrediction
from typing import Iterable
class ModelInterface(ABC):
    def get_model_info(self) -> str:
        raise NotImplementedError("Interface method was not implemented!")
    def process_image(self, image:NDArray[float]) -> Iterable[TextPrediction]:
        raise NotImplementedError("Interface method was not implemented!")
    def process_images(self, images:list[NDArray[float]]) -> Iterable[Iterable[TextPrediction]]:
        raise NotImplementedError("Interface method was not implemented!")