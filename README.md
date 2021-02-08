# Stonk Clonk 📈

> A stock price prediction algorithm powered by `bentoml` and `sktime`

Inspired by the recent surge of the GME stock , our hackathon group decided to 
create a naive stock price prediction model with `sktime`. Because our only 
predictor is time, an ARIMA model is trained for each stock's history on each 
request to the API.

Because of the way our model is designed, it has no knowledge of all the other
factors that influence stock prices: earnings reports, management changes,
etc. As a result the model will not predict any extraordinary events like the 
GME surge. It does work fairly well though!

## 💻 Development
After cloning the project, install all the required dependencies.
~~~
python -m venv venv # Optional, create a virtual environment named venv
source venv/bin/activate # Use the virtual environment
pip install -r requirements.txt
~~~

You can generate a Bento with the following command
~~~
python -m stonkclonk
~~~

You can then run the Bento
~~~
bentoml serve StonkClonk:latest
~~~

After doing that, start a proxy server to add CORS headers, or use an online one.
~~~
lcp --proxyUrl http://localhost:5000
~~~


## 🚀 Technology Stack:
<img alt="HTML5" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/><img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

Served by a BentoML server running on Heroku

## :heart: Contributing

If you have suggestions for how stonkclonk could be improved, or want to report a bug, open an issue! Contributions of all kinds are welcomed!

For more, check out the [Contributing Guide](./CONTRIBUTING.md).

## 📄 License

[MIT](LICENSE) © 2021 MLH Fellowship

Made with 🚀🚀🚀 by [Chau Vu](https://github.com/cqvu), [Aanand Kainth](https://github.com/akainth015), and [Drew Ehrlich](https://github.com/deehrlic) during the Orientation Hackathon of the MLH Fellowship Open Source Batch 2, Spring 2021.
