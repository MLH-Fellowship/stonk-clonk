import pandas as pd
import yfinance as yf
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from sktime.forecasting.arima import ARIMA
from sktime.forecasting.base import ForecastingHorizon
from datetime import datetime, timedelta


@env(infer_pip_packages=True)
@artifacts([])
class StockClock(BentoService):
    @api(input=JsonInput(http_input_example='{"ticker": "AAPL", "months": 3}'))
    def predict(self, request):
        stock = yf.Ticker(request["ticker"])
        hist = stock.history(period="5y", interval="1mo").to_period(freq="M")
        data = hist[~hist.index.duplicated(keep="first")]["Close"]

        forecaster = ARIMA(
            order=(3, 1, 0), seasonal_order=(0, 1, 0, 12),
            suppress_warnings=True
        )
        forecaster.fit(data)

        fh = ForecastingHorizon(
            pd.period_range(
                datetime.now() + timedelta(30),
                datetime.now() + timedelta(30 * request["months"]),
                freq="M"
            ),
            is_relative=False
        )
        y_pred = forecaster.predict(fh)

        output = data.append(y_pred)

        output.index = output.index.map(lambda date: str(date))
        return output.to_dict()
