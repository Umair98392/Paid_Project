import json
import pickle

import numpy as np
import pandas as pd
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from apis.models import (
    exteriorFeatures,
    housingConditions,
    interiorFeatures,
    localityDescription,
)
from apis.serializers import (
    exteriorFeaturesSerializer,
    housingConditionsSerializer,
    interiorFeaturesSerializer,
    localityDescriptionSerializer,
)


# Code for localityDescription
@api_view(["GET", "POST", "DELETE"])
def localityDescription_list(request):
    if request.method == "GET":
        application_data = localityDescription.objects.all()

        title = request.GET.get("title", None)
        if title is not None:
            application_data = application_data.filter(title__icontains=title)

        serializer = localityDescriptionSerializer(application_data, many=True)
        return JsonResponse(serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "POST":
        localitydescription_data = JSONParser().parse(request)
        localitydescription_serializer = localityDescriptionSerializer(
            data=localitydescription_data
        )
        if localitydescription_serializer.is_valid():
            localitydescription_serializer.save()
            return JsonResponse(
                localitydescription_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            localitydescription_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        count = localityDescription.objects.all().delete()
        return JsonResponse(
            {
                "message": "{} localityDescription were deleted successfully!".format(
                    count[0]
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def localityDescription_detail(request, pk):
    try:
        localitydescription = localityDescription.objects.get(pk=pk)
    except localityDescription.DoesNotExist:
        return JsonResponse(
            {"message": "The localitydescription does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        localitydescription_serializer = localityDescriptionSerializer(
            localitydescription
        )
        return JsonResponse(localitydescription_serializer.data)

    elif request.method == "PUT":
        localitydescription_data = JSONParser().parse(request)
        localitydescription_serializer = localityDescriptionSerializer(
            localitydescription, data=localitydescription_data
        )
        if localitydescription_serializer.is_valid():
            localitydescription_serializer.save()
            return JsonResponse(localitydescription_serializer.data)
        return JsonResponse(
            localitydescription_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        localitydescription.delete()
        return JsonResponse(
            {"message": "localityDescription was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def localityDescription_list_published(request):
    localityDescription = localityDescription.objects.filter(published=True)

    if request.method == "GET":
        localityDescription_serializer = localityDescriptionSerializer(
            localityDescription, many=True
        )
        return JsonResponse(localityDescription_serializer.data, safe=False)


# Code For housingconditions document


@api_view(["GET", "POST", "DELETE"])
def housingConditions_list(request):
    if request.method == "GET":
        application_data = housingConditions.objects.all()

        title = request.GET.get("title", None)
        if title is not None:
            application_data = application_data.filter(title__icontains=title)

        serializer = housingConditionsSerializer(application_data, many=True)
        return JsonResponse(serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "POST":
        housingconditions_data = JSONParser().parse(request)
        housingconditions_serializer = housingConditionsSerializer(
            data=housingconditions_data
        )
        if housingconditions_serializer.is_valid():
            housingconditions_serializer.save()
            return JsonResponse(
                housingconditions_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            housingconditions_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        count = housingConditions.objects.all().delete()
        return JsonResponse(
            {
                "message": "{} housingConditions were deleted successfully!".format(
                    count[0]
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def housingConditions_detail(request, pk):
    try:
        housingconditions = housingConditions.objects.get(pk=pk)
    except housingConditions.DoesNotExist:
        return JsonResponse(
            {"message": "The housingconditions does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        housingconditions_serializer = housingConditionsSerializer(housingconditions)
        return JsonResponse(housingconditions_serializer.data)

    elif request.method == "PUT":
        housingconditions_data = JSONParser().parse(request)
        housingconditions_serializer = housingConditionsSerializer(
            housingconditions, data=housingconditions_data
        )
        if housingconditions_serializer.is_valid():
            housingconditions_serializer.save()
            return JsonResponse(housingconditions_serializer.data)
        return JsonResponse(
            housingconditions_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        housingconditions.delete()
        return JsonResponse(
            {"message": "housingConditions was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def housingConditions_list_published(request):
    housingConditions = housingConditions.objects.filter(published=True)

    if request.method == "GET":
        housingConditions_serializer = housingConditionsSerializer(
            housingConditions, many=True
        )
        return JsonResponse(housingConditions_serializer.data, safe=False)


# Code for exteriorFeatures
@api_view(["GET", "POST", "DELETE"])
def exteriorFeatures_list(request):
    if request.method == "GET":
        application_data = exteriorFeatures.objects.all()

        title = request.GET.get("title", None)
        if title is not None:
            application_data = application_data.filter(title__icontains=title)

        serializer = exteriorFeaturesSerializer(application_data, many=True)
        return JsonResponse(serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "POST":
        exteriorfeatures_data = JSONParser().parse(request)
        exteriorfeatures_serializer = exteriorFeaturesSerializer(
            data=exteriorfeatures_data
        )
        if exteriorfeatures_serializer.is_valid():
            exteriorfeatures_serializer.save()
            return JsonResponse(
                exteriorfeatures_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            exteriorfeatures_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        count = exteriorFeatures.objects.all().delete()
        return JsonResponse(
            {
                "message": "{} exteriorFeatures were deleted successfully!".format(
                    count[0]
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def exteriorFeatures_detail(request, pk):
    try:
        exteriorfeatures = exteriorFeatures.objects.get(pk=pk)
    except exteriorFeatures.DoesNotExist:
        return JsonResponse(
            {"message": "The exteriorfeatures does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        exteriorfeatures_serializer = exteriorFeaturesSerializer(exteriorfeatures)
        return JsonResponse(exteriorfeatures_serializer.data)

    elif request.method == "PUT":
        exteriorfeatures_data = JSONParser().parse(request)
        exteriorfeatures_serializer = exteriorFeaturesSerializer(
            exteriorfeatures, data=exteriorfeatures_data
        )
        if exteriorfeatures_serializer.is_valid():
            exteriorfeatures_serializer.save()
            return JsonResponse(exteriorfeatures_serializer.data)
        return JsonResponse(
            exteriorfeatures_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        exteriorfeatures.delete()
        return JsonResponse(
            {"message": "exteriorFeatures was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def exteriorFeatures_list_published(request):
    exteriorFeatures = exteriorFeatures.objects.filter(published=True)

    if request.method == "GET":
        exteriorFeatures_serializer = exteriorFeaturesSerializer(
            exteriorFeatures, many=True
        )
        return JsonResponse(exteriorFeatures_serializer.data, safe=False)


# Code for interiorFeatures
@api_view(["GET", "POST", "DELETE"])
def interiorFeatures_list(request):
    if request.method == "GET":
        application_data = interiorFeatures.objects.all()

        title = request.GET.get("title", None)
        if title is not None:
            application_data = application_data.filter(title__icontains=title)

        serializer = interiorFeaturesSerializer(application_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        interiorfeatures_data = JSONParser().parse(request)
        interiorfeatures_serializer = interiorFeaturesSerializer(
            data=interiorfeatures_data
        )
        if interiorfeatures_serializer.is_valid():
            interiorfeatures_serializer.save()
            return JsonResponse(
                interiorfeatures_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            interiorfeatures_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        count = interiorFeatures.objects.all().delete()
        return JsonResponse(
            {
                "message": "{} interiorFeatures were deleted successfully!".format(
                    count[0]
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def interiorFeatures_detail(request, pk):
    try:
        interiorfeatures = interiorFeatures.objects.get(pk=pk)
    except interiorFeatures.DoesNotExist:
        return JsonResponse(
            {"message": "The interiorfeatures does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        interiorfeatures_serializer = interiorFeaturesSerializer(interiorfeatures)
        return JsonResponse(interiorfeatures_serializer.data)

    elif request.method == "PUT":
        interiorfeatures_data = JSONParser().parse(request)
        interiorfeatures_serializer = interiorFeaturesSerializer(
            interiorfeatures, data=interiorfeatures_data
        )
        if interiorfeatures_serializer.is_valid():
            interiorfeatures_serializer.save()
            return JsonResponse(interiorfeatures_serializer.data)
        return JsonResponse(
            interiorfeatures_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        interiorfeatures.delete()
        return JsonResponse(
            {"message": "interiorFeatures was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def interiorFeatures_list_published(request):
    interiorFeatures = interiorFeatures.objects.filter(published=True)

    if request.method == "GET":
        interiorFeatures_serializer = interiorFeaturesSerializer(
            interiorFeatures, many=True
        )
        return JsonResponse(interiorFeatures_serializer.data, safe=False)


@api_view(["POST"])
def house_predictions(request):

    if request.method == "POST":
        model_inputs = JSONParser().parse(request)
        features = json.load(open("apis/input_params.json", "r+"))
        model = pickle.load(open("apis/ml_model", "rb+"))

        for key in model_inputs.keys():
            if key in features:
                features[key] = model_inputs[key]
        df = pd.DataFrame([features], columns=features.keys())
        print(df.columns)
        prediction = float(np.expm1(model.predict(df)))
        prediction_json = {
            "predicted_price" : prediction
        }
        return JsonResponse(prediction_json, safe=False)
