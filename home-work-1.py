''' 1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
'''
def lumus_maxima(x):
    import time
    auto_light = ('Red','Yellow','Green')
    people_light = ('Red','Green')
    temp = 0
    n = True
    while True :
        for t in range(4):
            print(auto_light[0], people_light[1])
            time.sleep(1)
        for t in range(2):
            print(auto_light[1],people_light[0])
            time.sleep(1)
        for t in range(4):  
            print(auto_light[2],people_light[0])
            time.sleep(1)
        temp += 1
        if temp == x:
            break

lumus_maxima(20)
