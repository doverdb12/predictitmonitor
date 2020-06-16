## PredictIt Monitor

This is a simple script to poll https://www.predictit.org/ on an interval to get market data. It can be called simply using `pipenv run python main.py`, which will default to the VP Nomination market. It can also be called with `pipenv run python main.py <market_id>` or`pipenv run python main.py <market_id> <poll_interval>` to specify those parameters.