from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact('model')])
class SktimeForecastBento(BentoService):
    @api(input=JsonInput())
    def predict(self, input):
        return self.artifacts.model.predict(input)
