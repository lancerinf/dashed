from dataclasses import dataclass
from dataclasses_json import dataclass_json


# Make sure that the secret in SecretsManager contains all and only the same kays as this dataclass
@dataclass_json
@dataclass
class Credentials:
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_RO_USER: str
    POSTGRES_RO_PASSWORD: str
    GRAFANA_USER: str
    GRAFANA_PASSWORD: str


# activity_model: dict[str] = {
#     "beginTimestamp": None,
#     "activityId": None,
#     "startTimeLocal": None,
#     "activityType": {
#         "typeId": None,
#         "typeKey": None,
#         "parentTypeId": None
#     },
#     "startTimeGMT": None,
#     "distance": None,
#     "duration": None,
#     "elapsedDuration": None,
#     "movingDuration": None,
#     "elevationGain": None,
#     "elevationLoss": None,
#     "averageSpeed": None,
#     "maxSpeed": None,
#     "startLatitude": None,
#     "startLongitude": None,
#     "ownerId": None,
#     "ownerFullName": None,
#     "calories": None,
#     "averageHR": None,
#     "maxHR": None,
#     "averageRunningCadenceInStepsPerMinute": None,
#     "maxRunningCadenceInStepsPerMinute": None,
#     "averageBikingCadenceInRevPerMinute": None,
#     "maxBikingCadenceInRevPerMinute": None,
#     "averageSwimCadenceInStrokesPerMinute": None,
#     "maxSwimCadenceInStrokesPerMinute": None,
#     "steps": None,
#     "poolLength": None,
#     "unitOfPoolLength": None,
#     "timeZoneId": None,
#     "sportTypeId": None,
#     "avgPower": None,
#     "maxPower": None,
#     "aerobicTrainingEffect": None,
#     "anaerobicTrainingEffect": None,
#     "strokes": None,
#     "normPower": None,
#     "leftBalance": None,
#     "rightBalance": None,
#     "avgLeftBalance": None,
#     "max20MinPower": None,
#     "avgVerticalOscillation": None,
#     "avgGroundContactTime": None,
#     "avgStrideLength": None,
#     "avgFractionalCadence": None,
#     "maxFractionalCadence": None,
#     "trainingStressScore": None,
#     "intensityFactor": None,
#     "vO2MaxValue": None,
#     "avgVerticalRatio": None,
#     "avgGroundContactBalance": None,
#     "lactateThresholdBpm": None,
#     "lactateThresholdSpeed": None,
#     "maxFtp": None,
#     "avgStrokeDistance": None,
#     "avgStrokeCadence": None,
#     "maxStrokeCadence": None,
#     "workoutId": None,
#     "avgStrokes": None,
#     "minStrokes": None,
#     "deviceId": None,
#     "minTemperature": None,
#     "maxTemperature": None,
#     "minElevation": None,
#     "maxElevation": None,
#     "avgVerticalSpeed": None,
#     "maxVerticalSpeed": None,
#     "floorsClimbed": None,
#     "floorsDescended": None,
#     "locationName": None,
#     "lapCount": None,
#     "endLatitude": None,
#     "endLongitude": None,
#     "maxAvgPower_1": None,
#     "maxAvgPower_2": None,
#     "maxAvgPower_5": None,
#     "maxAvgPower_10": None,
#     "maxAvgPower_20": None,
#     "maxAvgPower_30": None,
#     "maxAvgPower_60": None,
#     "maxAvgPower_120": None,
#     "maxAvgPower_300": None,
#     "maxAvgPower_600": None,
#     "maxAvgPower_1200": None,
#     "maxAvgPower_1800": None,
#     "maxAvgPower_3600": None,
#     "maxAvgPower_7200": None,
#     "maxAvgPower_18000": None,
#     "minActivityLapDuration": None
# }
