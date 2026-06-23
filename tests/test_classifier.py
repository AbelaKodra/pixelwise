from backend.models.predict import predict_digit

def test_predict_digit_returns_dict():
    result = predict_digit()

    assert isinstance(result, dict)
    assert "digit" in result
    assert "confidence" in result

def test_confidence_is_float():
    result = predict_digit()

    assert isinstance(result["confidence"], float)
