import mult as model
import wiev


def button_click():
    value_a = wiev.get_value()
    value_b = wiev.get_value()
    model.init(value_a, value_b)
    result = model.multy()
    wiev.view(result)
