class Quiz
{
   constructor(type, questions, results)
   {
       //Тип теста: 1 - классический тест с правильными ответами, 2 - тест без правильных ответов
       this.type = type;
 
       //Массив с вопросами
       this.questions = questions;
 
       //Массив с возможными результатами
       this.results = results;
 
       //Количество набранных очков
       this.score = 0;
 
       //Номер результата из массива
       this.result = 0;
 
       //Номер текущего вопроса
       this.current = 0;
   }
 
   Click(index)
   {
       //Добавляем очки
       let value = this.questions[this.current].Click(index);
       this.score += value;
 
       let correct = -1;
 
       //Если было добавлено хотя бы одно очко, то считаем, что ответ верный
       if(value >= 1)
       {
           correct = index;
       }
       else
       {
           //Иначе ищем, какой ответ может быть правильным
           for(let i = 0; i < this.questions[this.current].answers.length; i++)
           {
               if(this.questions[this.current].answers[i].value >= 1)
               {
                   correct = i;
                   break;
               }
           }
       }
 
       this.Next();
 
       return correct;
   }
 
   //Переход к следующему вопросу
   Next()
   {
       this.current++;
      
       if(this.current >= this.questions.length)
       {
           this.End();
       }
   }
 
   //Если вопросы кончились, этот метод проверит, какой результат получил пользователь
   End()
   {
       for(let i = 0; i < this.results.length; i++)
       {
           if(this.results[i].Check(this.score))
           {
               this.result = i;
           }
       }
   }
}
 
//Класс, представляющий вопрос
class Question
{
   constructor(text, answers)
   {
       this.text = text;
       this.answers = answers;
   }
 
   Click(index)
   {
       return this.answers[index].value;
   }
}
 
//Класс, представляющий ответ
class Answer
{
   constructor(text, value)
   {
       this.text = text;
       this.value = value;
   }
}
 
//Класс, представляющий результат
class Result
{
   constructor(text, value)
   {
       this.text = text;
       this.value = value;
   }
 
   //Этот метод проверяет, достаточно ли очков набрал пользователь
   Check(value)
   {
       if(this.value <= value)
       {
           return true;
       }
       else
       {
           return false;
       }
   }
}

//Массив с результатами
const results =
[
   new Result("Тест завершен", 0),
   new Result("Тест завершен", 2),
   new Result("Тест завершент", 4),
   new Result("Тест завершена", 6)
];
 
//Массив с вопросами
const questions =
[
   new Question("В каком году был заложен собор?",
   [
       new Answer("1001", 0),
       new Answer("1099", 0),
       new Answer("1101", 1),
       new Answer("1100", 0)
   ]),
   new Question("Кем был заложен собор?",
   [
       new Answer("Владимир Мономах", 1),
       new Answer("Антон Иванович Шедель", 0),
       new Answer("Ярослав Мудрый", 0),
       new Answer("Алексей Михайлович Романов", 0)
   ]),
   new Question("Что еще расположено на Соборной горе?",
   [
       new Answer("комплекс артилерийского двора", 0),
       new Answer("баня", 0),
       new Answer("крепость", 0),
       new Answer("комплекс архиерейского двора", 1)
   ]),
   new Question("На какую крышу заменили тесовую?",
   [
       new Answer(" на жестяную", 1),
       new Answer("на деревянную", 0),
       new Answer("на каменную", 0),
       new Answer("на графитовую", 0)
   ]),
   new Question("Когда была возведена двухъярусная колоколня?",
   [
       new Answer("1752-1756", 0),
       new Answer("1756-1766", 0),
       new Answer("1766-1772", 1),
       new Answer("1772-1774", 0)
   ]),
   new Question("В каком году были изготовлены часы?",
   [
       new Answer("1785", 0),
       new Answer("1791", 1),
       new Answer("1789", 0),
       new Answer("1794", 0)
   ]),
   new Question("Что стоит на деревянной подставке около колокольни?",
   [
       new Answer("самовар", 0),
       new Answer("железный конь", 0),
       new Answer("колокол", 1),
       new Answer("ничего", 0)
   ]),
   new Question("Дата на нем?",
   [
       new Answer("1630", 0),
       new Answer("1636", 1),
       new Answer("1637", 0),
       new Answer("1640", 0)
   ]),
   new Question("Кем выполнен иконостас?",
   [
       new Answer("С.Трусицкий", 1),
       new Answer("А.Корольков ", 0),
       new Answer("В.Соколов", 0),
       new Answer("В.Успенский", 0)
   ]),
   new Question("Какая лучшая команда?",
   [
       new Answer("MISIS 52", 0),
       new Answer("MISIS Koptevo", 0),
       new Answer("MISIS NA MASSE", 0),
       new Answer("Все сразу", 1)
   ]),
];
 
//Сам тест
const quiz = new Quiz(1, questions, results);

Update();
 
//Обновление теста
function Update()
{
   //Проверяем, есть ли ещё вопросы
   if(quiz.current < quiz.questions.length)
   {
       //Если есть, меняем вопрос в заголовке
       document.getElementById('head').innerHTML = quiz.questions[quiz.current].text;
 
       //Удаляем старые варианты ответов
       document.querySelectorAll('.button').forEach((e) => {
        e.style.display = 'none';
       })
 
       //Создаём кнопки для новых вариантов ответов
       for(let i = 0; i < quiz.questions[quiz.current].answers.length; i++)
       {
           let btn = document.createElement("button");
           btn.className = "button";
 
           btn.innerHTML = quiz.questions[quiz.current].answers[i].text;
 
           btn.setAttribute("index", i);
 
           document.getElementById('buttons').appendChild(btn);
       }
      
       //Выводим номер текущего вопроса
       document.getElementById('pages').innerHTML = (quiz.current + 1) + " / " + quiz.questions.length;
 
       //Вызываем функцию, которая прикрепит события к новым кнопкам
       Init();
   }
   else
   {
       //Если это конец, то выводим результат
       document.querySelector('.btn-need').style.display = 'block'
//       document.getElementById('buttons').innerHTML = "<button class='btn-need'><a href='afterPlay.html'>Узнать результаты</a></button>";
       document.getElementById('head').innerHTML = quiz.results[quiz.result].text;
       
    //    document.querySelector('.wrapper1').style.display = 'block'
    //     body.appendChild(document.createElement('div').innerHTML = "<img width='100%' height='100vh' src='/images/Group1305.jpg'></img>")

       
   }
}
 
function Init()
{
   //Находим все кнопки
   let btns = document.getElementsByClassName("button");
 
   for(let i = 0; i < btns.length; i++)
   {
       //Прикрепляем событие для каждой отдельной кнопки
       //При нажатии на кнопку будет вызываться функция Click()
       btns[i].addEventListener("click", function (e) { Click(e.target.getAttribute("index")); });
   }
}
 
function Click(index)
{
   //Получаем номер правильного ответа
   let correct = quiz.Click(index);
 
   //Находим все кнопки
   let btns = document.getElementsByClassName("button");
 
   //Делаем кнопки серыми
   for(let i = 0; i < btns.length; i++)
   {
       btns[i].className = "button button_passive";
   }
 

   if(quiz.type == 1)
   {
       if(correct >= 0)
       {
           btns[correct].className = "button button_correct";
       }
  
       if(index != correct)
       {
           btns[index].className = "button button_wrong";
       }
   }
   else
   {
       //Иначе просто подсвечиваем зелёным ответ пользователя
       btns[index].className = "button button_correct";
   }
   
 
   //Ждём секунду и обновляем тест
   setTimeout(Update, 1000);
}
