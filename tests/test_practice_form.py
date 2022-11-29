from demoqa.model import app
from demoqa.model.data.user import User


def test_submit_student_details(open_practice_form):
    hellen = User(
        first_name='Hellen',
        last_name='Dudareva',
        email='dudarevalen_1997@mail.ru',
        gender='Female',
        phone_number='8919860276', #098645
        date_of_birth=[28, 'December', '1997'],
        subject='Maths',
        #subject='History', 'English',
        hobby='Music',
        #hobby='Sports', 'Music',
        picture='qa.jpeg',
        address='vostok',
        state='NCR',
        city='Gurgaon'
    )

#бизнес-шаг: заполнить форму данными
    app.registration_form.register(hellen)

# бизнес-шаг: проверить форму
    app.registration_form.assert_registered(hellen)