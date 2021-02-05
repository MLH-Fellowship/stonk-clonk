from sklearn import datasets, svm

from sktime_forecast_bento import SktimeForecastBento

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC(gamma="scale")
clf.fit(X, y)

service = SktimeForecastBento()
service.pack('model', clf)
service.save()
