from labkit import glucose_mgdl_to_mmol

def test_glucose_round_trip():
    assert abs(glucose_mgdl_to_mmol(90) - 4.995) < 0.01
