from stockclock import StockClock

service = StockClock()
service.save()

service.start_dev_server()

while True:
    pass
