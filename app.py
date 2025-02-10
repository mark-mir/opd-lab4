from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error_message = None

    if request.method == "POST":
        try:
            function = request.form["function"]
            angle = float(request.form["angle"])
            precision = int(request.form["precision"])
            unit = request.form["unit"]

            # Переводим угол в радианы, если нужно
            if unit == "degrees":
                angle = math.radians(angle)

            # Вычисляем нужную тригонометрическую функцию
            if function == "sin":
                result = round(math.sin(angle), precision)
            elif function == "cos":
                result = round(math.cos(angle), precision)
            elif function == "tan":
                result = round(math.tan(angle), precision)
            else:
                error_message = "Неизвестная функция"

        except ValueError:
            error_message = "Ошибка ввода данных. Проверьте правильность значений."

    return render_template("index.html", result=result, error_message=error_message)


if __name__ == "__main__":
    app.run()
