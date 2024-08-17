from rest_framework import serializers 
from apis.models import localityDescription
 
 
class localityDescriptionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = localityDescription
        fields = (
                  'Id',
                  'MSSubClass',
                  'MSZoning',
                  'LotFrontage',
                  'LotArea',
                  'Street',
                  'Alley',
                  'LotShape',
                  'LandContour',
                  'Utilities',
                  'LotConfig',
                  'LandSlope',
                  'Neighborhood')
                  
                  
from apis.models import housingConditions
 
 
class housingConditionsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = housingConditions
        fields = (
                  'Id',
                  'Condition1',
                  'Condition2',
                  'BldgType',
                  'HouseStyle',
                  'OverallQual',
                  'OverallCond',
                  'YearBuilt',
                  'YearRemodAdd')
                  
                  
from apis.models import exteriorFeatures
 
 
class exteriorFeaturesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = exteriorFeatures
        fields = (
                  'Id',
                  'RoofStyle',
                  'RoofMatl',
                  'Exterior1st',
                  'Exterior2nd',
                  'MasVnrType',
                  'MasVnrArea',
                  'ExterQual',
                  'ExterCond',
                  'Foundation',
                  'BsmtQual',
                  'BsmtCond',
                  'BsmtExposure',
                  'BsmtFinType1',
                  'BsmtFinSF1',
                  'BsmtFinType2',
                  'BsmtFinSF2',
                  'BsmtUnfSF',
                  'TotalBsmtSF',
                  'GarageType',
                  'GarageYrBlt',
                  'GarageFinish',
                  'GarageCars',
                  'GarageArea',
                  'GarageQual',
                  'GarageCond',
                  'PavedDrive',
                  'WoodDeckSF',
                  'OpenPorchSF',
                  'EnclosedPorch',
                  'ThrSsnPorch',
                  'ScreenPorch')


from apis.models import interiorFeatures
 
 
class interiorFeaturesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = interiorFeatures
        fields = (
                  'Id',
                  'Heating',
                  'HeatingQC',
                  'CentralAir',
                  'Electrical',
                  'FstFlrSF',
                  'SecFlrSF',
                  'LowQualFinSF',
                  'GrLivArea',
                  'BsmtFullBath',
                  'BsmtHalfBath',
                  'FullBath',
                  'HalfBath',
                  'BedroomAbvGr',
                  'KitchenAbvGr',
                  'KitchenQual',
                  'TotRmsAbvGrd',
                  'Functional',
                  'Fireplaces',
                  'FireplaceQu',
                  'PoolArea',
                  'PoolQC',
                  'Fence',
                  'MiscFeature',
                  'MiscVal',
                  'MoSold',
                  'YrSold',
                  'SaleType',
                  'SaleCondition',
                  'SalePrice')

