# StockClock

> A stock price prediction algorithm powered by `bentoml` and `sktime`

Inspired by the recent surge of the GME stock, our hackathon group decided to 
create a naive stock price prediction model with `sktime`. Because our only 
predictor is time, an ARIMA model is trained for each stock's history on each 
request to the API.

Because of the way our model is designed, it has no knowledge of all the other
factors that influence stock prices: earnings reports, management changes,
etc. As a result the model will not predict any extraordinary events like the 
GME surge. It does work fairly well though!

## Development
After cloning the project, install all the required dependencies.
~~~
python -m venv venv # Optional, create a virtual environment named venv
source venv/bin/activate # Use the virtual environment
pip install -r requirements.txt
~~~

You can generate a Bento with the following command
~~~
python -m stockclock
~~~

You can then run the Bento
~~~
bentoml serve StockClock:latest
~~~

After doing that, start a proxy server to add CORS headers.
~~~
lcp --proxyUrl http://localhost:5000
~~~
