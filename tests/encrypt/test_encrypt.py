from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    valid_test_script = [
        {"inputs": ["AABBCC", 3], "expect": "BAA_CCB"},
        {"inputs": ["ABBCCA", 4], "expect": "AC_CBBA"},
        {"inputs": ["AABBCC", -1], "expect": "CCBBAA"},
    ]
    for test in valid_test_script:
        message, key = test["inputs"]
        expect = test["expect"]

        result = encrypt_message(message, key)
        assert result == expect

    except_msg_match = "tipo inválido para message"
    except_key_match = "tipo inválido para key"

    raise_exception_test_script = [
        {"inputs": ["AABBCC", None], "message": except_key_match},
        {"inputs": [None, 1], "message": except_msg_match},
        {"inputs": [1, 1], "message": except_msg_match},
        {"inputs": [1, "1"], "message": except_key_match},
        {"inputs": [1, "AABBCC"], "message": except_key_match},
    ]
    for test in raise_exception_test_script:
        msg, key = test["inputs"]
        exception_msg = test["message"]

        with pytest.raises(TypeError, match=exception_msg):
            encrypt_message(msg, key)
