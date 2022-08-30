from Dash_app import update5






def test_1():
    output = update5("all")
    assert output[0] == "Visualization Title"


    
def test_2():
    output = update5("all")
    assert output[1] == "Visualization"


def test_3():
    output = update5("all")
    assert output[2] == "Region Picker"

def ac():
    try:
        test_1()
        test_2()
        test_3()
    except AssertionError:
        return 1
    except:
        return 0

print(int(bool(ac())))
