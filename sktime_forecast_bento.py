import yfinance as yf
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from pandas._libs.tslibs.period import Period
from sktime.forecasting.arima import ARIMA
from sktime.forecasting.base import ForecastingHorizon
import pandas as pd


@env(infer_pip_packages=True)
@artifacts([])
class SktimeForecastBento(BentoService):
    @api(input=JsonInput())
    def predict(self, input):
        stock = yf.Ticker(input["ticker"])
        hist = stock.history(period="max")
        hist.index = hist.index.map(lambda date: date.to_period(freq="M"))
        data = hist[~hist.index.duplicated(keep="first")]["Close"]

        forecaster = ARIMA(
            order=(3, 1, 0), seasonal_order=(0, 1, 0, 12),
            suppress_warnings=True
        )
        forecaster.fit(data)

        fh = ForecastingHorizon(pd.to_datetime(["2021-03", "2021-04", "2021-05"]).map(lambda date: date.to_period(freq="M")), is_relative=False)
        y_pred = forecaster.predict(fh)

        y_pred.index = y_pred.index.map(lambda date: str(date))
        return y_pred.to_dict()
