import json

ios_icon_mapping = {
    "20": [1, 2, 3],
    "29": [1, 2, 3],
    "40": [1, 2, 3],
    "60": [2, 3],
    "76": [1, 2],
    "83.5": [2],
    "1024": [1]
}

def generate_ios_json():
    result = []

    for key, value in ios_icon_mapping.items():
        for multiplier in value:
            effective_size = int(float(key) * float(multiplier))
            result.append({
                "absoluteSize": effective_size,
                "fileFormat": "png",
                "name": f'_{key}@{multiplier}x',
                "namingScheme": 0,
                "scale": 0,
                "visibleScaleType": 1
            })
    return [{
        "name": "iOS App Icon (noahgilmore.com)",
        "shouldApplyAutomatically": True,
        "exportFormats": result
    }]

def main():
    print(json.dumps(generate_ios_json()))

if __name__ == "__main__":
    main()