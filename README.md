# Statistics_project

## О проекте
Целью данного проекта является изучение данных о продажах аптечной сети, с целью выявления факторов, влияющих на выручку. Набор данных является частью обучающего Курса-симулятора «Аналитик данных» Simulative (ООО «АЙТИ РЕЗЮМЕ»). Датасет представляет собой исторические данные о продажах 8 аптек, расположенных в различных районах одного и того же города. 

## Цель проекта
Главной целью данного проекта является получение инсайтов о продажах аптечной сети, выявление различных факторов, оказывающих влияние на выручку. Использование полученных инсайтов для дальнейших исследований.

## О наборе данных
Датасет был получен с https://simulative.ru/data-analyst. Он содержит транзакции 8 различных аптек, расположенных в различных районах города. Данные состоят из 22 колонкок и 45128 строк.

| Column                  | Description                             | Data Type      |
| :---------------------- | :-------------------------------------- | :------------- |
| DR_Dat 	                | дата покупки	                           | DATE           |
| DR_Tim 	                | время покупки	                          | TIME           |
| DR_NChk 	               | номер чека	                             | INT(4)         |
| DR_NDoc 	               | номер кассового документа	              | INT(4)         |
| DR_apt 	                | номер магазина (FK  shops)	             | INT(4)         |
| DR_Kkm 	                | номер кассового аппарата	               | INT(4)         |
| DR_TDoc 	               | вид документа	                          | VARCHAR(100)   |
| DR_TPay 	               | форма платежа (18  безнал, 15 нал)	     | INT(4)         |
| DR_CDrugs 	             | артикул товара	                         | INT(4)         |
| DR_NDrugs 	             | название товара	                        | VARCHAR(100)   |
| DR_Suppl 	              | поставщик	                              | VARCHAR(100)   |
| DR_Prod 	               | производитель	                          | VARCHAR(100)   |
| DR_Kol 	                | кол-во проданного товара                |	FLOAT(8)       |
| DR_CZak 	               | закупочная цена	                        | FLOAT(8)       |
| DR_CRoz 	               | розничная цена	                         | FLOAT(8)       |
| DR_SDisc 	              | сумма скидки	                           | FLOAT(8)       |
| DR_CDisc 	              | код скидки	                             | TEXT           |
| DR_BCDisc 	             | штрихкод скидки	                        | TEXT           |
| DR_TabEmpl 	            | табельный номер сотрудника (FK - employee)  |	INT(4)     |
| DR_Pos 	                | номер позиции в чеке	                   | INT(4)         |
| DR_VZak 	               | вид закупки (1 - обычный, 2 -  интернет-заказ)	| INT(4)  |

## Объекты исследования

### Аптеки
Построить доверительные интервалы по выручке каждой из 8 аптек, чтобы получить представление, в каком примерно диапазоне лежит их выручка. 
Сравнить среднюю выручку всех аптек, чтобы получить понимание, все ли аптеки в среднем продают одинаково. И есть аптеки, продажи которых значительно отличаются в большую или меньшую сторону. Для дальнейшего выявления факторов, влияющих на данные отклонения, формулировки и проверки гипотез.

### Фармацевты
Сравнить среднюю сумму продаж всех фармацевтов, чтобы выявить сотрудников с низким и высоким уровнем продах. С целью дальнейшего исследования факторов, оказывающих влияние на данный показатель, формулировки и проверки гипотез. 

Исследовать навык допродаж. Сравнить количество проданных позиций товара всех фармацевтов, чтобы выявить, насколько эффективно сотрудник владеет техниками допродаж. С целью снижения негативного влияния данного фактора на уровень продаж, например посредством проведения обучения, внедрения практики менторства и т.д. 

### Прочие факторы
Исследования способов закупки в зависимости от статуса «обычный заказ» и «интернет-заказ». Определить, есть ли статистически значимые различия в пропорциях заказов по количеству и сумме продаж в зависимости от статуса. 
Выявить наличие или отсутствие взаимосвязи между производителем и видом закупки интернет-заказ. Определить существуют ли какие-либо производители, товары которых целенаправленно заказывают онлайн. 

## Гипотезы:
(т.к. данные предоставлены только за 1 месяц, все расчеты будут производится исходя из периода 1 месяц)
0.	Построить доверительные интервалы для каждой аптеки из 8 аптек. 

1.	Сравнить среднюю выручку всех аптек за месяц.
> H0: Нет статистически значимой разницы в выручке среди 8 аптек.<br>
> Н1: Существует хотя бы одна аптека, средняя выручка которой отличается.<br>

2.	Сравнить продажи за месяц всех фармацевтов. 
H0: Нет статистически значимой разницы в продажах всех фармацевтов.
Н1: Существует хотя бы один фармацевт, продажи которого отличаются.

3.	Сравнить количество проданных позиций всех фармацевтов. 
Н0: Нет статистически значимой разницы в количестве проданных позиций для всех фармацевтов.
Н1: Существует хотя бы один фармацевт, количество проданных позиций которого отличаются.

4.	Сравнить пропорции заказов в зависимости от вида закупки «обычный» и «интернет-заказ» (т.е. сравнить пропорции заказов со статусом обычный и онлайн)
Н0: Нет статистически значимой разницы в пропорциях, в зависимости от вида закупки
Н1: Пропорция обычных заказов больше
(пропорции по количеству)

5.	Сравнить пропорции выручки, полученной от заказов в зависимости от признака «вид закупки – интернет заказ/обычный». (т.е. сколько в пропорции приносят обычные заказы, сколько онлайн)
Н0: Нет статистически значимой разницы в пропорциях, в зависимости от вида закупки
Н1: Выручка обычных заказов пропорционально больше
(пропорции по выручке)

6.	Определить, существует ли корреляция между признаками «производитель» и «вид закупки – интернет заказ». Существуют ли какие-то определенные медикаменты, которые целенаправленно заказывают онлайн. 
Н0: корреляция между признаками не отличается от нуля
Н1: корреляция между признаками отличается от нуля.


