
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import StackingRegressor

def get_models():
    base_models = [
        ('lr', LinearRegression()),
        ('knn', KNeighborsRegressor()),
        ('tree', DecisionTreeRegressor())
    ]
    meta_model = GradientBoostingRegressor()
    model = StackingRegressor(estimators=base_models, final_estimator=meta_model)
    return model
