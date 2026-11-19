import turtle
import colorsys


def draw_bmw_logo():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Luminous BMW Logo Art")
    screen.setup(800, 800)

    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(10)  # تسريع الرسم قليلاً بسبب كثرة التفاصيل
    t.hideturtle()

    # 1. رسم الخلفية الدائرية السوداء الكبيرة (الإطار الخارجي)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("#111111")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

    # 2. رسم حلقات مضيئة متداخلة للشعار (تأثير الفراكتل المضيء)
    # هذا الجزء يرسم الدائرة المركزية المقسمة لأربعة أقسام بألوان مضيئة
    for i in range(360):
        t.penup()
        t.goto(0, 0)
        t.setheading(i)

        # تقسيم الألوان إلى 4 أقسام (أزرق مضيء وأبيض مضيء بالتناوب)
        if (0 <= i < 90) or (180 <= i < 270):
            # درجات الأزرق السماوي المضيء
            hue = 0.55 + (i % 90) / 900
            color = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
        else:
            # درجات الأبيض/الفضي المضيء
            color = (0.9, 0.9, 0.9)

        t.pencolor(color)
        t.pendown()
        t.forward(140)  # نصف قطر الدائرة الداخلية

        # إضافة لمسة هندسية عند الأطراف مثل الكود الخاص بك
        if i % 5 == 0:
            t.width(2)
            t.circle(5, 180)

    # 3. رسم الإطار الدائري الفضي الخارجي المحيط بالمراوح
    t.penup()
    t.goto(0, -145)
    t.pendown()
    t.pencolor("#CCCCCC")
    t.width(4)
    t.circle(145)

    # 4. كتابة الحروف المضيئة BMW في الأعلى
    t.penup()
    t.pencolor("white")

    # حرف B
    t.goto(-50, 150)
    t.write("B", font=("Arial", 30, "bold"), align="center")

    # حرف M
    t.goto(0, 160)
    t.write("M", font=("Arial", 32, "bold"), align="center")

    # حرف W
    t.goto(50, 150)
    t.write("W", font=("Arial", 30, "bold"), align="center")

    screen.exitonclick()


draw_bmw_logo()